# Generated by Django 2.1.3 on 2019-02-26 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190211_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='image_title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование ссылки'),
        ),
        migrations.AddField(
            model_name='banner',
            name='image_title_kz',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование ссылки'),
        ),
        migrations.AddField(
            model_name='banner',
            name='image_title_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование ссылки'),
        ),
        migrations.AddField(
            model_name='banner',
            name='subtitle_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование 2'),
        ),
        migrations.AddField(
            model_name='banner',
            name='subtitle_kz',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование 2'),
        ),
        migrations.AddField(
            model_name='banner',
            name='subtitle_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование 2'),
        ),
        migrations.AddField(
            model_name='banner',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='banner',
            name='title_kz',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='banner',
            name='title_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_kz',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='color',
            name='name_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='color',
            name='name_kz',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='color',
            name='name_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='item',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='item',
            name='description_kz',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='item',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='item',
            name='name_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='item',
            name='name_kz',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='item',
            name='name_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='name_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='name_kz',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='name_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='size',
            name='name_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='size',
            name='name_kz',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='size',
            name='name_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Наименование'),
        ),
    ]
