# Generated by Django 4.2.7 on 2024-05-05 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_pages', '0003_remove_page_qr_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='qr_link',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
