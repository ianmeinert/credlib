import unittest
from credentialcrypto import Credentials
import pathlib as pl

class TestCaseBase(unittest.TestCase):
                
    def assert_is_credential(self, credential):
        message = "given object is not instance of Credentials"
        self.assertIsInstance(credential, Credentials, message)
        
        
    def assert_is_file(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))
    
    
    def assert_username(self, username):
        value = "account"
        message = "First value and second value are not equal"        
        self.assertEqual(username, value, message)
    
    
    def assert_password(self, password):
        value = "genericpassword"
        message = "First value and second value are not equal"        
        self.assertEqual(password, value, message)