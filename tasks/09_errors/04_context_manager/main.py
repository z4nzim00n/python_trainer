class Resource:
    def __enter__(self):
        # TODO: напечатай Open и верни self
        return self

    def __exit__(self, exc_type, exc, tb):
        # TODO: напечатай Closed
        return False


with Resource():
    print("Using resource")
