# Generated by Django 2.1 on 2018-08-26 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=30)),
                ('Apellido', models.CharField(blank=True, max_length=30)),
                ('Cedula', models.CharField(max_length=10)),
                ('Direccion', models.CharField(blank=True, max_length=30)),
                ('Telefono', models.CharField(blank=True, max_length=10)),
                ('Correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cliente', models.CharField(blank=True, max_length=30)),
                ('Cantidad', models.IntegerField()),
                ('PrecioTotal', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=30)),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Descripcion', models.CharField(blank=True, max_length=150)),
                ('Imagen', models.ImageField(blank=True, upload_to='static')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=30)),
                ('Gerente', models.CharField(blank=True, max_length=30)),
                ('Direccion', models.CharField(blank=True, max_length=30)),
                ('Telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CI', models.CharField(max_length=10)),
                ('Nombres', models.CharField(blank=True, max_length=30)),
                ('Apellidos', models.CharField(blank=True, max_length=30)),
                ('Direccion', models.CharField(blank=True, max_length=30)),
                ('Telefono', models.CharField(blank=True, max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profiles')),
                ('contra', models.CharField(blank=True, default='', max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='idPro',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='appfoodie.Restaurante'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='idPed',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='appfoodie.Producto'),
        ),
    ]
