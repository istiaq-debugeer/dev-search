# Generated by Django 4.2.1 on 2023-10-11 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='assets//images//profiles//user-default.png', null=True, upload_to='profiles/'),
        ),
    ]
