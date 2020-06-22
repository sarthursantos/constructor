from main import *
from html import *

json = {
    'title': 'PASSO_1',
    'header': {
        'logo_img': 'img/logo-alura.svg',
        'logo_link': '#',
        'menu': ['Home', 'GeoPortal', 'Tipo', 'User']
    },
    'drop_down': {
        '2': ['Embarcações', 'Boias e Fundeios', 'Derivadores'],
        '3': ['Perfil', 'Cadastro']
    },
    'footer': 'gg'
}


def json_interp(json):
    title = json['title']


def get_header():
    logo_link = json['header']['logo_link']
    logo_img = json['header']['logo_img']
    menu = json['header']['menu']
    return logo_link, logo_img, menu


def get_drop_down():
    return json['drop_down']


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


if __name__ == '__main__':
    variavel = json_2_obj(json)
    #print(json)
    print(variavel.footer)