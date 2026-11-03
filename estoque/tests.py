from django.test import TestCase
from django.urls import reverse
from .models import Categoria


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