# Generated by Django 4.2.5 on 2023-09-18 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_alter_book_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.CharField(default='N/A', max_length=250),
        ),
    ]