window.onload = function() {
    // Capturando os elementos
    var titulo = document.getElementById('titulo');
    var ul = document.getElementsByTagName('ul')[0];
    var a = document.getElementsByTagName('a')[0];
    var ol = document.getElementById('lista-ordenada');

    // Adicionando conteúdo textual
    titulo.innerText = "Título do Projeto";
    a.innerText = "Proze Educação";

    // Adicionando itens à lista não ordenada
    ul.innerHTML = "<li>Item 1</li><li>Item 2</li><li>Item 3</li>";

    // Adicionando itens com links à lista ordenada
    ol.innerHTML = '<li><a href="https://www.google.com">Google</a></li>' +
                   '<li><a href="https://www.bing.com">Bing</a></li>' +
                   '<li><a href="https://www.duckduckgo.com">DuckDuckGo</a></li>';
}
