# Generated by Django 2.0.7 on 2022-05-28 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preliminary_form', '0002_auto_20220528_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formentry',
            name='resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='preliminary_form.Resume'),
        ),
    ]