# Generated by Django 4.2 on 2023-09-18 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default', upload_to='profile_pics')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
