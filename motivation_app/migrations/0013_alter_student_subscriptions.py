# Generated by Django 4.0.5 on 2022-07-09 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motivation_app', '0012_rename_wishlist_student_wished_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subscriptions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='motivation_app.subscription'),
        ),
    ]
