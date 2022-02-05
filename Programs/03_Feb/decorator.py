def make_bold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"
    return wrapper

def make_italic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"
    return wrapper

def make_underline(fn):
    def wrapper():
        return "<u>" + fn() + "</u>"
    return wrapper

# @make_bold
# @make_italic
# @make_underline

# def hello():
#     return "hello world"

def hello():
    @make_bold
    @make_italic
    @make_underline
    def hello_world():
        return "hello world"
    return hello_world()

print(hello())
     