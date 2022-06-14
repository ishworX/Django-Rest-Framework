# Generated by Django 4.0.5 on 2022-06-14 02:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='name',
            field=models.CharField(default=1, error_messages={'blank': 'You cannot leave it blank', 'null': 'This field cannot be null'}, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
