# Generated by Django 4.0.5 on 2022-06-09 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SoftDesk', '0005_delete_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='issue_id',
            new_name='issue',
        ),
    ]
