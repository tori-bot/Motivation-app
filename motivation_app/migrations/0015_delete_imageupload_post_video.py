# Generated by Django 4.0.5 on 2022-07-12 15:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motivation_app', '0014_imageupload_remove_post_content_image_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageUpload',
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]
