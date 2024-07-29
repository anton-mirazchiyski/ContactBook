class FormControlMixin:
    @staticmethod
    def apply_bootstrap_classes(fields):
        for field_name, field in fields.items():
            field.widget.attrs['class'] = 'form-control border border-dark border-2'
