# Generated by Django 5.1.3 on 2024-12-13 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emodon_main', '0004_remove_forum_title_forum_mood'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emoji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='reaction',
            name='emoji',
        ),
        migrations.AddField(
            model_name='reaction',
            name='icon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='icons', to='emodon_main.emoji'),
        ),
    ]
