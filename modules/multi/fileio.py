from asyncio.windows_events import NULL
import json
from pathlib import Path

sentence_pth = Path(__file__, "..", "..","..", "data", "multi_sentence.json").resolve()
def get():
    sentences: dict[str,list[str]] = json.loads(sentence_pth.read_text(encoding="utf-8"))
    return sentences

def getsp(targ:str):
    allst:dict[str,list[str]] = get()
    try:
        return allst[targ]
    except(KeyError):
        return []

def write(inp: str,to:str):
    sentences: dict[str,list[str]] = json.loads(sentence_pth.read_text(encoding="utf-8"))
    try:
        if(inp in sentences[to]):
            return 1
        sentences[to].append(inp)
    except(KeyError):
        sentences[to] = [inp]
    sentence_pth.write_text(json.dumps(sentences),encoding="utf-8")
    return 0
