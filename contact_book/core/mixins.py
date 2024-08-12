from contact_book.contacts.models import Category


class FormControlMixin:
    STYLE = 'form-control border border-dark border-2'

    def apply_bootstrap_classes(self, fields):
        for field_name, field in fields.items():
            field.widget.attrs['class'] = self.STYLE


class CategoriesCreationMixin:
    @staticmethod
    def get_categories_names():
        return [str(category) for category in Category.objects.all()]

    def check_for_categories_existence(self):
        categories = self.get_categories_names()
        if len(categories) == len(Category.CATEGORY_CHOICES):
            return
        self.create_category()

    def create_category(self):
        for element in Category.CATEGORY_CHOICES:
            category_name = element[0]
            if category_name not in self.get_categories_names():
                Category.objects.create(contact_category=category_name)
