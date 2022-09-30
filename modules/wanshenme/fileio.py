import json
from pathlib import Path

wanshenme_pth = Path(__file__,"..", "..","..","data","wanshenme.json").resolve()

def get():
    wsm_list = json.loads(wanshenme_pth.read_text(encoding="utf-8"))
    return wsm_list

def write(newitem: str):
    wsm_list = get()
    if newitem in wsm_list:
        return 1
    elif newitem == "":
        return 2
    wsm_list.append(newitem)
    wanshenme_pth.write_text(json.dumps(wsm_list),encoding="utf-8")
    return 0
