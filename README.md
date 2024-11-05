# py_polyhedral
The Python bindings to *polyhedral_common*.

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

Then this can be used via for example:
```sh
import py_polyhedral
M_iso = [ [ -4, 4, 4 ], [ 4, -2, -3 ], [ 4, -3, -3 ] ]
output_iso = py_polyhedral.compute_isotropic_vector(M_iso)
```

