# DESCRIÇÃO DO SISTEMA — STOCKFLOW

## 1. Apresentação do sistema

O StockFlow é um sistema web de gerenciamento de estoque desenvolvido com o objetivo de facilitar a organização, o controle e a consulta de informações relacionadas aos produtos, categorias e fornecedores de uma organização.

A aplicação permite centralizar os dados do estoque em um único ambiente, proporcionando ao funcionário responsável uma maneira mais prática e organizada de administrar os registros. Por meio de uma interface intuitiva, o usuário pode realizar operações de cadastro, consulta, edição e exclusão de informações, contribuindo para a organização e o gerenciamento dos produtos armazenados.

O sistema foi desenvolvido utilizando Python e o framework Django no processamento das informações, HTML, CSS e JavaScript na construção da interface e SQLite como sistema de gerenciamento de banco de dados.

## 2. Objetivo do sistema

O principal objetivo do StockFlow é oferecer uma ferramenta que auxilie no gerenciamento das informações relacionadas ao estoque, facilitando o controle dos produtos, a organização por categorias e o gerenciamento dos fornecedores.

Além disso, busca proporcionar maior praticidade no acesso às informações, reduzir dificuldades relacionadas ao gerenciamento manual dos registros e manter os dados organizados e centralizados.

## 3. Público-alvo

O sistema é destinado principalmente a funcionários responsáveis pelo gerenciamento e controle de estoque de uma organização.

Esses usuários poderão utilizar a aplicação para administrar os produtos cadastrados, organizar suas categorias e manter as informações dos fornecedores atualizadas.

## 4. Principais funcionalidades

O StockFlow é composto por três módulos principais:

### 4.1. Gerenciamento de produtos

O módulo de produtos permite administrar os registros dos itens disponíveis no estoque.

Cada produto possui informações como nome, SKU (código identificador), descrição, preço, quantidade disponível, estoque mínimo, categoria e fornecedor associado.

O usuário poderá cadastrar novos produtos, consultar os registros existentes, editar informações e excluir produtos quando necessário.

### 4.2. Gerenciamento de categorias

O módulo de categorias permite organizar os produtos de acordo com suas classificações.

O sistema possibilita cadastrar novas categorias, consultar as categorias existentes, modificar suas informações e realizar exclusões, respeitando os relacionamentos com os produtos cadastrados.

Cada categoria possui nome e descrição, facilitando a organização e identificação dos itens.

### 4.3. Gerenciamento de fornecedores

O módulo de fornecedores permite armazenar e administrar informações dos fornecedores relacionados aos produtos cadastrados no sistema.

São registradas informações como nome, CNPJ, e-mail, telefone e endereço.

O usuário poderá cadastrar, consultar, editar e excluir fornecedores, respeitando as regras de integridade dos dados e os vínculos existentes com os produtos.

## 5. Funcionamento geral

O StockFlow apresenta uma página inicial que permite ao usuário acessar as principais áreas do sistema por meio de um menu de navegação.

A partir dessa interface, o funcionário pode acessar as páginas de produtos, categorias e fornecedores, visualizar os registros existentes e realizar as operações disponibilizadas em cada módulo.

Os dados informados nos formulários são processados pelo Django e armazenados no banco de dados SQLite. Dessa forma, as informações permanecem disponíveis para consultas e alterações posteriores.

O sistema também possui um painel administrativo disponibilizado pelo Django, que permite o gerenciamento dos registros por meio de uma interface administrativa.

## 6. Tecnologias utilizadas

Para o desenvolvimento do StockFlow, foram utilizadas as seguintes tecnologias:

- **Python:** linguagem de programação utilizada no desenvolvimento da aplicação.
- **Django:** framework responsável pelo processamento das requisições, gerenciamento das funcionalidades e comunicação com o banco de dados.
- **HTML:** utilizado para estruturar as páginas e os formulários da aplicação.
- **CSS:** responsável pela apresentação visual e organização dos elementos da interface.
- **JavaScript:** utilizado para implementar interações na interface, como confirmações de ações.
- **SQLite:** banco de dados utilizado para armazenar as informações dos produtos, categorias e fornecedores.
- **Git e GitHub:** ferramentas utilizadas para versionamento, armazenamento do código-fonte e colaboração entre os integrantes da equipe.

## 7. Limites e escopo do sistema

O StockFlow tem como foco o gerenciamento cadastral e a organização das informações relacionadas a produtos, categorias e fornecedores.

Sua finalidade principal é facilitar a administração desses registros e o acompanhamento das quantidades disponíveis em estoque.

Nesta versão, o sistema não contempla funcionalidades como controle de vendas, emissão de notas fiscais, gerenciamento financeiro, processamento de pagamentos ou integração automática com sistemas externos.

Essas funcionalidades não fazem parte do escopo definido para a versão atual do projeto.

## 8. Considerações finais

O desenvolvimento do StockFlow busca oferecer uma solução simples e organizada para o gerenciamento de informações de estoque, reunindo em uma única aplicação os principais registros relacionados a produtos, categorias e fornecedores.

Por meio de sua interface web e de suas funcionalidades de cadastro, consulta, edição e exclusão, o sistema proporciona maior organização das informações e facilita as atividades de administração do estoque.

Dessa maneira, o StockFlow representa uma aplicação voltada à organização e ao gerenciamento de dados, utilizando tecnologias web e ferramentas de desenvolvimento que permitem sua manutenção e evolução em versões futuras.