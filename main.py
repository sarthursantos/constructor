from json import Json


def _head(title):
    return f'''\
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/fonts.css">
    <link rel="stylesheet" href="css/grades.css">
    <link rel="stylesheet" href="css/header.css">
    <link rel="stylesheet" href="css/banner.css">
    <link rel="stylesheet" href="css/form.css">
    <link rel="stylesheet" href="css/btn.css">
    <link rel="stylesheet" href="css/table.css">
    <link rel="stylesheet" href="css/footer.css">

    <title>{title}</title>
</head>\
    '''


def _logo(logo):
    a = '<a class="header-logo"'
    a += f''' onclick="{logo['onclick']}"''' if 'onclick' in logo and logo['onclick'] else '>'
    a += f'''<img class="header-logo" src="{logo["img"]}"></a>'''
    return a


def _menu(menu):
    nav = '<nav id="menu" class="header-content-menu">'
    for btn in menu:
       nav += _btn(btn)
    nav += '</nav>'
    return nav


def _btn(btn):
    div = '<div class="content-menu-section'
    nav = ''
    if 'drop' in btn and btn['drop']:
        div += ' drop">'
        nav = _btn_drop(btn['drop'])
    else:
        div += '">'

    a = '<a class="content-menu-button"'
    var = []
    if 'url' in btn:
        var.append(btn['url'])
        if 'banner' in btn:
            var.append(btn['banner'])
        a += f''' onclick="get_data('{"','".join(var)}')">'''
    else:
        a += '>'
    # a += f''' onclick="get_data('{btn['url']}')">''' if 'url' in btn and btn['url'] else '>'
    a += f'''<img src={btn['img']} class="headline-profile-avatar">''' if 'img' in btn and btn['img'] else ''
    a += f'''{btn['btn']}</a>'''
    div += a

    div += nav
    div += '</div>'
    return div


def _btn_drop(btn_drop):
    nav = '<nav class="header-nav header-nav-profile" tabindex="-1">'
    for btn in btn_drop:
        var = []
        if 'url' in btn:
            var.append(btn['url'])
            if 'banner' in btn:
                var.append(btn['banner'])

        if 'btn_sec' in btn and btn['btn_sec']:
            nav += '<nav class="header-nav-subLinks">'
            nav += '<a class="header-subLinks-firstLink" tabindex="-1"'

            nav += f''' onclick="get_data('{"','".join(var)}')">'''

            nav += btn['btn']
            nav += '</a>'
            nav += '<a class="header-subLinks-secondLink" tabindex="-1"'
            nav += f''' onclick="{btn['onclick_sec']}">''' if 'onclick_sec' in btn and btn['onclick_sec'] else '>'
            nav += btn['btn_sec']
            nav += '</a>'
            nav += '</nav>'
        else:
            nav += f'''<a class="header-nav-link" tabindex="-1"'''

            nav += f''' onclick="get_data('{"','".join(var)}')">'''
            # nav += f''' onclick="{btn['onclick']}">''' if 'onclick' in btn_drop and btn['onclick'] else '>'

            nav += f'''{btn['btn']}</a>'''
    nav += '</nav>'
    return nav


def _header(logo, menu):
    return f'''
        <header class="header header-desktop">
            <div class="container">
                {logo}
                {menu}
            </div>
        </header>
    '''


def _body(header):
    return f'''
        <body>
        {header}
        <div class="banner">
            <div class="container">
                <h1 id="banner-title">{Json['banner']['title']}</h1>
            </div>
        </div>
        <div>
            <div id="content" class="container">
            </div>
        </div>
        <div>
            <div id="footer" class="container">
            </div>
        </div>
        <script src="js/menu.js"></script>
        <script src="src/index.js"></script>
        </body>
    '''


def _html(head, body):
    html = f'''\
<!DOCTYPE html>
<html lang="pt-br">
    {head}
    {body}           
</html>
    '''
    with open("index.html", "w", encoding='UTF-8') as file:
        file.writelines(html)


if __name__ == '__main__':
    head = _head(Json['title'])
    logo = _logo(Json['header']['logo'])
    menu = _menu(Json['header']['menu'])
    header = _header(logo, menu)
    body = _body(header)
    _html(head, body)
