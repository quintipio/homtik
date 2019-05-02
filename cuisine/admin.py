from django.contrib import admin
from .models import Ingredient, AutreProduit, Recette, Frigo, ListeCourse, CourseAutre, CourseIngredient,\
    RecetteIngredient, Unite

admin.site.register(Unite)
admin.site.register(Ingredient)
admin.site.register(AutreProduit)
admin.site.register(Recette)
admin.site.register(RecetteIngredient)
admin.site.register(Frigo)
admin.site.register(ListeCourse)
admin.site.register(CourseAutre)
admin.site.register(CourseIngredient)
