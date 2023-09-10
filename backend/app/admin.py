from django.conf import settings
from django.contrib import admin

from app.models import (Favorite, Ingredient, Recipe, RecipeIngredient,
                        ShoppingCart, Tag)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'slug')
    search_fields = ('name', 'color', 'slug')
    list_filter = ('name', 'color', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    empty_value_display = settings.EMPTY_VALUE


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = settings.EMPTY_VALUE


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    min_num = 1
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'author',
        'favorites_amount',
        'get_ingredients',
    )
    search_fields = ('name', 'author')
    list_filter = (
        'name',
        'author',
        'tags'
    )
    empty_value_display = settings.EMPTY_VALUE
    inlines = [RecipeIngredientInline, ]

    def favorites_amount(self, obj):
        return obj.favorites.count()

    def get_ingredients(self, obj):
        ingredients = obj.ingredients.all()
        return ", ".join([ingredient.name for ingredient in ingredients])

    get_ingredients.short_description = 'Ingredients'


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'ingredient', 'amount')
    empty_value_display = settings.EMPTY_VALUE


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user', 'recipe')
    empty_value_display = settings.EMPTY_VALUE


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user', 'recipe')
    empty_value_display = settings.EMPTY_VALUE
