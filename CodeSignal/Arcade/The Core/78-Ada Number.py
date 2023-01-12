def strip_sh(s: str) -> str:
    res = ""
    for c in s:
        if c != '_':
            res += c
    return res


def solution(line: str) -> bool:
    line = strip_sh(line)
    if not line:
        return False
    po = line.count('#')
    if po == 0:
        for c in line:
            if c != '_' and not c.isdigit():
                return False
        return True
    if po != 2:
        return False
    if line[-1] != '#':
        return False
    if line[1] != '#' and line[2] != '#':
        return False
    pos = line.find('#')
    if pos + 1 == len(line) - 1:
        return False
    base_str = line[:pos]
    if base_str[0] == '0':
        return False
    if line[pos + 1] == '0' and len(line) - pos - 2 != 1:
        return False
    for c in base_str:
        if not c.isdigit():
            return False
    base = int(base_str)
    if base < 2 or base > 16:
        return False
    for i in range(pos + 1, len(line) - 1):
        if line[i] == '_':
            continue
        if line[i].isdigit():
            if int(line[i]) >= base:
                return False
            continue
        if not line[i].isalpha():
            return False
        c = line[i].lower()
        if ord(c) - ord('a') + 10 >= base:
            return False
    return True


def solution(line):
    line = line.replace('_', '')
    if line.isdigit():
        return True
    try:
        b, n = line.split('#')[:-1]
        if int(b) < 2 or int(b) > 16:
            return False
        try:
            int(n, int(b))
            return True
        except ValueError:
            return False
    except ValueError:
        return False


def solution(line):
    line = line.replace("_", "")
    if "#" not in line:
        try:
            int(line)
        except:
            return False
    else:
        try:
            n = int(line[line.find("#") + 1:line.rfind("#")],
                    int(line[:line.find("#")]))
            if int(line[:line.find("#")]) > 16 or int(line[:line.find("#")]) < 2:
                return False
        except:
            return False
    return True
