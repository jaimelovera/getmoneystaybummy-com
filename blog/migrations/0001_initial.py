# Generated by Django 2.2.1 on 2019-07-20 13:07

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_featured', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='NO', max_length=3)),
                ('category', models.CharField(choices=[('FRUGALITY', 'Frugality'), ('INVESTING', 'Investing'), ('CREDIT_CARDS', 'Credit Cards')], max_length=20)),
                ('main_image', models.ImageField(help_text='Aspect ratio must be exactly 3:2 </br> i.e. 1200 x 800', upload_to='blog/static/blog/img', validators=[blog.models.validate_image])),
                ('inline_image_1', models.ImageField(blank=True, default=None, help_text='Optional', null=True, upload_to='blog/static/blog/img')),
                ('inline_image_2', models.ImageField(blank=True, default=None, help_text='Optional', null=True, upload_to='blog/static/blog/img')),
                ('inline_image_3', models.ImageField(blank=True, default=None, help_text='Optional', null=True, upload_to='blog/static/blog/img')),
                ('inline_image_4', models.ImageField(blank=True, default=None, help_text='Optional', null=True, upload_to='blog/static/blog/img')),
                ('inline_image_5', models.ImageField(blank=True, default=None, help_text='Optional', null=True, upload_to='blog/static/blog/img')),
                ('inline_image_6', models.ImageField(blank=True, default=None, help_text='Optional', null=True, upload_to='blog/static/blog/img')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('body_html', models.TextField(help_text="<p> Use the following tags:</br> <xmp><h1>Bold Header</h1></xmp> <xmp><p>Paragraph</p></xmp> <xmp><h2>Quote</h2></xmp> <xmp><a href='url' target='_blank'>Link</a></xmp> <xmp><img1> - <img6></xmp> </p>", verbose_name='body (HTML)')),
                ('published_date', models.DateTimeField(blank=True, default=None, help_text='Post will not be published until this field is set </br> *Leave blank for draft', null=True)),
            ],
        ),
    ]
