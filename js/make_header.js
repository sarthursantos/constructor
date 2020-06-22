var title = "Passo 1"
var head = `
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/nav.css">
    <link rel="stylesheet" href="css/index.css">
    <link rel="stylesheet" href="css/banner.css">
    <link rel="stylesheet" href="css_arthur/passo_um.css">
    <title>${title}</title>
</head>
`
var html = `
<!DOCTYPE html>
<html lang="pt-br">
${head}
<body>
    <header class="header header-desktop">
        <div class="container">
            <a class="header-logo">
                LOGO
            </a>
            <nav id="menu" class="headerDesktop-content-menu"> 
                <div class="content-menu-section">
                    <a class="content-menu-button">Home </a>
                </div>      
                <div class="content-menu-section">
                    <a class="content-menu-button">GEOPORTAL</a>
                </div>
                <div class="content-menu-section">
                    <a class="content-menu-button">CONJUNTO DE DADOS</a>
                </div> 
                <div class="content-menu-section">
                    <a class="content-menu-button">proJETOS</a>
                </div> 
                <div class="content-menu-section drop">
                    <a class="content-menu-button">Tipo</a>
                    <nav class="header-nav">
                        <a class="header-nav-link">EMBARCAÇÕES</a>
                        <a class="header-nav-link">BOIAS</a>
                        <a class="header-nav-link">ESTAÇÃO</a>
                        <a class="header-nav-link">Veiculos autonômos</a>
                        <a class="header-nav-link">Informações Ceográficas</a>
                    </nav>
                </div>  
                <div class="content-menu-section drop">
                    <a href="#" class="content-menu-button">
                        <img src="img/step-hipsters.svg" class="headline-profile-avatar"> 
                        Arthur
                    </a>                
                    <nav class="header-nav">
                        <a class="header-nav-link">Perfil</a>
                        <a class="header-nav-link">Controle</a>
                        <a class="header-nav-link">Conjunto de Dados</a>
                        <a class="header-nav-link">Instituição</a>
                        <a class="header-nav-link">Projeto</a>
                        <a class="header-nav-link">Plataforma</a>
                    </nav>
                </div>
            </nav>
        </div>
    </header>
    <section class="banner">
        <div class="container">
            <h1 class="banner-title">CONJUNTO DE DADOS</h1>
        </div>
    </section>
    <br><br>
    <p>Conteúdo</p>
    <br><br>
    <footer>
        <div class="test">footer</div>
    </footer>
    <script src="js/menu.js"></script>
</body>
</html>
`

console.log(html)
