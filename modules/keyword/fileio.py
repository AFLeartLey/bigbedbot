import json
from pathlib import Path

preserved_path = Path(__file__,"..","..","..","data","preserved.json").resolve();

def get():
    return json.loads(preserved_path.read_text(encoding="utf-8"))

def add(inp: str):
    targ = get()
    targ.append(inp)
    preserved_path.write_text(json.dumps(targ),encoding="utf-8")