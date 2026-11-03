from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("produtos/", views.listar_produtos, name="listar_produtos"),
    path("categorias/", views.listar_categorias, name="listar_categorias"),
    path("fornecedores/", views.listar_fornecedores, name="listar_fornecedores"),
    path(
        "produtos/cadastrar/",
        views.cadastrar_produto,
        name="cadastrar_produto",
    ),
]