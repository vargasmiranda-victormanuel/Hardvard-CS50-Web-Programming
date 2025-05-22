#takes a function as an input and return a modified function as an output
#functional programming paradigme
def announce(f):
    def wrapper():
        print("about to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("hello")


hello()