# Generated by Django 4.0.5 on 2023-11-11 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticle',
            name='alt_img_header',
            field=models.CharField(blank=True, max_length=80, verbose_name='Атрибут alt фото шапки (необяз. поле)'),
        ),
        migrations.AlterField(
            model_name='blogarticle',
            name='autor_photo',
            field=models.ImageField(blank=True, default='author_deafaul_foto.jpg', upload_to='blog_img/', verbose_name='Фото автора (необяз. поле), имеется фото по умолчанию'),
        ),
        migrations.AlterField(
            model_name='blogarticle',
            name='img_header_desktop',
            field=models.ImageField(blank=True, default='', upload_to='blog_img/', verbose_name='Фото шапки - desktop 1440х760 (необяз. поле)'),
        ),
        migrations.AlterField(
            model_name='blogarticle',
            name='img_header_mobile',
            field=models.ImageField(blank=True, default='', upload_to='blog_img/', verbose_name='Фото шапки - mobile 576х568 (необяз. поле)'),
        ),
        migrations.AlterField(
            model_name='blogarticle',
            name='img_header_mobile_horizontal',
            field=models.ImageField(blank=True, default='', upload_to='blog_img/', verbose_name='Фото шапки - mobile 768х568 (необяз. поле)'),
        ),
        migrations.AlterField(
            model_name='blogarticle',
            name='img_header_tablet',
            field=models.ImageField(blank=True, default='', upload_to='blog_img/', verbose_name='Фото шапки - tablet 1200х550 (необяз. поле)'),
        ),
        migrations.AlterField(
            model_name='blogarticle',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название статьи (заголовок h1)'),
        ),
        migrations.AlterField(
            model_name='blogarticle',
            name='title_img_header',
            field=models.CharField(blank=True, max_length=80, verbose_name='Атрибут title фото шапки (необяз. поле)'),
        ),
    ]
