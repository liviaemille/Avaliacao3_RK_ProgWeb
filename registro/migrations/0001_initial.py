# Generated by Django 4.1.4 on 2022-12-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Produto')),
                ('status', models.CharField(choices=[('Em estoque', 'Disponível'), ('Doado', 'Doado')], max_length=15, verbose_name='Status')),
                ('doador', models.CharField(max_length=100, verbose_name='Doador')),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('dono', models.CharField(max_length=100, verbose_name='Dono')),
            ],
        ),
    ]
