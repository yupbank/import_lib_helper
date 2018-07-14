from scoped_importlib import scoped_importlib

def main():
    with scoped_importlib('a') as a:
        print a.NAME
    with scoped_importlib('b') as b:
        print b.NAME

if __name__ == "__main__":
    main()
