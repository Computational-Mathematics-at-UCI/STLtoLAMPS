# STLtoLAMMPS
Tool to convert CAD designs into particle models of surfaces importable in [LAMMPS](https://www.lammps.org/)

## Install 

We suggest using with this application the Python distribution of Anaconda:

Install [Anacoda](https://www.anaconda.com/products/distribution)

### Enviroment needed:

conda create --name=pyoccenv python=3.9

conda activate pyoccenv

conda install -c conda-forge pythonocc-core

conda install -c conda-forge jupyter

conda install -c conda-forge jupyter_contrib_nbextensions


#### On linux recommended 

conda install -c conda-forge  blas=1.0=mkl

conda install -c conda-forge  mkl



### Optional

conda install -c conda-forge -c trelau pyocct

conda install -c conda-forge -c cadquery ocp


### Clone repo

git clone https://github.com/Computational-Mathematics-at-UCI/STLtoLAMPS.git

cd STLtoLAMPS

pip install --user -e .

### Test on jupyter notebook on doc directory



