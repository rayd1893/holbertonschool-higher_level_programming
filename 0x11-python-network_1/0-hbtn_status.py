#!/usr/bin/python3

'''Print status'''


if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print('Body response:')
        print('\t- type: {}'.format(content.__class__))
        print('\t- content: {}'.format(content))
        print('\t- utf8 content: {}'.format(content.decode('utf-8')))
