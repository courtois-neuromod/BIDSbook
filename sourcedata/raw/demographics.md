---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

```{code-cell} python
:tags: remove-cell
import pandas as pd
import os
import pathlib
import plotly.express as px

BIDS_STUDY_PATH = pathlib.Path(os.environ.get('BIDS_STUDY'))

raw_bids_paths = []

for raw_dataset_path in BIDS_STUDY_PATH.glob('sourcedata/*/'):
  if (raw_dataset_path / 'dataset_description.json').exists():
    raw_bids_paths.append(raw_dataset_path)

```

```{code-cell} python
:tags: remove-input

for raw_dataset_path in raw_bids_paths:

  participants_data = pd.read_csv(raw_dataset_path/'participants.tsv', delimiter='\t')
  fig = px.histogram(participants_data, x="age", color="sex", title="Age Distribution by Gender", range_x=[0,100], nbins=50)
  fig.show()

```

```{code-cell} python
:tags: remove-input

participants_data

```
