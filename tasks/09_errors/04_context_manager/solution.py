class Resource:
    def __enter__(self):
        print("Open")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("Closed")
        return False


with Resource():
    print("Using resource")
