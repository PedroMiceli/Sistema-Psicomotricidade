# Generated by Django 4.1 on 2022-10-05 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0011_alter_anamnese_data_anamnese_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conclusao',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='desenhofigurahumana',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='primeiraunidadefuncional',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='terceiraunidadefuncional',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
