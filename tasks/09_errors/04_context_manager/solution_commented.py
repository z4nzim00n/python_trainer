class Resource:
    def __enter__(self):
        # Выполняется при входе в with.
        print("Open")
        return self

    def __exit__(self, exc_type, exc, tb):
        # Выполняется при выходе, даже если было исключение.
        print("Closed")
        return False


with Resource():
    print("Using resource")
