# Generated by Django 3.0.6 on 2020-06-19 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Footballers', '0003_auto_20200619_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footballers',
            name='F_goals',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='footballers',
            name='F_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='footballers',
            name='F_salary',
            field=models.IntegerField(),
        ),
    ]