# Generated by Django 3.0.6 on 2021-09-21 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0006_auto_20210920_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aulas.Lecture_template'),
        ),
    ]