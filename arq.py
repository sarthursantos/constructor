

def test(str_i, drop):
    var = None
    if str_i in drop:
        for j in drop[str_i]:
            var += f'<a class="header-nav-link">{j}</a>'
    return var


qq = test()

header += f''' {qq if qq else ''}">
    <a href="#" class="content-menu-button">{hd[2][i]}</a>
    <nav class="header-nav"> \
'''

header += qq


header += f'''
                </nav>
            </div>
'''







def make_header(hd, drop):
    print(hd, drop)
    header = f'''
    <header class="header header-desktop">
        <div class="container">
            <a class="header-logo" href="{hd[0]}">
                <img class="header-logo" src="{hd[1]}">
            </a>
            <nav id="menu" class="headerDesktop-content-menu">
'''
    for i in range(len(hd[2])):
        header += f'''\
             <div class="content-menu-section\
'''
        if str(i) in drop:
            header += f''' drop">
                <a href="#" class="content-menu-button">{hd[2][i]}</a>
                <nav class="header-nav"> \
            '''
            for j in drop[str(i)]:
                header += f'''
                    <a class="header-nav-link">{j}</a>\
                '''
            header += f'''
                </nav>
            </div>
'''
        else:
            header += f'''">
                   <a href="#" class="content-menu-button">{hd[2][i]}</a>
             </div>
'''
    header += f'''\
            </nav>
        </div>
    </header>\
'''
    return header
