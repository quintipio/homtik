from django.db import models


class Ingredient(models.Model):
    nom = models.CharField(max_length=60, null=False)

    class Meta:
        verbose_name = "Ingredient"
        ordering = ['nom']

    def __str__(self):
        return self.nom


class AutreProduit(models.Model):
    nom = models.CharField(max_length=60, null=False)

    class Meta:
        verbose_name = "Autre produits"
        ordering = ['nom']

    def __str__(self):
        return self.nom


class Frigo(models.Model):
    ingredient = models.ForeignKey("Ingredient", on_delete=models.PROTECT)
    nombre = models.PositiveIntegerField(default=0)
    dlc = models.DateField(verbose_name="Date limite de consomation", null=True)

    class Meta:
        verbose_name = "Frigo"
        ordering = ['ingredient']

    def __str__(self):
        return self.ingredient.nom


class Recette(models.Model):
    titre = models.CharField(max_length=200, null=False)
    tempsPreparation = models.IntegerField(null=False, verbose_name="Temps de préparation (en min)")
    contenu = models.TextField(null=False)
    ingredients = models.ManyToManyField(Ingredient, through='RecetteIngredient')
    dateDernierePrepa = models.DateField(verbose_name="Date de dernière préparation")

    class Meta:
        verbose_name = "Recette"
        ordering = ['titre']

    def __str__(self):
        return self.titre


class RecetteIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    recette = models.ForeignKey(Recette, on_delete=models.PROTECT)
    nombre = models.PositiveIntegerField(null=False)


class ListeCourse(models.Model):
    nom = models.CharField(null=False, max_length=50)
    ingredients = models.ManyToManyField(Ingredient, through='CourseIngredient')
    autre = models.ManyToManyField(AutreProduit, through='CourseAutre')
    commentaire = models.TextField()

    def __str__(self):
        return self.nom


class CourseIngredient(models.Model):
    listeCourse = models.ForeignKey(ListeCourse, on_delete=models.PROTECT)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    nombre = models.PositiveIntegerField(null=False)


class CourseAutre(models.Model):
    listeCourse = models.ForeignKey(ListeCourse, on_delete=models.PROTECT)
    autre = models.ForeignKey(AutreProduit, on_delete=models.PROTECT)
    nombre = models.PositiveIntegerField(null=False)




