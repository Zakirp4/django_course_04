# Generated by Django 2.2.7 on 2020-06-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('std_class', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
            ],
        ),
    ]