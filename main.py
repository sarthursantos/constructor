from json import Json


# ----------------------------------------------------------------
# As funções a seguir são utilizadas para extrair os dados do JSON
# ----------------------------------------------------------------
def get_title(json):
    return json['title']


def get_header(json):
    # Header
    header = json['header']
    # Logo
    header_logo_link = header['logo_link']
    header_logo_img = header['logo_img']
    header_logo = [header_logo_link, header_logo_img]
    # Menu
    header_menu_btn = header['menu']
    header_menu_btn_drop = header['btn_drop_down']
    header_menu_btn_img = header['btn_img']
    header_menu = [header_menu_btn, header_menu_btn_drop, header_menu_btn_img]
    return header_logo, header_menu


def get_footer(json):
    pass


def get_content(json):
    pass


# ------------------------------------------------------------------------------------------
# As funções a seguir são utilizadas para montar o HTML a partir dos dados extraidos do JSON
# ------------------------------------------------------------------------------------------
def _logo(link, img):
    return f'''
        <a class="header-logo" href="{link}">
            <img class="header-logo" src="{img}">
        </a>
    '''


def _menu(btn, btn_drop, btn_img):
    menu = '<nav id="menu" class="headerDesktop-content-menu">'
    for i in range(len(btn)):
       menu += _menu_section(btn[i], str(i), btn_drop, btn_img)
    menu += '</nav>'
    return menu


def _menu_section(name, str_btn_position, btn_drop, btn_img):
    section = '<div class="content-menu-section">'
    section += _section_btn(name, str_btn_position, btn_img)
    resp_drop = _btn_drop(str_btn_position, btn_drop)
    if resp_drop:
        section = section.replace("content-menu-section", "content-menu-section drop")
        section += resp_drop
    section += '</div>'
    return section


def _section_btn(name, str_position, btn_img):
    section = f'<a href="#" class="content-menu-button">'
    if str_position in btn_img:
        section += f'<img id="img-profile" src="{btn_img[str_position]}" class="headline-profile-avatar">'
    section += f'{name}</a>'
    return section


def _btn_drop(str_i, btn_drop):
    btn = ''
    if str_i in btn_drop:
        btn += '<nav class="header-nav">'
        for j in btn_drop[str_i]:
            btn += f'<a class="header-nav-link">{j}</a>'
        btn += '</nav>'
    return btn if btn != '' else None


def _btn_secondary():
    pass


# -----------------------------------
# Ainda falta limpar daqui para baixo
# -----------------------------------
def make_header(logo, menu):
    return f'''
        <header class="header header-desktop">
            <div class="container">
                {_logo(logo[0], logo[1])}
                {_menu(menu[0], menu[1], menu[2])}
            </div>
        </header>
    '''


def make_body(header):
    return f'''
        <body>
        {header}
        <section class="banner">
          <div class="container">
             <h1 id="banner-title" class="banner-title">CONJUNTO DE DADOS</h1>
         </div>
        </section>
        <p>FOOTER</p>
        <script src="js/menu.js"></script>
        </body>
    '''


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


def make_html(head, body):
    html = f'''\
<!DOCTYPE html>
<html lang="pt-br">
    {head}
    {body}           
</html>
    '''
    with open("index.html", "w", encoding='UTF-8') as file:
        file.writelines(html)
    return html


if __name__ == '__main__':
    title = get_title(Json)
    logo, menu = get_header(Json)
    head = make_head(title)
    body = make_body(make_header(logo, menu))
    make_html(head, body)
