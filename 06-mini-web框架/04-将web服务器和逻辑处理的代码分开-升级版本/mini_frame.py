import time


def login():
    return "----Login----Welcome to our website......time: %s" % time.ctime()


def register():
    return "----Register----Welcome to our website......time: %s" % time.ctime()


def profile():
    return "----Profile----Welcome to our website......time: %s" % time.ctime()


def application(file_name):
    if file_name == "/login.py":
        return login()
    elif file_name == "/register.py":
        return register()
    elif file_name == "/profile.py":
        return profile()
    else:
        return "404 Not Found!"
