import time

def getCurrentTimeInEpochSeconds():
    return int(time.time())

def getUniqueFileName(fileName: str):
    return f"{fileName}-{getCurrentTimeInEpochSeconds()}.png"