# Generated by Django 3.2.6 on 2022-02-10 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailBox',
            fields=[
                ('id', models.BigAutoField(db_column='mailbox_id', primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=20)),
                ('link_title', models.CharField(max_length=40)),
                ('mailbox_link', models.URLField(null=True)),
                ('open_date', models.DateField()),
                ('key', models.CharField(db_column='mailbox_key', max_length=50, null=True)),
                ('checked', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailboxes', to='accountapp.appuser')),
            ],
            options={
                'db_table': 'mailbox',
            },
        ),
    ]
