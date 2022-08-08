# Particles Module

Author  : Sam Hocking

Particles.morpho is a module to facilitate populating a mesh with point particles and moving those particles on the mesh surface subject to a specified force vector. 

## Installation

Place Particles.morpho in the same directory as the `Morpho` script that requires the module (i.e. the included particles_demo.morpho file) and include the following in the script:
```
import "Particles.morpho"
```
## Contents

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

And related files to facilitate testing by exporting performance dicts in plaintext to `Python`, forming a `DataFrame`, and plotting with `matplotlib`:
- dictImportTools.py
- dictPlotter.py
- dictToPython.morpho

## Usage

The typical process to use the `Particles` module is to:
1. Initialize `mesh`
2. Initialize list of random points using `RandomPoints`
3. Initialize a `Particles` object
4. Project random points onto mesh
5. Apply force vectors to mesh particles

## RandomPoints

The `RandomPoints` module is used to generate a list of random coordinate vectors.

`GenRandomRectangle` produces points within a rectangular prism region:
```
var ptsArr = GenRandomRectangle(1000, xBounds=[-2,2], yBounds=[-2,2], zBounds=[-2,2])
```

`GenParametrizedBall` produces deterministic (non-random) points within a parameterized ball:
```
var ptsArr = GenParametrizedBall(r=1, usteps=5, vsteps=5, wsteps=5)
```
`usteps` controls the number of longitudinal steps
`vsteps` controls the number of latitudinal steps
`wsteps` controls the number of steps along the radius

`GenRandomSphere` produces random points on the surface of a sphere of radius `r`:
```
var ptsArr = GenRandomSphere(1000, r=1)
```

`GenRandomBall` produces random points within a spherical ball region withi radius `r`:
```
var ptsArr = GenRandomBall(1000, r=1)
```

## Initialization

Initializing a `Particles` object is easy. Pass the mesh object as an argument to the `Particles` constructor:
```
var p = Particles(mesh)
```

## Projection

Projecting points in space onto the mesh surface is also simple. Call the `project` method with the list of points as an argument:
```
p.project(ptsArr)
```

(Under construction)

## Forces

The `Particles` module offers multiple force objects.

### Pairwise

`PairwiseForce` computes a force based on the locations of a pair of particles

### SinglePosition

`SinglePositionForce` computes a force based on the location of a single particle

### Constant

`ConstantForce` computes a constant force

## Movement

Force vectors can be applied to move particle either in two ways.

### moveAll

`moveAll` computes the set of force vectors for the entire set of vectors at once, then moves them sequentially. Calling `moveAll` will take one step of the specified force.
```
p.moveAll(ConstantForce(Matrix([1,0,0])), stepsize=1, quiet=true)
```

### moveAllLoop

`moveAllLoop` takes a specified number of `moveAll` steps.
```
p.moveAllLoop(1000, ElectrostaticPairwise(), stepsize=0.0001, stepQuiet=true, loopQuiet=true)
```

### moveOneByOne

`moveOneByOne` computes one force vector at a time, moves that particles, then calculates the next force vector. It has the same arguments as `moveAll`.

### moveOneByOneLoop

`moveOneByOneLoop` takes a specified number of `moveOneByOne` steps and has the same arguments as `moveAllLoop`.