from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Unite(models.Model):
    nom = models.CharField(max_length=25, null=False)
    diminutif = models.CharField(max_length=5, null=False)
    quantite = models.FloatField(max_length=5, null=False)
    unite_mere = models.ForeignKey("Unite", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Unité"
        ordering = ['nom']
        permissions = (
            ("gerer_unite", "Gérer les unités"),
        )

    def __str__(self):
        return self.nom


class Ingredient(models.Model):
    nom = models.CharField(max_length=60, null=False, unique=True)

    class Meta:
        verbose_name = "Ingredient"
        ordering = ['nom']
        permissions = (
            ("utiliser_ingredient", "Voir, Ajouter un ingrédient"),
            ("modifier_ingredient", "Modifier, Supprimer un ingrédient"),
        )

    def __str__(self):
        return self.nom


class AutreProduit(models.Model):
    nom = models.CharField(max_length=60, null=False, verbose_name="Nom", unique=True)

    class Meta:
        verbose_name = "Autre produits"
        ordering = ['nom']
        permissions = (
            ("utiliser_produit", "Voir, Ajouter un produit"),
            ("modifier_produit", "Modifier, Supprimer un produit"),
        )

    def __str__(self):
        return self.nom


class Frigo(models.Model):
    ingredient = models.ForeignKey("Ingredient", on_delete=models.CASCADE)
    quantite = models.FloatField(max_length=5, null=False)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = "Frigo"
        ordering = ['ingredient']
        permissions = (
            ("gerer_frigo", "Modifier le frigo"),
        )

    def __str__(self):
        return self.ingredient.nom


class Recette(models.Model):
    titre = models.CharField(max_length=200, null=False)
    tempsPreparation = models.IntegerField(null=False, verbose_name="Temps de préparation (en min)",
                                           validators=[MinValueValidator(1), MaxValueValidator(999)])
    contenu = models.TextField(null=False)
    ingredients = models.ManyToManyField(Ingredient, through='RecetteIngredient')
    dateDernierePrepa = models.DateField(verbose_name="Date de dernière préparation")
    DIFFICULTE_CHOICE = (
        (1, 'Très Facile'),
        (2, 'Facile'),
        (3, 'Moyen'),
        (4, 'Difficile'),
        (5, 'Très Difficile'),
    )
    difficulte = models.PositiveIntegerField(
        null=False,
        verbose_name="Difficulté",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        choices=DIFFICULTE_CHOICE,
        default=1,
    )
    CALORIE_CHOICE = (
        (1, 'Très peu calorique'),
        (2, 'Peu calorique'),
        (3, 'Normal'),
        (4, 'Calorique'),
        (5, 'Très Calorique'),
    )
    calorie = models.PositiveIntegerField(
        null=False,
        verbose_name="Calorique",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        choices=CALORIE_CHOICE,
        default=1,
    )
    CATEGORIE_CHOICE = (
        (1, "Entrée"),
        (2, "Plat"),
        (3, "Dessert")
    )
    categorie = models.PositiveIntegerField(
        null=False,
        verbose_name="Catégorie",
        validators=[MinValueValidator(1), MaxValueValidator(3)],
        choices=CATEGORIE_CHOICE,
        default=2,
    )

    class Meta:
        verbose_name = "Recette"
        ordering = ['categorie', 'titre']
        permissions = (
            ("utiliser_recette", "Ajouter, Voir une recette"),
            ("modifier_recette", "Modifier, Supprimer une recette"),
        )

    def __str__(self):
        return self.titre


class RecetteIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    quantite = models.FloatField(max_length=5, null=False)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE, null=False, default=3)


class ListeCourse(models.Model):
    nom = models.CharField(null=False, max_length=50)
    ingredients = models.ManyToManyField(Ingredient, through='CourseIngredient')
    autre = models.ManyToManyField(AutreProduit, through='CourseAutre')
    commentaire = models.TextField()

    class Meta:
        permissions = (
            ("utiliser_liste_course", "Ajouter, Voir, Modifier une liste de course"),
            ("effacer_liste_course", "Supprimer une liste de course"),
        )

    def __str__(self):
        return self.nom


class CourseIngredient(models.Model):
    listeCourse = models.ForeignKey(ListeCourse, on_delete=models.PROTECT)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantite = models.FloatField(null=False)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE, null=False, default=3)
    achete = models.BooleanField(null=False, default=False)


class CourseAutre(models.Model):
    listeCourse = models.ForeignKey(ListeCourse, on_delete=models.PROTECT)
    autre = models.ForeignKey(AutreProduit, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50, null=False)
    achete = models.BooleanField(null=False, default=False)


class Planning(models.Model):
    date = models.DateField(verbose_name="Date", null=False)
    MOMENT_CHOICE = (
        (1, "Midi"),
        (2, "Soir")
    )
    moment = models.PositiveIntegerField(
        null=False,
        verbose_name="Moment de la journée",
        validators=[MinValueValidator(1), MaxValueValidator(2)],
        choices=MOMENT_CHOICE,
        default=2,
    )
    CATEGORIE_CHOICE = (
        (1, "Entrée"),
        (2, "Plat"),
        (3, "Dessert")
    )
    categorie = models.PositiveIntegerField(
        null=False,
        verbose_name="Repas",
        validators=[MinValueValidator(1), MaxValueValidator(3)],
        choices=CATEGORIE_CHOICE,
        default=2,
    )
    recette = models.ForeignKey(Recette, on_delete=models.PROTECT, null=True)
    champ_libre = models.CharField(max_length=300, null=True)



