class User(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        pass


if __name__ == '__main__':
    user = User()
    print(user)
    user2 = User()
    print(user2)

