# Generated by Django 5.1.3 on 2024-12-03 23:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('bad', 'I feel bad'), ('alone', 'I feel lonely'), ('depressed', 'I feel depressed'), ('hard', 'Life is so hard'), ('useless', 'I feel useless'), ('tired', 'I feel tired')], max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Forum',
                'verbose_name_plural': 'Forums',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emoji', models.CharField(choices=[('heart', '❤️'), ('smile', '😊'), ('hugging', '🤗'), ('kiss', '😘'), ('sparkling_heart', '💖'), ('two_hearts', '💕'), ('love_letter', '💌'), ('rose', '🌹'), ('bouquet', '💐'), ('blush', '☺️'), ('cupid', '💘'), ('smiling_face_with_hearts', '🥰'), ('heartbeat', '💓'), ('revolving_hearts', '💞'), ('star_struck', '🤩'), ('peace', '✌️'), ('praying', '🙏'), ('butterfly', '🦋'), ('dove', '🕊️'), ('sunflower', '🌻'), ('rainbow', '🌈'), ('sparkles', '✨'), ('bear', '🐻'), ('panda', '🐼'), ('cat_heart_eyes', '😻'), ('dog', '🐶'), ('stars', '🌟')], max_length=50)),
                ('position_x', models.FloatField()),
                ('position_y', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='emodon_main.forum')),
            ],
        ),
    ]
