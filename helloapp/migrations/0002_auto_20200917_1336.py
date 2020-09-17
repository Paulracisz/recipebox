# Generated by Django 3.1 on 2020-09-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='author',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites', to='helloapp.Recipe'),
        ),
    ]
