from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q
from django.db.models.functions import Lower


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    #Meta define o comportamento do modelo de banco de dados
    class Meta:
        ordering = ["nome"] #Ordena analfabeticamente por nome
        constraints = [
            models.UniqueConstraint(
                Lower("nome"),
                name="categoria_nome_case_insensitive_unique",
            ),
        ]

    #retorna um atributo como nome
    def __str__(self): 
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(
        max_length=18,
        unique=True,
        blank=True,
        null=True,
    )
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    sku = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True)

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
    )

    quantidade_estoque = models.PositiveIntegerField(default=0)
    estoque_minimo = models.PositiveIntegerField(default=0)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="produtos",
    )
    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.PROTECT,
        related_name="produtos",
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]
        constraints = [
            models.UniqueConstraint(
                Lower("sku"),
                name="produto_sku_case_insensitive_unique",
            ),
            models.CheckConstraint(
                check=Q(preco__gte=0),
                name="produto_preco_nao_negativo",
            ),
        ]

    def __str__(self):
        return self.nome

    @property
    def estoque_baixo(self):
        return self.quantidade_estoque <= self.estoque_minimo
