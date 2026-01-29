---
kernelspec:
  name: python3
  display_name: 'Python 3'
---


```{code-cell} python
:tags: remove-cell

from IPython.display import display, Markdown, Latex, display_markdown

```



```{code-cell} python
#:tags: remove-input


import bidsbook.bids_utils

bids_layout = bidsbook.bids_utils.get_raw_layout()

output=''
for task in bids_layout.get_tasks():
	output += (f'*{task}* \n')

display(Markdown(output))
```
