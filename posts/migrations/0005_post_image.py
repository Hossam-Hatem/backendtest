# Generated by Django 3.2 on 2022-08-29 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_contnent'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='posts/'),
            preserve_default=False,
        ),
    ]
