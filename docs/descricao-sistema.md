# StockFlow — Descrição do Sistema

## 1. Identificação do projeto

**Nome:** StockFlow  
**Tipo:** Sistema Web de Controle de Estoque  
**Área:** Desenvolvimento de Sistemas Web  
**Tecnologia principal do backend:** Python e Django  
**Banco de dados inicial:** SQLite

## 2. Contextualização

O controle de estoque é uma atividade importante para organizações que precisam acompanhar seus produtos, suas quantidades disponíveis e as informações dos fornecedores. Quando esses dados são administrados de forma desorganizada, podem ocorrer dificuldades na localização de produtos, inconsistências nos registros e falta de visibilidade sobre os itens disponíveis.

O StockFlow é um sistema web acadêmico desenvolvido para organizar essas informações em uma aplicação centralizada, permitindo o gerenciamento de produtos, categorias e fornecedores.

## 3. Problema

A ausência de um sistema centralizado pode dificultar o cadastro, a consulta e a atualização dos dados de estoque, tornando o acompanhamento das informações mais trabalhoso e sujeito a erros.

O StockFlow busca reduzir essas dificuldades por meio de uma aplicação web com dados persistentes e operações organizadas.

## 4. Objetivo geral

Desenvolver um sistema web de controle de estoque que permita cadastrar, consultar, atualizar e excluir produtos, categorias e fornecedores, mantendo seus relacionamentos e a integridade dos dados.

## 5. Objetivos específicos

- Organizar os produtos cadastrados.
- Agrupar produtos por categorias.
- Manter os dados dos fornecedores.
- Relacionar produtos às respectivas categorias e aos fornecedores.
- Validar os dados inseridos pelos usuários.
- Identificar produtos cuja quantidade esteja abaixo do estoque mínimo.
- Aplicar conceitos de desenvolvimento web, modelagem de dados, versionamento e gerenciamento ágil.

## 6. Público-alvo

O sistema é destinado, inicialmente, a pequenos estabelecimentos ou responsáveis pelo controle de estoque que necessitem organizar informações básicas de produtos, categorias e fornecedores.

Esse público representa o contexto de uso proposto para o projeto, não um resultado de pesquisa de mercado.

## 7. Escopo funcional

A primeira versão do StockFlow contemplará:

- Cadastro, listagem, consulta, edição e exclusão de produtos.
- Cadastro, listagem, edição e exclusão de categorias.
- Cadastro, listagem, edição e exclusão de fornecedores.
- Associação de produtos às suas categorias e aos seus fornecedores.
- Registro de preço, quantidade disponível e estoque mínimo.
- Identificação de produtos com estoque baixo.
- Interface web com navegação entre as principais páginas.

## 8. Limites da primeira versão

Não fazem parte do escopo obrigatório inicial:

- Emissão de notas fiscais.
- Integração com sistemas externos.
- Controle de múltiplos depósitos.
- Compras automatizadas.
- Relatórios gerenciais avançados.
- Integração com plataformas de pagamento.

O histórico de movimentações de estoque, a autenticação de usuários e os relatórios adicionais poderão ser incorporados posteriormente, conforme o tempo disponível e a estabilidade das funcionalidades essenciais.

## 9. Tecnologias e ferramentas

- Python: linguagem de programação do backend.
- Django: framework web.
- SQLite: banco de dados para desenvolvimento inicial.
- HTML, CSS e JavaScript: tecnologias de interface.
- Figma: prototipação das telas.
- Git e GitHub: controle de versão e colaboração.
- GitHub Projects: organização das tarefas por meio de um quadro Kanban.

## 10. Resultado esperado

Ao final do desenvolvimento, espera-se obter uma aplicação web funcional, com dados persistentes, operações de gerenciamento de estoque, interface organizada e documentação suficiente para instalação, execução e compreensão do projeto.

O desenvolvimento será incremental, começando pela modelagem e pelas funcionalidades essenciais e avançando para integração, testes e melhorias de usabilidade.