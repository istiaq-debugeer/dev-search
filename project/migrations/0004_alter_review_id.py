# Generated by Django 4.2.1 on 2023-10-11 18:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_review_id_alter_review_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.UUIDField(default=uuid.UUID('231b041d-fdcd-449d-b657-9bc3bbb63d13'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]