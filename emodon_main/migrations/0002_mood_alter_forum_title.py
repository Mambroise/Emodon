# Generated by Django 5.1.3 on 2024-12-13 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emodon_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='forum',
            name='title',
            field=models.CharField(choices=[('bad', 'I feel bad'), ('alone', 'I feel lonely'), ('depressed', 'I feel depressed'), ('hard', 'Life is so hard'), ('useless', 'I feel useless'), ('tired', 'I feel tired'), ('sad', 'I feel sad')], max_length=50),
        ),
    ]
