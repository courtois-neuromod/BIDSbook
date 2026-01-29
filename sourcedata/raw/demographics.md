---
jupyter:
  jupytext:
    text_representation:
      extension: .mystnb
      format_name: myst
      format_version: 0.13
      jupytext_version: 1.19.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```{code-cell} python
:tags: [remove-cell]
import bids
import os
import pathlib
import plotly.express as px

BIDS_STUDY_PATH=pathlib.Path(os.environ.get('BIDS_STUDY'))

bids_layout = bids.BIDSLayout(
    BIDS_STUDY_PATH / 'sourcedata'/'raw',
    database_path=BIDS_STUDY_PATH / '.pybids_cache'
)

participants_tsv = bids_layout.get(suffix='participants', extension='tsv')[0]
participants_data=participants_tsv.get_df()
```

```{code-cell} python
:label: fig2cell
:tags: remove-input

fig = px.histogram(participants_data, x="age", color="sex", title="Age Distribution by Gender", range_x=[0,100], nbins=50)
fig.show()
```
