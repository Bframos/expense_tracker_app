# Generated by Django 4.2.5 on 2023-09-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_alter_book_distribution_expense'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(default='vazio', max_length=250),
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='book',
            name='distribution_expense',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='subtitle',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterModelTable(
            name='book',
            table='Book',
        ),
    ]
