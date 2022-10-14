"""
The main module: Store or retrieve credentials easily

Credentials are stored in an encrypted format
"""
import time
from credentialcrypto.createcred import Credentials

def retrieve_credentials(creds):
    creds.hostname = input("Enter Hostname: ")
    
    try:
        print(creds.read_cred())
    except:
        print(f"Could not find hostname [{creds.hostname}]. Try again.")
        retrieve_credentials(creds)
    
    
def main():
    """
    The main function

    Provides a commandline driven interface to encrypt or decrypt
    credentials.
    """
    # Creating an object for Credentials class
    creds = Credentials()
    try:
        while (res:=input("Is this an existing credential? [y/N]")
            .lower()) not in {"y", "n", ""}: pass

        if res in {"y"}:
            retrieve_credentials(creds)
        else:
            #Accepting credentials
            creds.username = input("Enter Username: ")
            creds.password = input("Enter Password: ")
            creds.hostname = input("Enter Hostname: ")
            print("Enter expiry time in days, [default:no expiry]")
            creds.expiry_time = int(input("Enter time: ") or '-1')            
            
            #calling the Credential
            creds.create_cred()
            print("**"*20)
            print(f"Cred file created successfully at {time.ctime()}")
            print("**"*20)
    except KeyboardInterrupt:
        quit()
    
    #remove from memory
    del creds


if __name__ == "__main__":
    main()
