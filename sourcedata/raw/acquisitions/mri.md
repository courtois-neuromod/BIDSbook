---
kernelspec:
  name: python3
  display_name: 'Python 3'
bidsbook:
  required_path: 'sourcedata/**/{anat,func,dwi,fmap}'
---


```{code-cell} python
:tags: remove-cell

import pandas as pd
from IPython.display import display, Markdown, Latex, display_markdown

```

```{code-cell} python
#:tags: remove-input


import bidsbook.bids_utils

bids_layout = bidsbook.bids_utils.get_raw_layout()

scanners_tables = []

mri_serial_numbers = bids_layout.get_DeviceSerialNumber()

if len(mri_serial_numbers) > 0:
	for serial_number in mri_serial_numbers:
		scanners_tables.append({
			'Site': bids_layout.get_InstitutionName(DeviceSerialNumber=serial_number)[0],
			'Manufacturer': bids_layout.get_Manufacturers(DeviceSerialNumber=serial_number)[0],
			'Magnetic Field Strength': bids_layout.get_MagneticFieldStrength(DeviceSerialNumber=serial_number)[0],
		})

pd.DataFrame(scanners_tables)
```
