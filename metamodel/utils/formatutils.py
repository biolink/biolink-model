def camelcase(txt: str) -> str:
    # TODO: fix so microRNA -> MicroRNA
    return txt.title().replace(" ", "").replace(",", "")


def underscore(txt: str) -> str:
    return txt.replace(" ", "_").replace(",", "")


def lcamelcase(txt: str) -> str:
    s = txt.title().replace(" ", "").replace(",", "")
    return s[0].lower() + s[1:]


def be(entry: object) -> str:
    return str(entry) if entry else ''
