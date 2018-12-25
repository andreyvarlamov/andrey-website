# Generated by Django 2.1.1 on 2018-11-15 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('name', models.CharField(max_length=200)),
                ('secName', models.CharField(max_length=200)),
                ('start_date', models.DateField(verbose_name='date activity started')),
                ('end_date', models.DateField(verbose_name='date activity ended')),
                ('attachments', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('detail', models.CharField(max_length=200)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
