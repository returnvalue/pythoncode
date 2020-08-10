# Requests is a Python HTTP library, released under the Apache License 2.0. The goal of the project is to make HTTP requests
# simpler and more human-friendly. It is one of the most popular python libraries that is not included with python by default.

import requests


# Making A GET Request
def printResponse(resp):
    print(f'Response Code: +----- {resp.status_code} -----+')
    print('\n')

    print('Headers: +----------------------+')
    print(resp.headers)
    print('\n')

    print('Returned data: +----------------------+')
    print(resp.text)


# Use requests to issue an HTTP GET request
url = 'http://httpbin.org/xml'
resp = requests.get(url)
printResponse(resp)


# Response Code: +----- 200 -----+
#
#
# Headers: +----------------------+
# {'Date': 'Wed, 11 Mar 2020 18:03:20 GMT', 'Content-Type': 'application/xml', 'Content-Length': '522', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
#
#
# Returned data: +----------------------+
# <?xml version='1.0' encoding='us-ascii'?>
#
# <!--  A SAMPLE set of slides  -->
#
# <slideshow
#     title="Sample Slide Show"
#     date="Date of publication"
#     author="Yours Truly"
#     >
#
#     <!-- TITLE SLIDE -->
#     <slide type="all">
#       <title>Wake up to WonderWidgets!</title>
#     </slide>
#
#     <!-- OVERVIEW -->
#     <slide type="all">
#         <title>Overview</title>
#         <item>Why <em>WonderWidgets</em> are great</item>
#         <item/>
#         <item>Who <em>buys</em> WonderWidgets</item>
#     </slide>
#
# </slideshow>
#
# Process finished with exit code 0

# Including Parameters
# Send some parameters to the URL via a GET request
# Requests handles this for you, no manual encoding
payload = {'Size': 'Large', 'Cream': True, 'Sugar': False}
url = 'http://httpbin.org/get'
resp = requests.get(url, params=payload)
printResponse(resp)
# Response Code: +----- 200 -----+
#
#
# Headers: +----------------------+
# {'Date': 'Wed, 11 Mar 2020 18:13:37 GMT', 'Content-Type': 'application/json', 'Content-Length': '410', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
#
#
# Returned data: +----------------------+
# {
#   "args": {
#     "Cream": "True",
#     "Size": "Large",
#     "Sugar": "False"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.23.0",
#     "X-Amzn-Trace-Id": "Root=1-5e692a51-71b500ab1d13d674526bc5d0"
#   },
#   "origin": "192.168.10.1",
#   "url": "http://httpbin.org/get?Size=Large&Cream=True&Sugar=False"
# }
#
#
# Process finished with exit code 0


# Making A POST Request
# Send some parameters to the URL via a GET request
# Requests handles this for you, no manual encoding
payload = {'Size': 'Large', 'Cream': True, 'Sugar': False}
url = 'http://httpbin.org/post'
resp = requests.post(url, data=payload)
printResponse(resp)
# Response Code: +----- 200 -----+
#
#
# Headers: +----------------------+
# {'Date': 'Wed, 11 Mar 2020 20:23:51 GMT', 'Content-Type': 'application/json', 'Content-Length': '526', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
#
#
# Returned data: +----------------------+
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "Cream": "True",
#     "Size": "Large",
#     "Sugar": "False"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "33",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.23.0",
#     "X-Amzn-Trace-Id": "Root=1-5e6948d7-4b5b42c85acf7660e4e2c1a8"
#   },
#   "json": null,
#   "origin": "10.10.10.10",
#   "url": "http://httpbin.org/post"
# }
#
#
# Process finished with exit code 0


# Sending Custom Headers
# Pass a custom header to the server
url = "http://httpbin.org/get"
customHeader = {'User-Agent': 'Gardens-Delight-App / 1.0.1'}
resp = requests.get(url, headers=customHeader)
printResponse(resp)
# Response Code: +----- 200 -----+
#
#
# Headers: +----------------------+
# {'Date': 'Wed, 11 Mar 2020 20:46:31 GMT', 'Content-Type': 'application/json', 'Content-Length': '312', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
#
#
# Returned data: +----------------------+
# {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "Gardens-Delight-App / 1.0.1",
#     "X-Amzn-Trace-Id": "Root=1-5e694e27-6ade43401b07635c60af1748"
#   },
#   "origin": "1.2.3.4",
#   "url": "http://httpbin.org/get"
# }

# Handling Errors With HTTPError
from requests.exceptions import HTTPError, Timeout

try:
    url = 'http://httpbin.org/status/404'
    resp = requests.get(url)
    resp.raise_for_status()
    printResponse(resp)
except HTTPError as error:
    print(f'Http Error: {error}')
except Timeout as error:
    print(f'Request timed out: {error}')
# Http Error: 404 Client Error: NOT FOUND for url: http://httpbin.org/status/404


# Handling A Timeout
try:
    url = 'http://httpbin.org/delay/5'
    resp = requests.get(url, timeout=3)
    resp.raise_for_status()
    printResponse(resp)
except HTTPError as error:
    print(f'Http Error: {error}')
except Timeout as error:
    print(f'Request timed out: {error}')
# Request timed out: HTTPConnectionPool(host='httpbin.org', port=80): Read timed out. (read timeout=3)

# Authentication With Requests
from requests.auth import HTTPBasicAuth

# Access a URL that requires authentication - the format of this
# URL is that you provide the username/password to auth against
url = 'https://httpbin.org/basic-auth/vegibit/secret'

# Create a credentials object using HTTPBasicAuth
credentials = HTTPBasicAuth('vegibit', 'secret')

# Issue the request with the authentication credentials
resp = requests.get(url, auth=credentials)
printResponse(resp)
# Response Code: +----- 200 -----+
#
#
# Headers: +----------------------+
# {'Date': 'Thu, 12 Mar 2020 14:36:41 GMT', 'Content-Type': 'application/json', 'Content-Length': '50', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
#
#
# Returned data: +----------------------+
# {
#   "authenticated": true,
#   "user": "vegibit"
# }