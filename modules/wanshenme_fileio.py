
def getlist():
    fio = open("./data/wanshenme.txt","r")
    ret:list[str] = ""
    ret = fio.readlines()
    fio.close()
    return ret

def add_wanshenme(option: str):
    fio = open("./data/wanshenme.txt","a")
    fio.write((option+'\n'))
    fio.close()