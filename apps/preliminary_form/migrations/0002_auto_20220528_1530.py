# Generated by Django 2.0.7 on 2022-05-28 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preliminary_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formentry',
            name='resume',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='preliminary_form.Resume'),
        ),
    ]
