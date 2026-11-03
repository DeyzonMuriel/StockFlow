from django.test import TestCase
from django.urls import reverse
from .models import Categoria, Fornecedor, Produto
from decimal import Decimal



class EditarCategoriaTests(TestCase):

    def setUp(self):
        self.categoria = Categoria.objects.create(
            nome="Eletrônicos",
            descricao="Produtos eletrônicos"
        )

    def test_abrir_pagina_edicao(self):

        resposta = self.client.get(
            reverse(
                "editar_categoria",
                args=[self.categoria.id]
            )
        )

        self.assertEqual(resposta.status_code, 200)

    def test_editar_categoria(self):

        resposta = self.client.post(
            reverse(
                "editar_categoria",
                args=[self.categoria.id]
            ),
            {
                "nome": "Informática",
                "descricao": "Produtos de informática"
            }
        )

        self.categoria.refresh_from_db()

        self.assertEqual(self.categoria.nome, "Informática")
        self.assertEqual(
            self.categoria.descricao,
            "Produtos de informática"
        )

        self.assertRedirects(
            resposta,
            reverse("listar_categorias")
        )

    def test_impedir_nome_duplicado(self):

        Categoria.objects.create(nome="Móveis")

        resposta = self.client.post(
            reverse(
                "editar_categoria",
                args=[self.categoria.id]
            ),
            {
                "nome": "Móveis",
                "descricao": "Nova descrição"
            }
        )

        self.assertEqual(resposta.status_code, 200)

        self.categoria.refresh_from_db()

        self.assertEqual(self.categoria.nome, "Eletrônicos")

    def test_impedir_nome_vazio(self):

        resposta = self.client.post(
            reverse(
                "editar_categoria",
                args=[self.categoria.id]
            ),
            {
                "nome": "",
                "descricao": "Descrição"
            }
        )

        self.assertEqual(resposta.status_code, 200)

        self.categoria.refresh_from_db()

        self.assertEqual(self.categoria.nome, "Eletrônicos")

class ExcluirCategoriaTests(TestCase):

    def setUp(self):
        self.categoria = Categoria.objects.create(
            nome="Eletrônicos",
            descricao="Produtos eletrônicos"
        )

    def test_excluir_categoria_sem_produtos(self):
        resposta = self.client.post(
            reverse(
                "excluir_categoria",
                args=[self.categoria.id]
            )
        )

        self.assertRedirects(
            resposta,
            reverse("listar_categorias")
        )

        self.assertFalse(
            Categoria.objects.filter(id=self.categoria.id).exists()
        )

    def test_impedir_exclusao_categoria_com_produtos(self):
        fornecedor = Fornecedor.objects.create(
            nome="Fornecedor Teste"
        )

        Produto.objects.create(
            nome="Notebook",
            sku="NOTE-001",
            preco=Decimal("2500.00"),
            categoria=self.categoria,
            fornecedor=fornecedor,
        )

        resposta = self.client.post(
            reverse(
                "excluir_categoria",
                args=[self.categoria.id]
            )
        )

        self.assertEqual(resposta.status_code, 200)

        self.assertContains(
            resposta,
            "Não é possível excluir esta categoria"
        )

        self.assertTrue(
            Categoria.objects.filter(id=self.categoria.id).exists()
        )

    def test_get_nao_exclui_categoria(self):
        resposta = self.client.get(
            reverse(
                "excluir_categoria",
                args=[self.categoria.id]
            )
        )

        self.assertRedirects(
            resposta,
            reverse("listar_categorias")
        )

        self.assertTrue(
            Categoria.objects.filter(id=self.categoria.id).exists()
        )

class ExcluirFornecedorTests(TestCase):

    def setUp(self):
        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor Teste",
            email="teste@email.com",
            telefone="123456789",
            endereco="Rua de Teste"
        )

    def test_excluir_fornecedor_sem_produtos(self):
        response = self.client.post(
            reverse(
                "excluir_fornecedor",
                args=[self.fornecedor.id]
            )
        )

        self.assertFalse(
            Fornecedor.objects.filter(id=self.fornecedor.id).exists()
        )
        self.assertRedirects(response, reverse("listar_fornecedores"))

    def test_impedir_exclusao_de_fornecedor_com_produto(self):
        categoria = Categoria.objects.create(
            nome="Categoria Teste",
            descricao="Descrição de teste"
        )

        Produto.objects.create(
            nome="Produto Teste",
            sku="SKU-TESTE-001",
            descricao="Produto para teste",
            preco=Decimal("10.00"),
            quantidade_estoque=5,
            estoque_minimo=1,
            categoria=categoria,
            fornecedor=self.fornecedor
        )

        response = self.client.post(
            reverse(
                "excluir_fornecedor",
                args=[self.fornecedor.id]
            )
        )

        self.assertTrue(
            Fornecedor.objects.filter(id=self.fornecedor.id).exists()
        )
        self.assertContains(
            response,
            "Não é possível excluir este fornecedor"
        )

    def test_get_nao_exclui_fornecedor(self):
        response = self.client.get(
            reverse(
                "excluir_fornecedor",
                args=[self.fornecedor.id]
            )
        )

        self.assertTrue(
            Fornecedor.objects.filter(id=self.fornecedor.id).exists()
        )
        self.assertRedirects(response, reverse("listar_fornecedores"))