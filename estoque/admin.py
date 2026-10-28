
from django.contrib import admin

from .models import Categoria, Fornecedor, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "criado_em")
    search_fields = ("nome",)


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "email", "telefone")
    search_fields = ("nome", "cnpj", "email")


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "sku",
        "preco",
        "quantidade_estoque",
        "estoque_minimo",
        "categoria",
        "fornecedor",
    )
    search_fields = ("nome", "sku")
    list_filter = ("categoria", "fornecedor")
