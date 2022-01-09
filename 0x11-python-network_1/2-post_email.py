#!/usr/bin/python3
'''Send value method POST'''

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    from sys import argv
    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
