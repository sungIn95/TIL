# Generated by Django 3.2.13 on 2022-10-18 06:23

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='')),
            ],
        ),
    ]
