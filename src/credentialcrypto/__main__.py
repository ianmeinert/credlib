"""
The main module: Store or retrieve credentials easily

Credentials are stored in an encrypted format
"""
import time
from credentialcrypto.createcred import Credentials
import credentialcrypto.password_checker as Checker


def retrieve_credentials(creds):
    creds.hostname = input("Enter Hostname: ")

    try:
        print(creds.read_cred())
    except:
        print(f"Could not find hostname [{creds.hostname}]. Try again.")
        retrieve_credentials(creds)


def check_password(password):
    # check if password was breached
    count = Checker.pwned_api_check(password)
    if count:
        print(
            f'Provided password was found {count} times... you should probably change your password')
    else:
        print(f'{password} was NOT found. Carry on!')

    return count


def main():
    """
    The main function

    Provides a commandline driven interface to encrypt or decrypt
    credentials.
    """
    # Creating an object for Credentials class
    creds = Credentials()
    try:
        while (res := input("Is this an existing credential? [y/N]")
               .lower()) not in {"y", "n", ""}:
            pass

        if res in {"y"}:
            retrieve_credentials(creds)
        else:
            # Accepting credentials
            creds.username = input("Enter Username: ")
            pass_input = input("Enter Password: ")

            while True:
                # Enable password validation
                do_check_pw = input(
                    'Check if your password may have been compromised? [y/N]')
                try:
                    if (do_check_pw.lower() == "y" and check_password(pass_input) > 0
                            and input('Would you like to enter a new password? [y/N]').lower() == "y"):
                        pass_input = input("Enter Password: ")
                        continue
                    else:
                        break
                except:
                    print(
                        "Unable to verify at this time. Continuing without check")
                    break

            creds.password = pass_input
            # remove the cleartext now that its no longer needed
            del pass_input

            creds.hostname = input("Enter Hostname: ")
            print("Enter expiry time in days, [default:no expiry]")
            creds.expiry_time = int(input("Enter time: ") or '-1')

            # calling the Credential
            creds.create_cred()
            print("**"*20)
            print(f"Cred file created successfully at {time.ctime()}")
            print("**"*20)
    except KeyboardInterrupt:
        quit()

    # remove from memory
    del creds


if __name__ == "__main__":
    main()
