# Generated by Django 4.2.5 on 2023-09-18 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_alter_book_authors_alter_book_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateTimeField(default='N/A'),
        ),
    ]