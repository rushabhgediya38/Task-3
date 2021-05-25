# Generated by Django 3.2.3 on 2021-05-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sApp', '0008_auto_20210525_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterestingUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Interesting_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Non_interesting_url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Non_interesting_url', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='sdata',
            name='Interesting_url',
        ),
        migrations.RemoveField(
            model_name='sdata',
            name='Non_interesting_url',
        ),
    ]
