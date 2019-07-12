# Generated by Django 2.2.1 on 2019-07-06 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190705_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='article_image_1',
            field=models.ImageField(blank=True, help_text='This is optional', upload_to='blog/static/blog/img'),
        ),
        migrations.AlterField(
            model_name='post',
            name='article_image_2',
            field=models.ImageField(blank=True, help_text='This is optional', upload_to='blog/static/blog/img'),
        ),
        migrations.AlterField(
            model_name='post',
            name='article_image_3',
            field=models.ImageField(blank=True, help_text='This is optional', upload_to='blog/static/blog/img'),
        ),
        migrations.AlterField(
            model_name='post',
            name='article_image_4',
            field=models.ImageField(blank=True, help_text='This is optional', upload_to='blog/static/blog/img'),
        ),
        migrations.AlterField(
            model_name='post',
            name='article_image_5',
            field=models.ImageField(blank=True, help_text='This is optional', upload_to='blog/static/blog/img'),
        ),
        migrations.AlterField(
            model_name='post',
            name='article_image_6',
            field=models.ImageField(blank=True, help_text='This is optional', upload_to='blog/static/blog/img'),
        ),
        migrations.AlterField(
            model_name='post',
            name='main_image',
            field=models.ImageField(help_text='This is required and image must be 1200 x 800', upload_to='blog/static/blog/img'),
        ),
    ]