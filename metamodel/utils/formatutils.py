from typing import List


def camelcase(txt: str) -> str:
    def _up(s: str):
        return s[0].upper() + (s[1:] if len(s) > 1 else '')

    return ''.join([_up(word) for word in txt.split()])


def underscore(txt: str) -> str:
    return txt.replace(" ", "_").replace(",", "")


def lcamelcase(txt: str) -> str:
    s = camelcase(txt.replace('_', ' '))
    return s[0].lower() + s[1:]


def be(entry: object) -> str:
    return str(entry).strip() if entry else ''


split_col = 115


def split_line(txt: str, split_len: int=split_col) -> List[str]:
    # TODO: consider replacing by textwrap.fill function, but note that its behavior is a bit different
    out_lines = []
    words = txt.split()
    cur_line = ""
    for word in words:
        word += ' '
        if len(cur_line) + len(word) > split_len:
            out_lines.append(cur_line if cur_line else word)
            if not cur_line:
                word = ""
            else:
                cur_line = ""
        cur_line += word
    if cur_line:
        out_lines.append(cur_line)
    return out_lines


def wrapped_annotation(txt: str) -> str:
    rval = []
    for line in [l.strip() for l in txt.split('\n')]:
        if len(line) > split_col:
            rval += split_line(line)
        else:
            rval.append(line)
    return '\n\t'.join(rval)
