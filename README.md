# E-commerce - Sistema de Compras

Este é um projeto de e-commerce desenvolvido utilizando **Django** para o back-end e **JavaScript** para o front-end. O sistema oferece funcionalidades básicas de **login de usuários**, **carrinho de produtos** e **busca de produtos**.

## Tecnologias Utilizadas

- **Back-end**: 
  - Python
  - Django (com Django REST Framework para APIs)
  - Banco de dados: PostgreSQL
- **Front-end**:
  - JavaScript (vanilla JS ou framework como React, dependendo da implementação)
  - HTML5, CSS3
  - Bootstrap 5 para layout responsivo

## Funcionalidades

### 1. Login de Usuários

- Usuários podem criar contas, fazer login e acessar a área personalizada do site.
- Implementação de autenticação utilizando Django e Django REST Framework.
  
### 2. Carrinho de Produtos

- Adicionar e remover produtos do carrinho.
- Visualizar os produtos no carrinho, com a quantidade e o total de preços.
- Persistir o carrinho de compras, mesmo após recarregar a página (por exemplo, usando cookies ou localStorage).

### 3. Busca de Produtos

- Funcionalidade de busca que permite ao usuário procurar por produtos específicos.
- Resultados de busca dinâmicos com base no nome ou descrição dos produtos.

## Como Rodar o Projeto

### 1. Requisitos

- **Python 3.8+**
- **Django 3.2+**
- **PostgreSQL** (ou outro banco de dados de sua escolha)
- **Node.js e npm** (caso esteja utilizando React ou qualquer outro front-end dinâmico)

### 2. Configuração do Ambiente

Clone o repositório:

```bash
git clone https://github.com/FFS4ant0s/Projeto-E-commerce.git
cd Projeto-E-commerce
