# Particles

Author  : Sam Hocking

Particles.morpho is a module to facilitate populating a mesh with point particles and moving those particles on the mesh surface subject to a specified force vector. 

## Installation

Place Particles.morpho in the same directory as the `Morpho` script that requires the module (i.e. the included particles_demo.morpho file) and include the following in the script:
```
import "Particles.morpho"
```
### Contents

Particle projection and movement demonstrations:
- particles_demo.morpho
- particles_thomson_demo.morpho

Utilities:
- RandomPoints.morpho
- DictlikeSetOps.morpho
- LinAlgTools.morpho
- MeshChecker.morpho
- Tester.morpho

Primary performance testing file:
- particles_testing_demo.morpho

And related files are to facilitate testing by exporting performance dicts in plaintext to `Python`, forming a `DataFrame`, and plotting with `matplotlib`:
- dictImportTools.py
- dictPlotter.py
- dictToPython.morpho