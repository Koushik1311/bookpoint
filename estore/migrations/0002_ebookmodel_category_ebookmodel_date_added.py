# Generated by Django 4.0.4 on 2022-05-24 13:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebookmodel',
            name='category',
            field=models.CharField(default='Uncategorized', max_length=200),
        ),
        migrations.AddField(
            model_name='ebookmodel',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
