window.onload = function() {
    // Cria o título
    var titulo = document.createElement("h1");
    titulo.id = "titulo";
    titulo.textContent = "Bem-vindo ao meu site!";
    document.body.appendChild(titulo);

    // Cria o elemento do produto
    var produto = document.createElement("div");

    // Cria e adiciona o nome do produto
    var nomeProduto = document.createElement("h2");
    nomeProduto.textContent = "Pizza de Atum";
    produto.appendChild(nomeProduto);

    // Cria e adiciona a descrição do produto
    var descricaoProduto = document.createElement("p");
    descricaoProduto.textContent = "A Pizza de Atum é uma deliciosa opção para uma refeição leve e saborosa. A receita básica inclui uma base de pizza, ketchup, atum em lata, cebola picada, tomates cereja, azeitonas verdes, queijo mozzarella ralado e orégano seco";
    produto.appendChild(descricaoProduto);

    // Cria e adiciona o preço do produto
    var precoProduto = document.createElement("p");
    precoProduto.textContent = "R$30,00";
    produto.appendChild(precoProduto);

    // Adiciona o produto ao corpo do documento
    document.body.appendChild(produto);
}
