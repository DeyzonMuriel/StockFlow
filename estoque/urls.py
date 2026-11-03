from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    
    path(
        "produtos/cadastrar/",
        views.cadastrar_produto,
        name="cadastrar_produto",
    ),

    path("produtos/", views.listar_produtos, 
    name="listar_produtos"),
        path(
        "produtos/<int:produto_id>/editar/",
        views.editar_produto,
        name="editar_produto",
    ),

    path("categorias/", views.listar_categorias, name="listar_categorias"),

    path(
        "categorias/cadastrar/",
        views.cadastrar_categoria,
        name="cadastrar_categoria",
    ),
    path(
        "categorias/<int:categoria_id>/editar/",
        views.editar_categoria,
        name="editar_categoria",
    ),
    path(
        "categorias/<int:categoria_id>/excluir/",
        views.excluir_categoria,
        name="excluir_categoria",
    ),
    path(
    "produtos/<int:produto_id>/excluir/",
    views.excluir_produto,
    name="excluir_produto",
    ),

    path(
        "fornecedores/cadastrar/",
        views.cadastrar_fornecedor,
        name="cadastrar_fornecedor",
    ),

    path("fornecedores/", views.listar_fornecedores, name="listar_fornecedores"),

    path(
    "fornecedores/<int:fornecedor_id>/editar/",
    views.editar_fornecedor,
    name="editar_fornecedor",
    ),

    path("fornecedores/<int:fornecedor_id>/excluir/", views.excluir_fornecedor, name="excluir_fornecedor",)



]