from django.contrib.auth.models import User
from django.test import TestCase

from recipes.models import Category, Recipe


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='This is the recipe title',
            description='This is the recipe description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutes',
            servings=5,
            servings_unit='Portions',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            is_published=True,
        )
        return super().setUp()
