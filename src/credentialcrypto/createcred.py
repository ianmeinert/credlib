"""
Encypts a logon credential

Outputs a credential file and key
"""

import ctypes
import os
import sys
from datetime import date, datetime
from cryptography.fernet import Fernet


class Credentials():
    """Class representing the credentials"""
    __username = ""
    __key = ""
    __password = ""
    __hostname = ""
    __key_file = ""
    __time_of_exp = -1
    __cred_file = ""

    def init(self):
        """
        :username value: the value of the username
        :key value: the value of the key
        :password value: the value of the password
        :hostname value: the name of the hostname
        :key_file value: the name of the key file
        :time_of_exp value: the value of the credential expiration
        :cred_file value: the value of the credential file
        """
        self.__username = ""        
        self.__key = Fernet.generate_key()
        self.__password = ""
        self.__hostname = ""
        self.__key_file = ""
        self.__time_of_exp = -1
        self.__cred_file = ""

    # ----------------------------------------
    # Getter setter for attributes
    # ----------------------------------------

    @property
    def username(self):
        """
        Gets the username
        """
        return self.__username

    @username.setter
    def username(self, username):
        while username == '':
            username = input('Username may not be blank: ')
        
        self.__key = Fernet.generate_key()
        fernet_key = Fernet(self.__key)
        self.__username = fernet_key.encrypt(username.encode()).decode()
        del fernet_key

    @property
    def password(self):
        """
        Gets the password
        """
        return self.__password

    @password.setter
    def password(self, password):
        fernet_key = Fernet(self.__key)
        self.__password = fernet_key.encrypt(password.encode()).decode()
        del fernet_key

    @property
    def hostname(self):
        """
        Gets the hostname
        """
        return self.__hostname

    @hostname.setter
    def hostname(self, hostname):
        while hostname == '':
            hostname = input('Hostname may not be blank: ')
        self.__hostname = hostname
        self.__key_file = self.__hostname+'.key'
        self.__cred_file = self.__hostname+'_credential.ini'

    @property
    def expiry_time(self):
        """
        Gets the expiry_time
        """
        return self.__time_of_exp

    @expiry_time.setter
    def expiry_time(self, exp_time):
        self.__time_of_exp = exp_time

    def create_cred(self):
        """
        This function is responsible for encrypting the password and create
        key file for storing the key and create a credential file with user
        name and password
        """
        with open(self.__cred_file, 'w', encoding="utf-8") as file_in:
            username = f"Username={self.__username}\n"
            password = f"Password={self.__password}\n"
            expiry = f"Expiry={self.__time_of_exp}\n"
            entry = f"#Credential file:\n{username}{password}{expiry}"
            file_in.write(entry)
            file_in.write("++"*20)

        # If there exists an older key file, This will remove it.
        if os.path.exists(self.__key_file):
            os.remove(self.__key_file)

        # Open the Key.key file and place the key in it.
        # The key file is hidden.
        try:

            os_type = sys.platform

            with open(self.__key_file, 'w', encoding="utf-8") as key_in:
                key_in.write(self.__key.decode())
                # Hidding the key file.
                # The below code snippet finds out which current os the scrip
                # is running on and does the task base on it.
                if os_type == 'win32':
                    ctypes.windll.kernel32.SetFileAttributesW(
                        self.__key_file, 2)
                else:
                    pass

        except PermissionError:
            os.remove(self.__key_file)
            print("A Permission error occurred.\n Please re run the script")
            
            sys.exit()

    def read_cred(self):
        """
        This function is responsible for decrypting the password in the
        credential file
        """
        key = ''
        username = ''
        password = ''

        with open(self.__key_file, 'r', encoding="utf-8") as key_in:
            key = key_in.read().encode()

        fernet_key = Fernet(key)
        with open(self.__cred_file, 'r', encoding="utf-8") as cred_in:
            lines = cred_in.readlines()
            config = {}
            for line in lines:
                tuples = line.rstrip('\n').split('=', 1)
                if tuples[0] in ('Username', 'Password'):
                    config[tuples[0]] = tuples[1]

            username = fernet_key.decrypt(config['Username'].encode()).decode()
            password = fernet_key.decrypt(config['Password'].encode()).decode()
            
        return { 'username':username, 'password': password }
    

    def isExpired(self):
        """
        This function sets the expiry of the credentials
        """
        
        with open(self.__cred_file, 'r', encoding="utf-8") as cred_in:            
            # find the line containing the expiry period
            for line in cred_in:
                tuples = line.rstrip('\n').split('=', 1)

                if tuples[0] in ('Expiry'):
                    self.__time_of_exp = tuples[1]

        # check if there is an expiry on the token
        
        if not(self.__time_of_exp) == -1:
            try:                    
                # get the key creation time
                key_created = os.path.getctime(self.__key_file)
                # convert timestamp into DateTime object
                key_date = datetime.fromtimestamp(key_created).date()
                
                today = date.today()

                # get the difference between two dates as timedelta object
                diff = (today - key_date).days
                is_expired = diff > int(self.__time_of_exp)
                
                return is_expired
            except:
                raise FileNotFoundError("Missing key file")
        else:
            #if no expiration
            return False