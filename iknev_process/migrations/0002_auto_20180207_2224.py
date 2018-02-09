# Generated by Django 2.0.2 on 2018-02-07 22:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iknev_process', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessWay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequential', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'ProcessWays',
                'verbose_name': 'ProcessWay',
                'ordering': ['sequential'],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=None, related_name='ticket_owner', to=settings.AUTH_USER_MODEL)),
                ('process', models.ForeignKey(on_delete=None, related_name='tickets', to='iknev_process.Process')),
                ('process_way', models.ForeignKey(on_delete=None, related_name='ticket_pw', to='iknev_process.ProcessWay')),
            ],
            options={
                'verbose_name_plural': 'Tickets',
                'verbose_name': 'Ticket',
            },
        ),
        migrations.RemoveField(
            model_name='action',
            name='process',
        ),
        migrations.AddField(
            model_name='action',
            name='responsible',
            field=models.ForeignKey(default=None, on_delete=None, related_name='action_responsible', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processway',
            name='action',
            field=models.ForeignKey(on_delete=None, related_name='pw_action', to='iknev_process.Action'),
        ),
        migrations.AddField(
            model_name='processway',
            name='process',
            field=models.ForeignKey(on_delete=None, related_name='pw_process', to='iknev_process.Process'),
        ),
    ]