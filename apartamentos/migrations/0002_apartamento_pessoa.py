# Generated by Django 3.2.7 on 2021-09-22 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
        ('apartamentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartamento',
            name='pessoa',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoa'),
            preserve_default=False,
        ),
    ]
