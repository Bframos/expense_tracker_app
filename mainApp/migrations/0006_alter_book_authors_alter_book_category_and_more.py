# Generated by Django 4.2.5 on 2023-09-18 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_book_publisher_alter_book_authors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.CharField(default='N/A', max_length=250),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(default='N/A', max_length=250),
        ),
        migrations.AlterField(
            model_name='book',
            name='distribution_expense',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(default='N/A', max_length=250),
        ),
        migrations.AlterField(
            model_name='book',
            name='subtitle',
            field=models.CharField(default='N/A', max_length=250),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='N/A', max_length=250),
        ),
    ]