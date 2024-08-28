class InvalidOptionIdException(Exception):
    def __init__(self, message="Invalid option id."):
        super().__init__(message)
