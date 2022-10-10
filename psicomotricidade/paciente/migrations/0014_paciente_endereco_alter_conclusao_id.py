# Generated by Django 4.1 on 2022-10-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0013_alter_desenhofigurahumana_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='endereco',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='endereço do paciente'),
        ),
        migrations.AlterField(
            model_name='conclusao',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]