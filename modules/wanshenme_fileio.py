
def getlist():
    fio = open("./data/wanshenme.txt","r",encoding='utf-8')
    ret:list[str] = ""
    ret = fio.readlines()
    fio.close()
    return ret

def add_wanshenme(option: str):
    fio = open("./data/wanshenme.txt","a",encoding='utf-8')
    fio.write((option+'\n'))
    fio.close()