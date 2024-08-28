class InvalidOptionIndexException(Exception):
    def __init__(self, message = "Invalid option index."):
        super().__init__(message)
