# py_polyhedral
The Python bindings to the C++ package *polyhedral_common* available at 


## Installation

The installation is done first by building some environment. This can be done for example by:
```sh
python3 -m venv $HOME/my_environment
source $HOME/my_environment/bin/activate
```

Then the installation is done in the following way:
```sh
pip3 install git+https://github.com/MathieuDutSik/py_polyhedral -vvv
```
which will compile the C++ binaries of polyhedral and install them.

Related install commands:
```sh
pip3 uninstall py_polyhedral
pip3 install --force-reinstall git+https://github.com/MathieuDutSik/py_polyhedral -vvv
pip3 install --no-cache-dir git+https://github.com/MathieuDutSik/py_polyhedral -vvv
pip3 install --force-reinstall --no-cache-dir git+https://github.com/MathieuDutSik/py_polyhedral -vvv
```


## Usage

Then this can be used via the following stuff:

### Isotropic vector

It is done in the following way for isotropic vector
```python
import py_polyhedral
M_iso = [ [ -4, 4, 4 ], [ 4, -2, -3 ], [ 4, -3, -3 ] ]
py_polyhedral.compute_isotropic_vector(M_iso)
```

For non-isotropic we return `None`:
```python
import py_polyhedral
M_noniso = [ [ -3, 0, 0 ], [ 0, 1, 0 ], [ 0, 0, 1 ] ]
py_polyhedral.compute_isotropic_vector(M_noniso)
```

### Copositivity

Testing copositivity is done in the following way:
```python
import py_polyhedral
M_horn = [ [ 1, -1, 1, 1, -1 ], [ -1, 1, -1, 1, 1 ], [ 1, -1, 1, -1, 1 ], [ 1, 1, -1, 1, -1 ], [ -1, 1, 1, -1, 1 ] ]
py_polyhedral.test_copositivity(M_horn)
```

Test complete positivity is done in the following way:
```python
import py_polyhedral
M_berman = [ [ 2, 1, 0, 0, 1 ], [ 1, 2, 1, 0, 0 ], [ 0, 1, 2, 1, 0 ], [ 0, 0, 1, 2, 1 ], [ 1, 0, 0, 1, 2 ]
py_polyhedral.test_complete_positivity(M_berman)
```

### Indefinite form computation

Computing the automorphism group of an indefinite form is done in the following way:
```python
import py_polyhedral
M = [[0,1,0,0],[1,0,0,0],[0,0,0,2],[0,0,2,0]]
py_polyhedral.indefinite_form_automorphism_group(M)
```

Testing equivalence of indefinite forms is done in the following way:
```python
import py_polyhedral
M1 = [[0,1,0,0],[1,0,0,0],[0,0,0,2],[0,0,2,0]]
M2 = [[0,2,0,0],[2,0,0,0],[0,0,0,1],[0,0,1,0]]
py_polyhedral.indefinite_form_test_equivalence(M1, M2)
```

Compute orbit representative of vectors is done in the following way:
```python
import py_polyhedral
M = [[0,1,0,0],[1,0,0,0],[0,0,0,2],[0,0,2,0]]
py_polyhedral.indefinite_form_get_orbit_representative(M, 4)
```

The computation of isotropic planes can be done in the following way:
```python
import py_polyhedral
M = [[0,1,0,0],[1,0,0,0],[0,0,0,2],[0,0,2,0]]
py_polyhedral.indefinite_form_isotropic_k_plane(M, 2)
```

### Canonical form computation

The computation of canonical form of positive definite quadratic forms is done in the following way:
```python
import py_polyhedral
M = [ [ 2, -1, 0, 0, 0 ], [ -1, 2, -1, 0, 0 ], [ 0, -1, 2, -1, 0 ], [ 0, 0, -1, 2, -1 ], [ 0, 0, 0, -1, 2 ] ]
py_polyhedral.compute_canonical_form(M)
```

### Reflective lattices

Testing the reflectivity of lorentzian form is done in the following way:
```python
import py_polyhedral
M = [ [ 10, 0, 0 ], [ 0, 0, -1 ], [ 0, -1, 0 ] ]
py_polyhedral.lorentzian_reflective_edgewalk(M)
```

### Delaunay polytopes

The computation of Delaunay polytopes is done in the following way:
```python
import py_polyhedral
M = [[2,1,1,0,1,1], [1,4,1,1,1,3], [1,1,2,1,1,1], [0,1,1,2,1,2], [1,1,1,1,2,2], [1,3,1,2,2,4] ]
py_polyhedral.lattice_compute_delaunay(M)
```

### Dual description

The computation of dual description of polytope according to symmetries is done in the following way:
```python
import py_polyhedral
EXT = [[1,0,0],[1,1,0],[1,0,1],[1,1,1]]
GRP = [[0,2,1,3]]
py_polyhedral.dual_description(EXT, GRP)
```

## Dependencies

Following links are of interest:

  * The original C++ code: https://github.com/MathieuDutSik/polyhedral_common
  * How to package with setuptools: https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
  * The packaging for GAP: https://github.com/MathieuDutSik/gap_polyhedral
