from django.contrib import admin

from api.utils import get_end_letter
from recipes.models import (Favorite, Ingredient, Recipe, RecipeIngredient,
                            ShoppingCart, Tag)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 0
    min_num = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'image', 'text']
    search_fields = ['name', 'author__username']
    list_filter = ['tags']
    inlines = [RecipeIngredientInline]
    readonly_fields = ('in_favorite',)

    def in_favorite(self, obj):
        label = obj.in_favorite.count()
        end_letter = get_end_letter(label)
        return f'всего рецепт добавлен в избранное  {label} раз{end_letter}'
        


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'measurement_unit']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'color', 'slug']
    search_fields = ['name', 'slug']


@admin.register(ShoppingCart)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipe', 'user']
    list_filter = ['user__username', 'user__email']


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipe', 'user']
    search_filter = ['user__username', 'user__email']
