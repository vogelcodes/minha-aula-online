# Generated by Django 3.0.6 on 2021-09-20 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0003_auto_20210920_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='aulas.Lecture_template'),
        ),
    ]