import unittest
from tests.unit.test_testCaseBase import TestCaseBase
from credentialcrypto.createcred import Credentials
  
class TestCreateCred(TestCaseBase):
    credential = Credentials()
    decrypted_text = ""
        
    def init(self):
        self.credential = Credentials()
        
    def test(self):
        self.credential.hostname = "test_hostname"
        self.decrypted_text = self.credential.read_cred()
        
        self.assert_username(self.decrypted_text["username"])
        self.assert_password(self.decrypted_text["password"])
    # { 'username':username, 'password': password }
        
        
if __name__ == '__main__':
    unittest.main()