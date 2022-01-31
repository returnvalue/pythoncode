def my_decorator(func):
    '''Decorator Function'''

    def wrapper():
        '''Wrapper Function'''
        result = func()
        return result.title().replace(' ', ' !##! ')

    return wrapper


@my_decorator
def to_be_decorated():
    return 'output to decorate'


result = to_be_decorated()
print(result)