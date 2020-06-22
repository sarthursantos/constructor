
var botaoADD = document.querySelector("#btn-add");

botaoADD.addEventListener("click", function(){

    var xhr = new XMLHttpRequest();

    var url = "http://localhost:5000/api/users";
    xhr.open("GET", url);

    xhr.withCredentials = true;

    var erroAjax = document.querySelector("#erro");
    if (xhr.status == 200){
        erroAjax.classList.add("invisivel");
        
        xhr.addEventListener("load", function(){
            var users = JSON.parse(xhr.responseText);
            console.log(users);
        });

    }else{
        erroAjax.classList.remove("invisivel");
        console.log(xhr.status);
        console.log(xhr.responseText);
    }

    xhr.send();
});