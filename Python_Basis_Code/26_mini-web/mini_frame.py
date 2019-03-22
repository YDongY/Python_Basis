import time


def login():
    return "welcome to our website .......:%s" % time.ctime()


def register():
    return "register .......:%s" % time.ctime()


def application(title):
    if title == "/login.py":
        return login()
    elif title == "/register.py":
        return register()
    else:
        return "not found"
