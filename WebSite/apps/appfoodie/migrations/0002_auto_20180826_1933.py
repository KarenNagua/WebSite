# Generated by Django 2.1 on 2018-08-27 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfoodie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Imagen',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
