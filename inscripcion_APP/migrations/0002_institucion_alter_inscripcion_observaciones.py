# Generated by Django 4.1 on 2022-12-19 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion_APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='observaciones',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
