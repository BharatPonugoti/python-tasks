#Secure Login System (Decorators)#
def login_required(func):
    def wrapper(logged_in):
        if logged_in:
            func(logged_in)
        else:
            print("Access Denied")
    return wrapper

@login_required
def dashboard(logged_in):
    print("Welcome to Dashboard")

dashboard(True)
dashboard(False)