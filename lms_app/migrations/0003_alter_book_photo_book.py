# Generated by Django 4.1.1 on 2022-09-13 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0002_alter_book_photo_book_alter_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo_book',
            field=models.ImageField(blank=True, default='/media/photo/photo1.png', null=True, upload_to='photo'),
        ),
    ]