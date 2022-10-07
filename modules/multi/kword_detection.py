from modules.keyword import fileio as kwio

def lengthdetect(*inputval: str):
    for i in inputval:
        if(len(i) > 50):
            return 1
    return 0

def keywordDetection(*inputval: str):
    keywordlist = kwio.get()
    for i in inputval:
        for j in keywordlist:
            if j in i:
                return 1
    return 0