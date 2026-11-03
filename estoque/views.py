from django.shortcuts import render, redirect
from django.db import IntegrityError, transaction
from .models import Produto, Categoria, Fornecedor

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

def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()

    return render(
        request,
        "estoque/fornecedores.html",
        {"fornecedores": fornecedores}
    )

def cadastrar_produto(request):
    erro = None

    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()
        sku = request.POST.get("sku", "").strip()
        descricao = request.POST.get("descricao", "")
        preco = request.POST.get("preco")
        quantidade_estoque = request.POST.get("quantidade_estoque")
        estoque_minimo = request.POST.get("estoque_minimo")
        categoria_id = request.POST.get("categoria")
        fornecedor_id = request.POST.get("fornecedor")

        try:
            with transaction.atomic():
                Produto.objects.create(
                    nome=nome,
                    sku=sku,
                    descricao=descricao,
                    preco=preco,
                    quantidade_estoque=quantidade_estoque,
                    estoque_minimo=estoque_minimo,
                    categoria_id=categoria_id,
                    fornecedor_id=fornecedor_id,
                )

            return redirect("listar_produtos")

        except IntegrityError:
            erro = "Não foi possível cadastrar. Verifique se o SKU já existe."

        except (ValueError, TypeError):
            erro = "Confira os valores informados e tente novamente."

    categorias = Categoria.objects.all()
    fornecedores = Fornecedor.objects.all()

    return render(
        request,
        "estoque/cadastrar_produto.html",
        {
            "categorias": categorias,
            "fornecedores": fornecedores,
            "erro": erro,
        }
    )

def cadastrar_categoria(request):
    erro = None

    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()
        descricao = request.POST.get("descricao", "").strip()

        if not nome:
            erro = "O nome da categoria é obrigatório."

        elif Categoria.objects.filter(nome__iexact=nome).exists():
            erro = "Já existe uma categoria com esse nome."

        else:
            Categoria.objects.create(
                nome=nome,
                descricao=descricao,
            )

            return redirect("listar_categorias")

    return render(
        request,
        "estoque/cadastrar_categoria.html",
        {"erro": erro},
    )

def cadastrar_fornecedor(request):
    erro = None

    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()
        cnpj = request.POST.get("cnpj", "").strip() or None
        email = request.POST.get("email", "").strip()
        telefone = request.POST.get("telefone", "").strip()
        endereco = request.POST.get("endereco", "").strip()

        if not nome:
            erro = "O nome do fornecedor é obrigatório."

        else:
            try:
                Fornecedor.objects.create(
                    nome=nome,
                    cnpj=cnpj,
                    email=email,
                    telefone=telefone,
                    endereco=endereco,
                )

                return redirect("listar_fornecedores")

            except IntegrityError:
                erro = "Este CNPJ já está cadastrado."

    return render(
        request,
        "estoque/cadastrar_fornecedor.html",
        {"erro": erro},
    )