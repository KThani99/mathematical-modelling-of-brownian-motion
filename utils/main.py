import uuid

def getUniqueId():
    return uuid.uuid4()

def getUniqueFileName(fileName: str):
    return f"{fileName}-{getUniqueId()}.png"