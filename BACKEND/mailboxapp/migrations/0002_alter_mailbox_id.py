# Generated by Django 3.2.6 on 2021-08-29 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailboxapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailbox',
            name='id',
            field=models.BigAutoField(db_column='mailbox_id', primary_key=True, serialize=False),
        ),
    ]
