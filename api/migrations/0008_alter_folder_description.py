# Generated by Django 4.1 on 2022-08-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_note_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='description',
            field=models.CharField(default='No Description', max_length=300),
        ),
    ]
