# your code goes here!
# lib/email_address_parser.py

class EmailAddressParser:
    def __init__(self):
        pass 

    def parse_email_address(self, email):
        username, domain = email.split('@')
        return {'username': username, 'domain': domain}


if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
