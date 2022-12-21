# If the security of your account is truly important to you,
# you should find out if your password has ever been compromised,
# and if you want to do this You're probably going to use one of the websites or apps,
# and I should warn you that doing so puts you at risk of being hacked in some way,
# because the password you entered on this website was actually taken and stored
# in a sizable database somewhere in the world,
# and you have no idea what will happen to it from there.

# To address this issue I'll create a program that examines the password
# and determines whether it has ever been compromised and how many times,
# By retrieving some information from a database that is specifically designed
# to keep track of these instances and
# completing the entire process on your device without
# your password leaving your computer, In this instance,
# you can be certain that it has never been hacked and that you are totally secure.
# No platform or person in the world is aware of your password.


# =>  => Program logic is as follows:
# => create a function that sends a request to the destination website and returns data.
# => Convert our password to sha1 using hashlib library
# => Search for all compromised passwords that began with the
# same five characters or numbers as ours hash started with {k-anonymity}.
# => We now compare the remaining hash of our password with the hash that we obtained after having a list of all
# the passwords that were converted to sha1 and began with the same beginning as ours.
# => It will now display our password in sha1 hash format along with the number of hacks that it has experienced.


import requests
import hashlib
import sys


# Make a request to a pwnedpasswords.com, and return the status code
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[0:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'=> {password} was found {count} time... you should probably change this password')
        else:
            print(f'=> {password} was NOT found. Carry on!')
    return '_-Done!-_'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
