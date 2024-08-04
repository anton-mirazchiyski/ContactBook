class FormControlMixin:
    STYLE = 'form-control border border-dark border-2'

    def apply_bootstrap_classes(self, fields):
        for field_name, field in fields.items():
            field.widget.attrs['class'] = self.STYLE
