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

# Changelog

## v1.1

- Added a password compromise option
  - This adds a menu option to allow the user to validate the password against an API to determine if the password was ever compromised
  
  **<u>NOTE</u>:** SSL is necessary for this call, as it connects to the [pwned API](https://api.pwnedpasswords.com/range/). The call will fail if there is any issues with either certificate