document.querySelector("#menu").addEventListener("click",function(event){
        
    if (event.target.matches('img')){
        let parent = event.target.parentNode.parentNode.getElementsByClassName('header-nav')[0];    
    }else{
        let parent = event.target.parentNode.getElementsByClassName('header-nav')[0];
    }
    
    if (parent.classList.contains('dpdw-open')){
        parent.classList.remove('dpdw-open');
    }else{
        parent.classList.add('dpdw-open');
    };

    let menu_dorpdown = document.querySelector('#menu').getElementsByClassName('header-nav');
    for (let j=0; j < menu_dorpdown.length; j++){
        if (menu_dorpdown[j] != parent){
            menu_dorpdown[j].classList.remove('dpdw-open');
        }
    }
});

window.onclick = function(event) {
if (!event.target.matches('.content-menu-button') && !event.target.matches('img')) {
    let dropdowns = document.getElementsByClassName("header-nav");
    for (let i = 0; i < dropdowns.length; i++) {
        let openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('dpdw-open')) {
            openDropdown.classList.remove('dpdw-open');
        }
    }
}
}