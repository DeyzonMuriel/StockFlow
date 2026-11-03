from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError, transaction
from .models import Produto, Categoria, Fornecedor
from .forms_produtos import ProdutoForm
from django.db.models.deletion import ProtectedError

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

def editar_categoria(request, categoria_id):
    # Busca a categoria pelo ID
    categoria = get_object_or_404(Categoria, id=categoria_id)

    erro = None

    # Verifica se o formulário foi enviado
    if request.method == "POST":

        nome = request.POST.get("nome", "").strip()
        descricao = request.POST.get("descricao", "").strip()

        # Verifica se o nome foi preenchido
        if not nome:
            erro = "O nome da categoria é obrigatório."

        # Verifica se já existe outra categoria com esse nome
        elif Categoria.objects.filter(
            nome__iexact=nome
        ).exclude(id=categoria.id).exists():

            erro = "Já existe uma categoria com esse nome."

        else:
            try:
                # Atualiza os dados da categoria
                with transaction.atomic():
                    categoria.nome = nome
                    categoria.descricao = descricao
                    categoria.save()

                return redirect("listar_categorias")

            except IntegrityError:
                erro = "Não foi possível atualizar a categoria."

    return render(
        request,
        "estoque/editar_categoria.html",
        {
            "categoria": categoria,
            "erro": erro,
        }
    )
def editar_produto(request, produto_id):

    produto = get_object_or_404(Produto, pk=produto_id)

    if request.method == "POST":

        form = ProdutoForm(request.POST, instance=produto)

        if form.is_valid():

            try:
                with transaction.atomic():
                    form.save()

            except IntegrityError:
                form.add_error(
                    "sku",
                    "Este SKU já está sendo utilizado por outro produto."
                )

            else:
                return redirect("listar_produtos")

    else:
        form = ProdutoForm(instance=produto)

    return render(
        request,
        "estoque/editar_produto.html",
        {
            "form": form,
            "produto": produto,
        }
    )
def excluir_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)

    if request.method != "POST":
        return redirect("listar_categorias")

    try:
        categoria.delete()

    except ProtectedError:
        categorias = Categoria.objects.all()

        return render(
            request,
            "estoque/categorias.html",
            {
                "categorias": categorias,
                "erro_exclusao": (
                    "Não é possível excluir esta categoria "
                    "porque existem produtos vinculados a ela."
                ),
            }
        )

    return redirect("listar_categorias")