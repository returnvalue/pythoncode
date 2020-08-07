# Set Url and Fetch Data
import urllib.request

# specify the URL to get data from
url = 'http://httpbin.org/xml'

# open the URL and fetch some data
result = urllib.request.urlopen(url)

# Checking Http Response Code
# Print the resulting http status code
print('Result code: {0}'.format(result.status))
# Result code: 200

# Http Response Headers
# print the response data headers
print('Headers: ---------------------')
print(result.getheaders())
# [('Date', 'Thu, 06 Aug 2020 14:31:27 GMT'), ('Content-Type', 'application/xml'), ('Content-Length', '522'),
# ('Connection', 'close'), ('Server', 'gunicorn/19.9.0'), ('Access-Control-Allow-Origin', '*'),
# ('Access-Control-Allow-Credentials', 'true')]

# Reading Response Data
# print the actual response data
print('Returned data: ---------------------')
print(result.read().decode('utf-8'))
# Returned data: ---------------------
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

# GET and POST with urllib
# set up Url for the request
url = 'http://httpbin.org/get'

result = urllib.request.urlopen(url)

print('Result code: {0}'.format(result.status))
print('Returned data: ----------------------')
print(result.read().decode('utf-8'))
# Result code: 200
# Returned data: ----------------------
# {
#   "args": {},
#   "headers": {
#     "Accept-Encoding": "identity",
#     "Host": "httpbin.org",
#     "User-Agent": "Python-urllib/3.8",
#     "X-Amzn-Trace-Id": "Root=1-5f2c14b8-bcfc01b09834e542d43b0e1a"
#   },
#   "origin": "151.203.10.206",
#   "url": "http://httpbin.org/get"
# }

# Creating an args payload
import urllib.parse

# set up Url for the request
url = 'http://httpbin.org/get'

# define sample data to pass to the GET request
args = {
    'color': 'Blue',
    'shape': 'Circle',
    'is_active': True
}

# url-encoded data before passing as arguments
data = urllib.parse.urlencode(args)

# issue the request with the data params as part of the URL
result = urllib.request.urlopen(url + '?' + data)

print('Result code: {0}'.format(result.status))
print('Returned data: ----------------------')
print(result.read().decode('utf-8'))
# Result code: 200
# Returned data: ----------------------
# {
#   "args": {
#     "color": "Blue",
#     "is_active": "True",
#     "shape": "Circle"
#   },
#   "headers": {
#     "Accept-Encoding": "identity",
#     "Host": "httpbin.org",
#     "User-Agent": "Python-urllib/3.8",
#     "X-Amzn-Trace-Id": "Root=1-5f2c14f4-6ca91950eadef770ca1ae888"
#   },
#   "origin": "151.203.10.206",
#   "url": "http://httpbin.org/get?color=Blue&shape=Circle&is_active=True"
# }

# Making POST Request
# issue the request with a data parameter to use POST
url = 'http://httpbin.org/post'

# define sample data to pass to the GET request
args = {
    'color': 'Blue',
    'shape': 'Circle',
    'is_active': True
}

# url-encoded data before passing as arguments
data = urllib.parse.urlencode(args)

data = data.encode()
result = urllib.request.urlopen(url, data=data)

print('Result code: {0}'.format(result.status))
print('Returned data: ----------------------')
print(result.read().decode('utf-8'))
# Result code: 200
# Returned data: ----------------------
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "color": "Blue",
#     "is_active": "True",
#     "shape": "Circle"
#   },
#   "headers": {
#     "Accept-Encoding": "identity",
#     "Content-Length": "38",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "Python-urllib/3.8",
#     "X-Amzn-Trace-Id": "Root=1-5e6683a5-777d0378401b31982e213810"
#   },
#   "json": null,
#   "origin": "127.0.0.1",
#   "url": "http://httpbin.org/post"
# }

# Errors With urllib
from urllib.error import HTTPError, URLError
from http import HTTPStatus

url = 'http://httpbin.org/html'

# wrap the web request in a try catch block
try:
    result = urllib.request.urlopen(url)
    print('Result code: {0}'.format(result.status))
    if (result.getcode() == HTTPStatus.OK):
        print(result.read().decode('utf-8'))

# happens on a non-success error code
except HTTPError as err:
    print('There was an HTTP Error with code: {0}'.format(err.code))

# happens when there is something wrong with the URL itself
except URLError as err:
    print('There has been a catastrophic failure. {0}'.format(err.reason))
# no errors on the above code

# code below has errors
url = 'http://i-dont-exist.org/'

# wrap the web request in a try catch block
try:
    result = urllib.request.urlopen(url)
    print('Result code: {0}'.format(result.status))
    if (result.getcode() == HTTPStatus.OK):
        print(result.read().decode('utf-8'))

# happens on a non-success error code
except HTTPError as err:
    print('There was an HTTP Error with code: {0}'.format(err.code))

# happens when there is something wrong with the URL itself
except URLError as err:
    print('There has been a catastrophic failure. {0}'.format(err.reason))

# check for 404 status codes
from http import HTTPStatus

url = 'http://httpbin.org/status/404'

# wrap the web request in a try catch block
try:
    result = urllib.request.urlopen(url)
    print('Result code: {0}'.format(result.status))
    if (result.getcode() == HTTPStatus.OK):
        print(result.read().decode('utf-8'))

# happens on a non-success error code
except HTTPError as err:
    print('There was an HTTP Error with code: {0}'.format(err.code))

# happens when there is something wrong with the URL itself
except URLError as err:
    print('There has been a catastrophic failure. {0}'.format(err.reason))
# There was an HTTP Error with code: 404