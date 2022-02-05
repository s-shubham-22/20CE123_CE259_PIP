# Decorator for Upper Case

def make_upper(fn):
    def wrapper(String):
        return string.upper()
    return wrapper

@make_upper
def hello(string):
    return string

string = 'I Love Web Development'
print(hello(string))