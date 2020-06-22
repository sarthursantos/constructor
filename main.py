from json_header import get_header, get_drop_down


def make_head(title):
    return f'''\
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/fonts.css">
    <link rel="stylesheet" href="css/nav.css">
    <link rel="stylesheet" href="css/index.css">
    <link rel="stylesheet" href="css/banner.css">

    <title>{title}</title>
</head>\
    '''


def make_header(hd, drop):
    header = f'''
    <header class="header header-desktop">
        <div class="container">
            <a class="header-logo" href="{hd[0]}">
                <img class="header-logo" src="{hd[1]}">
            </a>
            <nav id="menu" class="headerDesktop-content-menu">
'''
    for i in range(len(hd[2])):
        header += '<div class="content-menu-section'
        qq = test(str(i), drop)
        header += f''' {qq if qq == '' else 'drop'}">
            <a href="#" class="content-menu-button">{hd[2][i]}</a>\
        '''
        header += qq + '\n</div>'

    header += f'''
            </nav>
        </div>
    </header>\
'''
    return header


def make_footer(footer):
    return footer


def make_body(header, footer):
    return f'''
<body>
    {header}
    <section class="banner">
      <div class="container">
         <h1 id="banner-title" class="banner-title">CONJUNTO DE DADOS</h1>
     </div>
    </section>
{footer}
    <script src="js/menu.js"></script>
</body>
    '''


def make_html(head, body):
    html = f'''\
<!DOCTYPE html>
<html lang="pt-br">
    {head}
    {body}           
</html>
    '''

    with open("test.html", "w", encoding='UTF-8') as file:
        file.writelines(html)
    return html


def test(str_i, drop):
    var = ''
    if str_i in drop:
        var += '<nav class="header-nav">'
        for j in drop[str_i]:
            var += f'<a class="header-nav-link">{j}</a>'
        var += '</nav>'
    return var


if __name__ == '__main__':
    head = make_head(json['title'])
    header = make_header(
        get_header(),
        get_drop_down()
    )

    footer = "Aqui FOOTER"
    body = make_body(
        header,
        footer
    )
    make_html(head, body)
