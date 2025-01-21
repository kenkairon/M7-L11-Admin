# Generated by Django 5.1.5 on 2025-01-20 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Energia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_nombre', models.CharField(max_length=100)),
                ('porcentaje', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
