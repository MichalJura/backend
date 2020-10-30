# Generated by Django 3.1.2 on 2020-10-26 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jedzenie', '0002_adres_restauracja'),
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=30)),
                ('nr_telefonu', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TypRestauracji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='adres',
            name='restauracja',
        ),
        migrations.AddField(
            model_name='restauracja',
            name='adresy',
            field=models.ManyToManyField(to='jedzenie.Adres'),
        ),
        migrations.AddField(
            model_name='restauracja',
            name='opis',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='Zamowienie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cena_zamowienia', models.FloatField()),
                ('przyblizony_czas_dostawy', models.IntegerField()),
                ('klient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedzenie.klient')),
                ('pozycje', models.ManyToManyField(to='jedzenie.Pozycja')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restauracja', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jedzenie.restauracja')),
            ],
        ),
        migrations.AddField(
            model_name='klient',
            name='adres',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedzenie.adres'),
        ),
        migrations.AddField(
            model_name='pozycja',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jedzenie.menu'),
        ),
    ]