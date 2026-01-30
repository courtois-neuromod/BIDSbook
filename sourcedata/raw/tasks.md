---
kernelspec:
  name: python3
  display_name: 'Python 3'
bidsbook:
  required_path: 'sourcedata/*/dataset_description.json'
---

```{code-cell} python
#:tags: remove-input

from IPython.display import display, Markdown, Latex, display_markdown

import bidsbook.bids_utils

bids_layout = bidsbook.bids_utils.get_raw_layout()

output=''
for task in bids_layout.get_tasks():
	output += (f'*{task}* \n')

display(Markdown(output))
```
