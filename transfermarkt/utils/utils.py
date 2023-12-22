import re
def getNumberAllNumsFromStr(s: str) -> int:
    t = re.findall(r"\d+", s)
    return int(''.join(t))