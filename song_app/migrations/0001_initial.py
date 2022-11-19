# Generated by Django 4.1.1 on 2022-11-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artist_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_profile_img', models.ImageField(default='', upload_to='song_info')),
                ('song_name', models.CharField(max_length=50)),
                ('song_length', models.CharField(max_length=20)),
                ('song_genre', models.CharField(max_length=100)),
                ('song_file', models.FileField(upload_to='song_audio')),
                ('song_released', models.DateField(default='-', max_length=30)),
                ('song_writer', models.CharField(default='-', max_length=200)),
                ('song_label', models.CharField(default='-', max_length=100)),
                ('artists', models.ManyToManyField(to='artist_app.artistmodel')),
            ],
            options={
                'db_table': 'song_table',
            },
        ),
    ]
