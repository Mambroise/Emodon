# Generated by Django 5.1.3 on 2024-12-13 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emodon_main', '0003_alter_mood_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='title',
        ),
        migrations.AddField(
            model_name='forum',
            name='mood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='moods', to='emodon_main.mood'),
        ),
    ]