# Generated by Django 3.0.6 on 2020-06-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footballers',
            fields=[
                ('F_id', models.IntegerField(primary_key=True, serialize=False)),
                ('F_name', models.CharField(max_length=100)),
                ('F_salary', models.IntegerField()),
                ('F_goals', models.IntegerField()),
            ],
        ),
    ]