def announce(f):
    def wrapper():
        print("ABout to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("hello, World!")

hello()