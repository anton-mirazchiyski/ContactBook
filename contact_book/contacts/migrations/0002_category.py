# Generated by Django 5.0.7 on 2024-08-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('contact_category', models.CharField(choices=[('Family', 'Family'), ('Friends', 'Friends'), ('Work', 'Work'), ('Other', 'Other')], max_length=30, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
