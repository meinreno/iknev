# Generated by Django 2.0.2 on 2018-02-07 00:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('approver', models.ForeignKey(on_delete=None, related_name='action_approver', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Actions',
                'verbose_name': 'Action',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Messages',
                'verbose_name': 'Message',
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('owner_group', models.ForeignKey(on_delete=None, related_name='owner_group', to='auth.Group')),
            ],
            options={
                'verbose_name': 'Processes',
            },
        ),
        migrations.AddField(
            model_name='action',
            name='process',
            field=models.ForeignKey(on_delete=None, related_name='actions', to='iknev_process.Process'),
        ),
    ]
