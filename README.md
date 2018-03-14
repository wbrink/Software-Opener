# Software Opener

This program utilizes pyqt5 to create a gui that reads in a UPC barcode and opens up the software that is associated with that UPC code.


#### UPC Dictionary
In main.py
```Python
from software_dict import software_dict
```
This program is implemented assuming the following type of dictionary.  
```python
software_dict = {'UPC Code': {'Spotify': r'path\to\spotify\SpotifyLauncher.exe'},
                 'Another UPC': {'Google Chrome': r'path\to\chrom\chrome.exe'}}
```

Installation paths vary, and this dictionary is easier to implement from scratch.
