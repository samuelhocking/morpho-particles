# Particles

Author  : Sam Hocking

Particles.morpho is a module to facilitate populating a mesh with point particles and moving those particles on the mesh surface subject to a specified force vector. 

## Installation

None required except dependent packages:
- numpy
- matplotlib
- pandas
- copy
- scipy

Place Particles.morpho in the same directory as the `Morpho` script that requires the module (i.e. the included particles_demo.morpho file) and include the following in the script:
```
import "Particles.morpho"
```

The other included files are to facilitate testing of the `Particles` module by exporting performance dicts in plaintext to `Python`, forming a `DataFrame`, and plotting with `matplotlib`:
- dictImportTools.py
- dictPlotter.py
- dictToPython.morpho

The testing script is under revision and currently unavailable.