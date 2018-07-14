import importlib


def main():
    a = importlib.import_module('a')
    print a.NAME
    b = importlib.import_module('b')
    print b.NAME

if __name__ == "__main__":
    main()
