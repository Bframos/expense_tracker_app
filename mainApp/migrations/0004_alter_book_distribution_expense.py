# Generated by Django 4.2.5 on 2023-09-13 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_book_distribution_expense_alter_book_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='distribution_expense',
            field=models.FloatField(default=0, verbose_name='distribution_expense'),
        ),
    ]
