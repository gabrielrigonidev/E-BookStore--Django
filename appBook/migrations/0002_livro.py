# Generated by Django 5.1.1 on 2024-09-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('genero', models.CharField(max_length=255)),
                ('paginas', models.PositiveIntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
