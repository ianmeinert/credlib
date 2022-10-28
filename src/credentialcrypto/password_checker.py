import requests
import hashlib

"""
Looks up an MD5 partial hash in the 
https;//.pwnedpasswords.com API to determine if it was ever compromised

"""


def request_api_data(query_char):
    """Transmits the query_char to pwnedpassword API

    Args:
        query_char (_type_): partial MD5 hash

    Raises:
        RuntimeError: A non-200 status code was received

    Returns:
        response: the HTTP response received from the API
    """
    url = f'https://api.pwnedpasswords.com/range/{query_char}'

    res = requests.get(url, verify=True)

    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the API and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    """returns the count value of the hash_to_check
    as provided by the API

    Args:
        hashes (Response): the response from the API call
        hash_to_check (str): the string representation of a sha1 string

    Returns:
        int: count of times the hash was found
    """
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, c in hashes:
        if h == hash_to_check:
            return int(c)
    return 0


def pwned_api_check(password):
    """Checks the pwned website API for a given password to
    determine if it was potentially compromised

    Args:
        password (str): the password to check

    Returns:
        int: count of times the hash was found
    """
    # check password if it exists in API response
    sha1password = hashlib.sha1(
        password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)

    return get_password_leaks_count(response, tail)
