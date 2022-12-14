# Generated by Django 4.1 on 2022-08-26 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_folder_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='description',
            field=models.CharField(blank=True, default='No Description', max_length=300),
        ),
        migrations.AlterField(
            model_name='note',
            name='body',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='note',
            name='folder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='api.folder'),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.TextField(default='unnamed note'),
        ),
    ]
