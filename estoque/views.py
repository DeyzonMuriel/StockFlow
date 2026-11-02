from django.shortcuts import render
from .models import Produto, Categoria


def inicio(request):
    return render(request, "estoque/inicio.html")


def listar_produtos(request):
    produtos = Produto.objects.all()

    return render(
        request,
        "estoque/produtos.html",
        {"produtos": produtos}
    )




def listar_categorias(request):
    categorias = Categoria.objects.all()

    return render(
        request,
        "estoque/categorias.html",
        {"categorias": categorias}
    )