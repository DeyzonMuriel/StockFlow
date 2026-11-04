# DOCUMENTO DE REQUISITOS — STOCKFLOW

**Projeto:** StockFlow — Sistema de Gerenciamento de Estoque  
**Tipo de sistema:** Aplicação Web  
**Tecnologias:** Python, Django, HTML, CSS, JavaScript e SQLite.  
**Banco de dados:** SQLite.  
**Atores principais:** Funcionário responsável pelo gerenciamento do estoque.

---

# 1. INTRODUÇÃO

## 1.1. Objetivo do documento

Este documento apresenta os requisitos funcionais e não funcionais do StockFlow, estabelecendo as funcionalidades que o sistema deverá oferecer, suas restrições e os critérios de qualidade esperados.

O documento tem como finalidade orientar o desenvolvimento, a implementação, os testes e a validação do sistema, garantindo que as funcionalidades desenvolvidas atendam às necessidades identificadas para o gerenciamento de estoque.

## 1.2. Descrição do sistema

O StockFlow é um sistema web de gerenciamento de estoque desenvolvido para auxiliar no controle e na organização de produtos, categorias e fornecedores de uma organização.

O sistema permite que o funcionário responsável pelo estoque realize operações de cadastro, consulta, edição e exclusão de registros, centralizando as informações em um único ambiente.

A aplicação possui uma interface web desenvolvida com HTML, CSS e JavaScript, enquanto o processamento das informações é realizado utilizando Python e Django. Os dados são armazenados em um banco de dados SQLite.

## 1.3. Objetivo geral

Desenvolver um sistema web que facilite o gerenciamento de produtos, categorias e fornecedores, proporcionando maior organização, controle e acesso às informações relacionadas ao estoque.

## 1.4. Usuário do sistema

**Funcionário:** responsável por utilizar o StockFlow para cadastrar, consultar, editar e excluir produtos, categorias e fornecedores.

---

# 2. REQUISITOS FUNCIONAIS (RF)

Os requisitos funcionais descrevem as funcionalidades e os serviços que o sistema deverá disponibilizar aos usuários.

## 2.1. Módulo geral do sistema

**RF01 — Exibir página inicial**

O sistema deverá disponibilizar uma página inicial contendo a identificação do StockFlow e informações básicas sobre sua finalidade.

**RF02 — Disponibilizar menu de navegação**

O sistema deverá apresentar um menu que permita ao usuário acessar as áreas de produtos, categorias e fornecedores, além da página inicial e do painel administrativo.

## 2.2. Módulo de produtos

**RF03 — Cadastrar produtos**

O sistema deverá permitir o cadastro de novos produtos, solicitando as seguintes informações:

- Nome;
- SKU;
- Descrição;
- Preço;
- Quantidade em estoque;
- Estoque mínimo;
- Categoria;
- Fornecedor.

**RF04 — Listar produtos**

O sistema deverá permitir a visualização dos produtos cadastrados, apresentando informações como nome, SKU, preço, quantidade em estoque, categoria e fornecedor.

**RF05 — Consultar produtos**

O sistema deverá permitir que o funcionário consulte os dados dos produtos cadastrados por meio da listagem disponibilizada pelo sistema.

**RF06 — Editar produtos**

O sistema deverá permitir a alteração das informações de um produto previamente cadastrado, apresentando os dados atuais no formulário de edição.

**RF07 — Excluir produtos**

O sistema deverá permitir a exclusão de produtos cadastrados, solicitando confirmação do usuário antes de efetivar a operação.

**RF08 — Validar informações dos produtos**

O sistema deverá verificar os dados informados durante o cadastro e a edição dos produtos, impedindo o armazenamento de informações inválidas.

**RF09 — Impedir SKU duplicado**

O sistema deverá impedir o cadastro ou a alteração de produtos utilizando um SKU já registrado, considerando também diferenças entre letras maiúsculas e minúsculas.

**RF10 — Controlar valores do estoque**

O sistema deverá impedir que o preço, a quantidade em estoque e o estoque mínimo recebam valores negativos.

## 2.3. Módulo de categorias

**RF11 — Cadastrar categorias**

O sistema deverá permitir o cadastro de novas categorias, solicitando o nome e a descrição da categoria.

**RF12 — Listar categorias**

O sistema deverá apresentar as categorias cadastradas, permitindo que o funcionário consulte suas informações.

**RF13 — Editar categorias**

O sistema deverá permitir a alteração das informações de categorias previamente cadastradas.

**RF14 — Excluir categorias**

O sistema deverá permitir a exclusão de categorias, desde que elas não estejam associadas a produtos cadastrados.

**RF15 — Impedir categorias duplicadas**

O sistema deverá impedir o cadastro de categorias com nomes repetidos, considerando também diferenças entre letras maiúsculas e minúsculas.

## 2.4. Módulo de fornecedores

**RF16 — Cadastrar fornecedores**

O sistema deverá permitir o cadastro de fornecedores, solicitando as seguintes informações:

- Nome;
- CNPJ;
- E-mail;
- Telefone;
- Endereço.

O campo CNPJ deverá ser opcional.

**RF17 — Listar fornecedores**

O sistema deverá apresentar os fornecedores cadastrados, permitindo a consulta de suas informações.

**RF18 — Editar fornecedores**

O sistema deverá permitir a alteração das informações de fornecedores previamente cadastrados.

**RF19 — Excluir fornecedores**

O sistema deverá permitir a exclusão de fornecedores, desde que eles não estejam associados a produtos cadastrados.

**RF20 — Impedir CNPJ duplicado**

O sistema deverá impedir que dois fornecedores possuam o mesmo CNPJ cadastrado.

Quando o CNPJ não for informado, o sistema deverá permitir o cadastro do fornecedor sem essa informação.

## 2.5. Relacionamento entre entidades

**RF21 — Associar produtos a categorias**

O sistema deverá permitir que cada produto seja vinculado a uma categoria cadastrada.

**RF22 — Associar produtos a fornecedores**

O sistema deverá permitir que cada produto seja vinculado a um fornecedor cadastrado.

**RF23 — Preservar relacionamentos existentes**

O sistema deverá impedir a exclusão de categorias ou fornecedores que possuam produtos vinculados, preservando a integridade dos dados.

---

# 3. REQUISITOS NÃO FUNCIONAIS (RNF)

Os requisitos não funcionais estabelecem critérios de qualidade, segurança, desempenho, usabilidade e confiabilidade que o sistema deverá atender.

## 3.1. Usabilidade

**RNF01 — Interface intuitiva**

O sistema deverá possuir uma interface simples, organizada e de fácil compreensão, permitindo que o usuário utilize suas funcionalidades sem dificuldades desnecessárias.

**RNF02 — Padronização visual**

As páginas deverão manter um padrão visual consistente, incluindo cores, fontes, menus, botões, formulários e tabelas.

**RNF03 — Facilidade de navegação**

O sistema deverá oferecer navegação clara entre as páginas de produtos, categorias e fornecedores.

**RNF04 — Mensagens informativas**

O sistema deverá apresentar mensagens compreensíveis para informar o usuário sobre operações realizadas com sucesso ou problemas encontrados durante o preenchimento dos formulários.

## 3.2. Desempenho

**RNF05 — Tempo de resposta**

O sistema deverá responder às operações comuns de cadastro, consulta, edição e exclusão em tempo adequado, considerando as condições normais de execução e o volume de dados previsto para o projeto.

Como meta inicial de avaliação, as operações deverão ser concluídas em até três segundos em ambiente local, nas condições normais de teste.

**RNF06 — Processamento eficiente**

O sistema deverá realizar consultas e operações no banco de dados de maneira eficiente, evitando processamento desnecessário.

## 3.3. Segurança

**RNF07 — Validação dos dados**

O sistema deverá realizar validações dos dados enviados pelos formulários, tanto na interface quanto no processamento realizado pelo servidor.

**RNF08 — Proteção contra requisições indevidas**

O sistema deverá utilizar mecanismos de proteção contra requisições não autorizadas, incluindo a proteção CSRF disponibilizada pelo Django nos formulários que realizam operações de alteração de dados.

**RNF09 — Proteção das operações de exclusão**

As operações de exclusão deverão utilizar requisições apropriadas e exigir confirmação do usuário, evitando remoções acidentais.

**RNF10 — Proteção da integridade dos dados**

O sistema deverá impedir operações que provoquem inconsistências nos relacionamentos entre produtos, categorias e fornecedores.

## 3.4. Confiabilidade e integridade

**RNF11 — Consistência dos dados**

O sistema deverá manter a consistência das informações armazenadas, impedindo registros duplicados quando houver restrições de unicidade.

**RNF12 — Integridade referencial**

O sistema deverá preservar os relacionamentos entre produtos, categorias e fornecedores, impedindo a exclusão de registros utilizados por outros registros.

**RNF13 — Persistência das informações**

Os dados cadastrados deverão permanecer armazenados no banco de dados após o encerramento e a reinicialização da aplicação.

**RNF14 — Tratamento de erros**

O sistema deverá tratar erros durante as operações, apresentando mensagens compreensíveis ao usuário e evitando a exposição desnecessária de informações técnicas internas.

## 3.5. Compatibilidade e portabilidade

**RNF15 — Compatibilidade com navegadores**

O sistema deverá funcionar nos principais navegadores modernos, como Google Chrome, Microsoft Edge e Mozilla Firefox.

**RNF16 — Responsividade**

A interface deverá adaptar sua apresentação a diferentes tamanhos de tela, incluindo computadores, tablets e dispositivos móveis.

**RNF17 — Ambiente de execução**

O sistema deverá ser executado em um ambiente compatível com Python e Django, utilizando as dependências especificadas no arquivo `requirements.txt`.

## 3.6. Manutenibilidade

**RNF18 — Organização do código**

O código-fonte deverá apresentar organização lógica, separando modelos, visualizações, rotas, formulários, arquivos estáticos e templates.

**RNF19 — Facilidade de manutenção**

O sistema deverá permitir a correção de erros e a implementação de melhorias sem exigir modificações desnecessárias em partes independentes da aplicação.

**RNF20 — Documentação técnica**

O projeto deverá possuir documentação que apresente sua finalidade, tecnologias utilizadas, instruções de instalação e orientações para execução.

## 3.7. Acessibilidade e idioma

**RNF21 — Idioma**

A interface deverá apresentar textos, mensagens e instruções em português brasileiro.

**RNF22 — Legibilidade**

O sistema deverá apresentar textos, campos e botões com tamanhos e contrastes adequados para facilitar a leitura e a utilização.

**RNF23 — Identificação dos campos**

Os formulários deverão apresentar rótulos que identifiquem claramente cada campo de preenchimento.

---

# 4. REGRAS DE NEGÓCIO (RN)

As regras de negócio representam restrições e condições que devem ser respeitadas durante a utilização do StockFlow.

**RN01 — Identificação dos produtos**

Cada produto deverá possuir um SKU único.

**RN02 — Preço não negativo**

O preço de um produto não poderá ser inferior a zero.

**RN03 — Quantidade não negativa**

A quantidade de produtos em estoque não poderá ser inferior a zero.

**RN04 — Estoque mínimo não negativo**

O estoque mínimo definido para um produto não poderá ser inferior a zero.

**RN05 — Categoria obrigatória**

Todo produto deverá estar associado a uma categoria cadastrada.

**RN06 — Fornecedor obrigatório**

Todo produto deverá estar associado a um fornecedor cadastrado.

**RN07 — Nome único das categorias**

Não será permitido cadastrar duas categorias com nomes iguais, desconsiderando diferenças entre letras maiúsculas e minúsculas.

**RN08 — CNPJ único**

Quando informado, o CNPJ de um fornecedor não poderá estar associado a outro fornecedor.

**RN09 — Exclusão de categorias**

Uma categoria não poderá ser excluída enquanto possuir produtos vinculados.

**RN10 — Exclusão de fornecedores**

Um fornecedor não poderá ser excluído enquanto possuir produtos vinculados.

**RN11 — Descrição opcional**

A descrição dos produtos e categorias poderá permanecer vazia.

**RN12 — Dados opcionais do fornecedor**

O CNPJ, e-mail, telefone e endereço poderão ser informados de acordo com a necessidade do cadastro, respeitando a obrigatoriedade definida para o nome do fornecedor.

---

# 5. RESTRIÇÕES E LIMITES DO SISTEMA

O StockFlow possui como escopo principal o gerenciamento de produtos, categorias e fornecedores.

Não fazem parte do escopo definido para esta versão:

- Controle de vendas;
- Emissão de notas fiscais;
- Controle financeiro;
- Gestão de pagamentos;
- Integração com sistemas externos;
- Compras automáticas;
- Leitura de códigos de barras;
- Gestão de funcionários;
- Controle avançado de permissões;
- Histórico completo de movimentações de estoque.

Essas funcionalidades poderão ser consideradas em versões futuras, caso exista necessidade.

---

# 6. CONSIDERAÇÕES FINAIS

Os requisitos funcionais e não funcionais apresentados neste documento estabelecem as funcionalidades e características esperadas para o StockFlow.

Os requisitos funcionais definem as operações disponibilizadas ao usuário, principalmente o gerenciamento completo de produtos, categorias e fornecedores.

Os requisitos não funcionais estabelecem condições relacionadas à usabilidade, segurança, desempenho, integridade, compatibilidade e manutenção do sistema.

As regras de negócio complementam os requisitos, definindo restrições necessárias para preservar a consistência das informações armazenadas.

Dessa forma, este documento serve como referência para o desenvolvimento, a validação e a avaliação do StockFlow, auxiliando a equipe na construção de um sistema organizado, funcional e adequado às necessidades de gerenciamento de estoque.