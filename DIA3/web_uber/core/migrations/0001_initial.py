# Generated by Django 2.2.28 on 2023-10-28 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('license', models.CharField(max_length=30, null=True)),
                ('picture', models.CharField(max_length=130, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coments', models.TextField(null=True)),
                ('date_feedback', models.DateField(auto_now=True)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=30, null=True)),
                ('model', models.CharField(max_length=30, null=True)),
                ('year', models.IntegerField()),
                ('vin', models.CharField(max_length=30, null=True)),
                ('picture', models.CharField(max_length=130, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Driver')),
            ],
        ),
    ]
