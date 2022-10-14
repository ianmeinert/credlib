import unittest
from tests.unit.test_testCaseBase import TestCaseBase
from credentialcrypto import Credentials
from credentialcrypto.createcred import Credentials
   
class TestCredential(TestCaseBase):
    credential = Credentials()
        
    def init(self):
        self.credential = Credentials()
        
    def test(self):        
        self.credential.username = "account"
        self.credential.password = "genericpassword"
        self.credential.hostname = "test_hostname"
        self.credential.expiry_time = "90"
        
        self.assert_is_credential(self.credential)

if __name__ == "__main__":
    unittest.main(verbosity=2)