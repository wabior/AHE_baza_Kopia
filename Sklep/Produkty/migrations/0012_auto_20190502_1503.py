# Generated by Django 2.2.1 on 2019-05-02 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0011_auto_20190501_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=60)),
                ('opis', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Producent',
                'verbose_name_plural': 'Producenci',
            },
        ),
        migrations.AlterModelOptions(
            name='produkty',
            options={'verbose_name': 'Produkt', 'verbose_name_plural': 'Produkty'},
        ),
    ]
