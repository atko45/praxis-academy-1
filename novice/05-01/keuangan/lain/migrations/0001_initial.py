# Generated by Django 3.1 on 2020-09-15 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_transaksi', models.DateField(auto_now_add=True)),
                ('keterangan', models.CharField(max_length=255)),
                ('kas', models.IntegerField(default=0)),
                ('piutang', models.IntegerField()),
                ('catatan', models.IntegerField(default=0)),
            ],
        ),
    ]