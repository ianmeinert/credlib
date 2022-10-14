import unittest
import pathlib as pl
from tests.unit.test_testCaseBase import TestCaseBase
from credentialcrypto.createcred import Credentials
  
class TestCreateCred(TestCaseBase):
    credential = Credentials()
        
    def init(self):
        self.credential = Credentials()
        
    def test(self):
        self.credential.username = "account"
        self.credential.password = "genericpassword"
        self.credential.hostname = "test_hostname"
        self.credential.expiry_time = "90"
        self.credential.create_cred()
        
        key = "test_hostname.key"
        key_path = pl.Path(key)
        self.assert_is_file(key_path)
        
        ini = "test_hostname_credential.ini"
        ini_path = pl.Path(ini)
        self.assert_is_file(ini_path)
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)