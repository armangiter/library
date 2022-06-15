# Generated by Django 4.0.4 on 2022-06-09 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, help_text='This is deleted datetime', null=True, verbose_name='Deleted Datetime')),
                ('is_deleted', models.BooleanField(default=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, help_text='This is active status', verbose_name='Active status')),
                ('name', models.CharField(max_length=50)),
                ('isbn', models.CharField(help_text='International Standard Book Number', max_length=50, verbose_name='ISBN')),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('publisher', models.CharField(blank=True, max_length=50, null=True)),
                ('inventory', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Barrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, help_text='This is deleted datetime', null=True, verbose_name='Deleted Datetime')),
                ('is_deleted', models.BooleanField(default=False, help_text='This is deleted status', verbose_name='Deleted status')),
                ('is_active', models.BooleanField(default=True, help_text='This is active status', verbose_name='Active status')),
                ('barrow_date', models.DateField(default=django.utils.timezone.now)),
                ('return_date', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Barrows', to='librarian.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Barrows', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
