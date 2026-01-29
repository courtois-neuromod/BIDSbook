"""
Script that retrieve the metadata from `dataset_description.json` and 
`CITATION.cff` if exist, to configure the myst.yml file
"""

import yaml
from pathlib import Path
from bids import BIDSLayout

YAML_JSON = {
    'title': 'Name',
    'authors': {
        'name': 'Authors'
    },
    'funding': {
        'name': 'Funding'
    },
    'tags': 'Keywords',
    'license': 'License',
    'doi': 'DatasetDOI'
}

YAML_CFF = {
    'title': 'title',
    'authors': {
        'name': {
            'values': ['given-names', 'family-names'],
            'transform': lambda g, f: f"{g} {f}"
        },
        'orcid': 'orcid'
    },
    'doi': 'identifiers'
}

def metadata2yml(bids_path):
    ## Create yaml file if it doesn't exist
    yaml_path = Path("../myst.yml")
    yaml_path.touch(exist_ok=True)

    # Load content of yaml file
    with open(yaml_path, 'r') as file:
        yaml_data = yaml.safe_load(file)

    # Load content of dataset_description
    bids_path = Path(bids_path)
    bids_layout = BIDSLayout(bids_path)

    description = bids_layout.description

    # Update yaml_data based on the content of description
    yaml_data = get_dataset_description(description, yaml_data)

    # Check if CITATION.cff file exists in bids_path
    citation_path = bids_path / 'CITATION.cff'

    if citation_path.exists():
        try:
            with open(citation_path, 'r', encoding='utf-8') as cff_file:
                # Use safe_load to prevent execution of arbitrary code
                cff_data = yaml.safe_load(cff_file)
            # Since CITATION.cff has precedence over dataset_description.json,
            # we update the yaml_data given the information in that file
            yaml_data = get_citation(cff_data, yaml_data) 

        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Save the yml file
    with open('../myst.yml', 'w') as file:
        yaml.dump(yaml_data, file)


def get_dataset_description(description, metadata):
    for k, v in YAML_JSON.items():
        if isinstance(v, str):
            if v in description.keys():
                metadata.update({
                    k: description[v]
                })
        else:
            for key, value in v.items():
                metadata.update({
                    k: [{key: i} for i in description[value]]
                })

    return metadata

def get_citation(citation, metadata):
    for k, v in YAML_CFF.items():
        if isinstance(v, str):
            if v == 'identifiers':
                if citation[v][0]['type'] == k:
                    metadata.update({
                        k: citation[v][0]['value']
                    })
            elif v in citation.keys():
                metadata.update({
                    k: citation[v]
                })
        elif isinstance(v, dict):
            sources = citation[k]
            if isinstance(sources, list):
                tmp_sources = []
                for source in sources:
                    tmp_dict = {}
                    for key, value in v.items():
                        if isinstance(value, dict):
                            if isinstance(value['values'], list):
                                citation = [source[v] for v in value['values']]
                            tmp_dict.update({
                                key: value['transform'](*citation)
                            })
                        else:
                            if value in source.keys():
                                tmp_dict.update({
                                    key:source[value]
                                })
                    tmp_sources.append(tmp_dict)
                metadata.update({
                    k: tmp_sources
                })
        else:
            raise IOError(f'Can not process field {v}')
    return metadata