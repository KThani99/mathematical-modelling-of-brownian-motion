import uuid

def getUniqueId():
    """
    Generate a random UUID (Universally Unique Identifier).

    This function creates a random UUID using version 4 of the UUID
    specification.

    Returns:
        UUID: A new random UUID.
    """

    return uuid.uuid4()

def getUniqueFileName(fileName: str):
    """
    Generate a unique filename by appending a UUID to the base filename.

    Parameters:
        fileName (str): 
            The base filename to make unique.

    Returns:
        str: A new filename string in the format "fileName-uuid.png"
    """

    return f"{fileName}-{getUniqueId()}.png"