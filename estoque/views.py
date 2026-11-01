from django.shortcuts import render
from .models import Produto


def inicio(request):
    return render(request, "estoque/inicio.html")


def listar_produtos(request):
    produtos = Produto.objects.all()

    return render(
        request,
        "estoque/produtos.html",
        {"produtos": produtos}
    )