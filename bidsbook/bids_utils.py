import os
import bids
import pathlib

BIDS_STUDY_PATH = pathlib.Path(os.environ.get('BIDS_STUDY'))

def get_raw_layout():

    for raw_dataset_path in BIDS_STUDY_PATH.glob('sourcedata/*/'):
        if (raw_dataset_path / 'dataset_description.json').exists():
            indexer = bids.BIDSLayoutIndexer(index_metadata=True)
            return bids.BIDSLayout(
                raw_dataset_path,
                database_path=raw_dataset_path / '.pybids_cache',
                indexer=indexer,
            )
