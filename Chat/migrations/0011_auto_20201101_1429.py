# Generated by Django 3.1.2 on 2020-11-01 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0010_auto_20201101_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='opinion',
            field=models.CharField(blank=True, choices=[('dislike', 'dislike'), ('like', 'like')], max_length=20),
        ),
    ]
