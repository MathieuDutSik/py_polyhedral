py_polyhedral
=============
The Python bindings to the C++ package *polyhedral_common* available at 


Installation
------------

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


Usage
-----

Then this can be used via for example:
```sh
import py_polyhedral
M_iso = [ [ -4, 4, 4 ], [ 4, -2, -3 ], [ 4, -3, -3 ] ]
output_iso = py_polyhedral.compute_isotropic_vector(M_iso)
```

Dependencies
------------

Following links are of interest:

  * The original C++ code: https://github.com/MathieuDutSik/polyhedral_common
  * How to package with setuptools: https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
  * The packaging for GAP: https://github.com/MathieuDutSik/gap_polyhedral
