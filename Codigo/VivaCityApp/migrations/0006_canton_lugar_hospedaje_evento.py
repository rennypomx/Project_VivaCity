# Generated by Django 4.2.7 on 2024-01-22 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VivaCityApp', '0005_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='canton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre_canton', models.CharField(max_length=225, null=True)),
            ],
            options={
                'verbose_name': 'nombre_canton',
                'verbose_name_plural': 'nombre_cantones',
                'ordering': ['nombre_canton'],
            },
        ),
        migrations.CreateModel(
            name='lugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre_lugar', models.CharField(max_length=225, null=True)),
                ('fotolugar', models.ImageField(null=True, upload_to='')),
                ('direccionlugar', models.URLField(null=True)),
                ('horario', models.DateTimeField(null=True)),
                ('tipo_lugar', models.CharField(max_length=225, null=True)),
                ('canton_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VivaCityApp.canton')),
            ],
            options={
                'verbose_name': 'lugar',
                'verbose_name_plural': 'lugares',
                'ordering': ['nombre_lugar'],
            },
        ),
        migrations.CreateModel(
            name='hospedaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre_hospedaje', models.CharField(max_length=225, null=True)),
                ('fotoHospedaje', models.ImageField(null=True, upload_to='')),
                ('direccionHospedaje', models.URLField(null=True)),
                ('hora_abre', models.TimeField(null=True)),
                ('hora_cierra', models.TimeField(null=True)),
                ('infoHospedaje', models.TextField(null=True)),
                ('precioNoche', models.DecimalField(decimal_places=4, max_digits=15, null=True)),
                ('tipoHospedaje', models.CharField(max_length=225, null=True)),
                ('categoria', models.CharField(max_length=225, null=True)),
                ('canton_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VivaCityApp.canton')),
            ],
            options={
                'verbose_name': 'hospedaje',
                'verbose_name_plural': 'hospedajes',
                'ordering': ['nombre_hospedaje'],
            },
        ),
        migrations.CreateModel(
            name='evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nomEvento', models.CharField(max_length=225, null=True)),
                ('fecha_inicio', models.DateTimeField(null=True)),
                ('fecha_fin', models.DateTimeField(null=True)),
                ('direccionEvento', models.URLField(null=True)),
                ('infoEvento', models.TextField(max_length=225, null=True)),
                ('fotoEvento', models.ImageField(null=True, upload_to='static/eventos/images')),
                ('canton_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VivaCityApp.canton')),
            ],
            options={
                'verbose_name': 'evento',
                'verbose_name_plural': 'evento',
                'ordering': ['nomEvento'],
            },
        ),
    ]
