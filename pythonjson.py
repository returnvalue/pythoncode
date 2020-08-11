# json.loads() Parse Example
import json

jsonstring = '''{
        "burrito" : "Steak",
        "double-meat" : true,
        "toppings" : [
            "Black Beans",
            "Lettuce",
            "Salsa",
            "Guacamole"
        ],
        "price" : 9.17
    }'''

data = json.loads(jsonstring)

print('Order: ' + data['burrito'])
if (data['double-meat']):
    print('With Double Meat')
for topping in data['toppings']:
    print('Topping: ' + topping)
# Order: Steak
# With Double Meat
# Topping: Black Beans
# Topping: Lettuce
# Topping: Salsa
# Topping: Guacamole

# json.dumps() Serialize Example
pythondict = {
    'burrito': 'Steak',
    'double-meat': True,
    'toppings': ['Black Beans',
                 'Lettuce',
                 'Salsa',
                 'Guacamole'
                 ],
    'price': 9.17
}

jsonstring = json.dumps(pythondict, indent=4)

print('-------- JSON String Data --------')
print(jsonstring)
# -------- JSON String Data --------
# {
#     "burrito": "Steak",
#     "double-meat": true,
#     "toppings": [
#         "Black Beans",
#         "Lettuce",
#         "Salsa",
#         "Guacamole"
#     ],
#     "price": 9.17
# }


# Handling JSON errors with JSONDecodeError
from json import JSONDecodeError

jsonstring = '''{
        "burrito" : "Steak",
        "double-meat" : true,
        "toppings" : [
            "Black Beans",
            "Lettuce"
            "Salsa",
            "Guacamole"
        ],
        "price" : 9.17
    }'''

try:
    data = json.loads(jsonstring)

    print('Order: ' + data['burrito'])
    if (data['double-meat']):
        print('With Double Meat')
    for topping in data['toppings']:
        print('Topping: ' + topping)

except JSONDecodeError as error:
    print('Hold on now, there was a JSON Decoding erroror:')
    print(error.msg)
    print(error.lineno, error.colno)
# Hold on now, there was a JSON Decoding erroror:
# Expecting ',' delimiter
# 7 13

jsonstring = '''{
        "burrito" : "Steak",
        "double-meat" : true,
        "toppings" : [
            "Black Beans",
            "Lettuce",
            "Salsa",
            "Guacamole
        ],
        "price" : 9.17
    }'''

try:
    data = json.loads(jsonstring)

    print('Order: ' + data['burrito'])
    if (data['double-meat']):
        print('With Double Meat')
    for topping in data['toppings']:
        print('Topping: ' + topping)

except JSONDecodeError as error:
    print('Hold on now, there was a JSON Decoding erroror:')
    print(error.msg)
    print(error.lineno, error.colno)
# Hold on now, there was a JSON Decoding erroror:
# Invalid control character at
# 8 23


# Working With JSON from an API
import json, requests

url = 'http://httpbin.org/json'
result = requests.get(url)

pythondict = result.json()

print(json.dumps(pythondict, indent=4))

print(list(pythondict.keys()))

print(pythondict['slideshow']['title'])
slides = len(pythondict['slideshow']['slides'])
print(f'There are {slides} slides')
# {
#     "slideshow": {
#         "author": "Yours Truly",
#         "date": "date of publication",
#         "slides": [
#             {
#                 "title": "Wake up to WonderWidgets!",
#                 "type": "all"
#             },
#             {
#                 "items": [
#                     "Why <em>WonderWidgets</em> are great",
#                     "Who <em>buys</em> WonderWidgets"
#                 ],
#                 "title": "Overview",
#                 "type": "all"
#             }
#         ],
#         "title": "Sample Slide Show"
#     }
# }
# ['slideshow']
# Sample Slide Show
# There are 2 slides