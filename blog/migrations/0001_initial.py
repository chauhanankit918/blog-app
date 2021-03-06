# Generated by Django 3.2.9 on 2022-07-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=500, null=True)),
                ('description', models.CharField(max_length=1200, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]
