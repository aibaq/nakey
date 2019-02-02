# Generated by Django 2.1.3 on 2019-01-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190126_1111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='banner',
            name='image_title',
            field=models.CharField(default=1, max_length=500, verbose_name='Наименование ссылки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banner',
            name='subtitle',
            field=models.CharField(default=1, max_length=500, verbose_name='Наименование 2'),
            preserve_default=False,
        ),
    ]