## Installation
The package requires `python 3.10` to be installed
  
Navigate to the project path and run the below from the command line:
  ```
  C:\> py -m build
  C:\> cd dist
  C:\dist> pip install credentialcrypto-[version].tar.gz
  ```
The build script will use the configuration in the `setup.cfg` file, so needs to be run from the same path.

The package is installed so that it can be imported into any python project or run from the command line. The below command will present the available options for the program
  ```
  C:\> py -m credentialcrypto
  ```