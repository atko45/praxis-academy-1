# Generated by Django 3.1 on 2020-09-10 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20200908_0345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comic',
            old_name='author',
            new_name='deskripsi',
        ),
        migrations.RenameField(
            model_name='comic',
            old_name='genres',
            new_name='harga',
        ),
        migrations.RenameField(
            model_name='comic',
            old_name='judul',
            new_name='nama',
        ),
        migrations.RenameField(
            model_name='comic',
            old_name='status',
            new_name='stok',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='genres',
            new_name='harga',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='judul',
            new_name='kedaluarsa',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='rating',
            new_name='nama',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='tahun',
            new_name='stok',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='album',
            new_name='deskripsi',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='artis',
            new_name='harga',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='genre',
            new_name='nama',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='judul',
            new_name='stok',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='lirik',
            new_name='ukuran',
        ),
        migrations.RemoveField(
            model_name='comic',
            name='update',
        ),
        migrations.RemoveField(
            model_name='task',
            name='tahun',
        ),
    ]
