from django.core.exceptions import ValidationError

from .test_recipe_base import RecipeTestBase


class RecipeModelCategoryTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(name='Model category test')
        return super().setUp()

    def test_recipe_category_model_string_representarion(self):
        self.assertEqual(
            str(self.category),
            self.category.name
        )

    def test_recipe_category_model_name_has_more_than_65_chars(self):
        self.category.name = 'a' * 66
        with self.assertRaises(ValidationError):
            self.category.full_clean()
