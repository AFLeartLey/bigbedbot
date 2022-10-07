import json
from pathlib import Path

bc_pth = Path(__file__, "..", "..","..", "data", "bc_data.json").resolve()


def get():
    memberinfo: dict[int,int] = json.loads(bc_pth.read_text(encoding="utf-8"))
    return memberinfo

def getid(targ: int):
    memberinfo: dict[int,int] = get()
    retval = 0
    try:
        retval = memberinfo[targ]
    except(KeyError):
        return -1
    return retval

"""
fileio
return 2 on Keyerror
"""
def write(member: int,diff: int):
    allst = get()
    try:
        allst[member] = allst[member] + diff
    except(KeyError):
        return 2
    bc_pth.write_text(json.dumps(allst),encoding="utf-8")
