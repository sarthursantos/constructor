

# -------------------------------------
# Esta Class será utilizada futuramente
# -------------------------------------
class HtmlAtr:
    def __init__(self, title, header, footer):
        self.title = title
        self.header = header
        self.footer = footer


def json_2_obj(json):
    title = json["title"]
    header = json["header"]
    footer = json["footer"]
    drop_down = json["drop_down"]
    return HtmlAtr(title, [header, drop_down], footer)

