# Generated by Django 5.2 on 2025-04-29 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_waitlist_delete_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waitlist',
            old_name='DOB',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='waitlist',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='waitlist',
            old_name='Name',
            new_name='name',
        ),
    ]
