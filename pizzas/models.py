from django.db import models

# Pizzas Models
class Ingrediente(models.Model):
    nome = models.CharField(max_length=50)
    qt_estoque = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    qt_minima = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    qt_maxima = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    un_medida = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class TipoPizza(models.Model):
    nome = models.CharField(max_length=50)
    valor_adicional = models.DecimalField(decimal_places=2, max_digits=7, default=0)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tipo de Pizza'
        verbose_name_plural = 'Tipos de Pizzas'


class SaborBorda(models.Model):
    nome = models.CharField(max_length=50)
    valor_adicional = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    disponivel = models.BooleanField(default=True)
   # ingredientes = models.ManyToManyField(Ingrediente, related_name='ingredientes')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Sabor da Borda'
        verbose_name_plural = 'Sabores de Bordas'

class SaborPizza(models.Model):
    nome = models.CharField(max_length=50)
    tipo_pizza = models.ForeignKey(TipoPizza, on_delete=models.PROTECT)
    descricao = models.TextField(default='')
    valor_adicional = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(null=True, blank=True, upload_to="sabor_pizza_img/", verbose_name="Imagem")
    ingredientes = models.ManyToManyField(Ingrediente, blank=True, through='SaborPizzaIngrediente', related_name='sabores')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Sabor de Pizza'
        verbose_name_plural = 'Sabores de Pizzas'


class SaborPizzaIngrediente(models.Model):
    sabor_pizza = models.ForeignKey(SaborPizza, on_delete=models.CASCADE, related_name='ingredientes_pivot')
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT, related_name='sabores_pivot')
    quantidade = models.DecimalField(decimal_places=2, max_digits=7, default=0)

    class Meta:
        verbose_name = 'Ingrediente do Sabor de Pizza'
        verbose_name_plural = 'Ingredientes do Sabor de Pizza'


class SaborBordaIngrediente(models.Model):
    sabor_borda = models.ForeignKey(SaborBorda, on_delete=models.CASCADE, related_name='ingredientes')
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT, related_name='sabores_borda')
    quantidade = models.DecimalField(decimal_places=2, max_digits=7, default=0)


class TamanhoPizza(models.Model):
    nome = models.CharField(max_length=50)
    max_sabores = models.IntegerField(default=1)
    preco = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    multiplicador = models.DecimalField(decimal_places=2, max_digits=7, default=0)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tamanho da Pizza'
        verbose_name_plural = 'Tamanhos de Pizzas'
