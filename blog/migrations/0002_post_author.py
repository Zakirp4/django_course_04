# Generated by Django 2.2.7 on 2020-07-04 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='harun', max_length=50),
            preserve_default=False,
        ),
    ]
