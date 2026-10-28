# StockFlow — Documento de Requisitos

## 1. Introdução

Este documento especifica os requisitos funcionais, os requisitos não funcionais e as regras de negócio da primeira versão do StockFlow.

## 2. Requisitos funcionais

### 2.1. Produtos

**RF01 — Cadastrar produto:** o sistema deve permitir o cadastro de produtos com nome, SKU, descrição, preço, quantidade em estoque, estoque mínimo, categoria e fornecedor.

**RF02 — Listar produtos:** o sistema deve apresentar os produtos cadastrados em uma listagem organizada.

**RF03 — Consultar produto:** o sistema deve permitir visualizar os detalhes de um produto.

**RF04 — Editar produto:** o sistema deve permitir alterar os dados de um produto existente.

**RF05 — Excluir produto:** o sistema deve permitir excluir um produto, mediante confirmação da operação.

**RF06 — Identificar estoque baixo:** o sistema deve identificar produtos cuja quantidade disponível seja menor ou igual ao estoque mínimo.

### 2.2. Categorias

**RF07 — Cadastrar categoria:** o sistema deve permitir cadastrar categorias com nome e descrição.

**RF08 — Listar categorias:** o sistema deve apresentar as categorias cadastradas.

**RF09 — Editar categoria:** o sistema deve permitir atualizar os dados de uma categoria.

**RF10 — Excluir categoria:** o sistema deve permitir excluir uma categoria quando não houver produtos associados a ela.

### 2.3. Fornecedores

**RF11 — Cadastrar fornecedor:** o sistema deve permitir cadastrar fornecedores com nome, CNPJ opcional, e-mail, telefone e endereço.

**RF12 — Listar fornecedores:** o sistema deve apresentar os fornecedores cadastrados.

**RF13 — Editar fornecedor:** o sistema deve permitir atualizar os dados de um fornecedor.

**RF14 — Excluir fornecedor:** o sistema deve permitir excluir um fornecedor quando não houver produtos associados a ele.

### 2.4. Navegação e apresentação

**RF15 — Navegar entre páginas:** o sistema deve permitir acessar as páginas principais de produtos, categorias e fornecedores por meio de uma navegação consistente.

**RF16 — Exibir mensagens:** o sistema deve apresentar mensagens claras de sucesso ou erro após operações relevantes.

**RF17 — Apresentar informações gerais:** a página inicial poderá apresentar indicadores básicos, como quantidade de produtos cadastrados e itens com estoque baixo.

## 3. Requisitos não funcionais

**RNF01 — Usabilidade:** a interface deve apresentar organização visual consistente e navegação compreensível.

**RNF02 — Integridade dos dados:** o sistema deve preservar os relacionamentos e impedir registros incompatíveis com as regras de negócio.

**RNF03 — Persistência:** os dados cadastrados devem permanecer armazenados após o encerramento e a reinicialização do servidor.

**RNF04 — Validação:** os dados recebidos devem ser validados antes de serem persistidos.

**RNF05 — Compatibilidade:** as principais páginas devem funcionar nos navegadores modernos utilizados para a demonstração.

**RNF06 — Manutenibilidade:** o código deve manter separação adequada entre modelos, formulários, views, URLs e templates.

**RNF07 — Versionamento:** o código-fonte e a documentação devem ser mantidos no repositório GitHub, com contribuições identificáveis dos dois integrantes.

**RNF08 — Segurança básica:** o sistema deve utilizar os mecanismos de proteção disponibilizados pelo Django, incluindo proteção CSRF nos formulários aplicáveis e tratamento seguro das entradas.

## 4. Regras de negócio

**RN01 — Identificação do produto:** cada produto deve possuir um SKU único.

**RN02 — Preço:** o preço de um produto não pode ser negativo.

**RN03 — Quantidade:** a quantidade disponível em estoque não pode ser negativa.

**RN04 — Estoque mínimo:** o estoque mínimo não pode ser negativo.

**RN05 — Categoria:** cada produto deve estar associado a uma categoria existente.

**RN06 — Fornecedor:** cada produto deve estar associado a um fornecedor existente.

**RN07 — Nome da categoria:** não devem existir categorias com nomes duplicados, desconsiderando diferenças de maiúsculas e minúsculas.

**RN08 — Exclusão de categoria:** uma categoria com produtos associados não pode ser excluída.

**RN09 — Exclusão de fornecedor:** um fornecedor com produtos associados não pode ser excluído.

**RN10 — Estoque baixo:** um produto deve ser considerado com estoque baixo quando sua quantidade disponível for menor ou igual ao estoque mínimo.

**RN11 — Integridade referencial:** os relacionamentos entre produtos, categorias e fornecedores devem apontar para registros existentes.

## 5. Critérios gerais de aceitação

- Os formulários devem rejeitar dados inválidos.
- Os registros devem ser salvos e recuperados do banco de dados.
- As operações de edição devem atualizar o registro correto.
- As exclusões devem respeitar as regras de relacionamento.
- As páginas principais devem permitir navegação funcional.
- O sistema deve apresentar mensagens compreensíveis ao usuário.
- O comportamento implementado deve corresponder aos requisitos documentados.

## 6. Priorização

### Prioridade alta — primeira entrega e núcleo do sistema

- Modelagem das três entidades.
- Persistência no banco de dados e migrações.
- Telas principais e navegação.
- Documentação dos requisitos e do projeto.

### Prioridade alta — evolução do CRUD

- Cadastro, consulta, edição e exclusão das três entidades.
- Validações e integridade referencial.
- Mensagens de sucesso e erro.

### Prioridade complementar

- Dashboard com indicadores.
- Busca e filtros.
- Histórico de movimentações de estoque.
- Autenticação e relatórios adicionais.

As funcionalidades complementares devem ser priorizadas conforme o tempo restante, sem comprometer a estabilidade do núcleo do sistema.

## 7. Observações

Este documento representa o escopo planejado. Um requisito somente deverá ser considerado implementado após seu desenvolvimento e validação por meio de testes ou demonstração verificável.