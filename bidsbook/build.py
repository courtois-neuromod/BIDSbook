import pathlib
import .bids_utils

BIDS_BOOK_DATA_PATH = pathlib.Path()


RAW_BIDS_TOC = {
    'title': 'Raw data',
    'file': BIDS_BOOK_DATA_PATH / 'sourcedata',
    'children': [
        {
            'title': 'Demographics',
            'file': BIDS_BOOK_DATA_PATH / 'sourcedata' / 'demographics'
        },
        {
            'title': 'Acquisitions',
            'file': BIDS_BOOK_DATA_PATH / 'sourcedata' / 'acquisitions',
            'children': [
                {
                    'modality':
                    'title': 'MRI',
                    'file': BIDS_BOOK_DATA_PATH / 'sourcedata' / 'demographics'
                },
                {
                    'title': 'Physio',
                    'file': BIDS_BOOK_DATA_PATH / 'sourcedata' / 'acquisitions'
                }
            ]
        }
    ]
}

def study2toc(study_path: pathlib.Path):
    toc = []
    raw_layout = get_raw_layout()
    if raw_layout:
        toc.append({
            'file': BIDS_BOOK_DATA_PATH / 'sourcedata',
        })
