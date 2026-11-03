from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto

        fields = [
            "nome",
            "sku",
            "descricao",
            "preco",
            "quantidade_estoque",
            "estoque_minimo",
            "categoria",
            "fornecedor",
        ]

        labels = {
            "nome": "Nome do produto",
            "sku": "SKU",
            "descricao": "Descrição",
            "preco": "Preço",
            "quantidade_estoque": "Quantidade em estoque",
            "estoque_minimo": "Estoque mínimo",
            "categoria": "Categoria",
            "fornecedor": "Fornecedor",
        }

        widgets = {
            "descricao": forms.Textarea(attrs={"rows": 4}),

            "preco": forms.NumberInput(attrs={
                "min": "0",
                "step": "0.01",
            }),

            "quantidade_estoque": forms.NumberInput(attrs={
                "min": "0",
            }),

            "estoque_minimo": forms.NumberInput(attrs={
                "min": "0",
            }),
        }