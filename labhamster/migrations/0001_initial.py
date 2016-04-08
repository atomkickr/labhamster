# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 20:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import labhamster.customfields.datafields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=b'name of product category', max_length=20, unique=True, verbose_name=b'Product Category')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=b'descriptive name of grant', max_length=40, unique=True)),
                ('grant_id', models.CharField(blank=True, max_length=30, unique=True)),
                ('comment', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('name', 'grant_id'),
                'verbose_name': 'Grant',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=b'short descriptive name of this item', max_length=60, unique=True)),
                ('catalog', models.CharField(help_text=b'catalogue number', max_length=30)),
                ('shelflife', labhamster.customfields.datafields.DayModelField(blank=True, null=True, unit=b'months', verbose_name=b'Shelf Life')),
                ('status', models.CharField(choices=[(b'ok', b'in stock'), (b'low', b'running low'), (b'out', b'not in stock'), (b'expired', b'expired'), (b'deprecated', b'deprecated')], default=b'out', max_length=20, verbose_name=b'Status')),
                ('link', models.URLField(blank=True, help_text=b'URL Link to product description')),
                ('comment', models.TextField(blank=True, help_text=b'', verbose_name=b'comments & description')),
                ('location', models.CharField(blank=True, help_text=b'location in the lab', max_length=60)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labhamster.Category', verbose_name=b'Product Category')),
            ],
            options={
                'ordering': ('name', 'vendor'),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(b'draft', b'draft'), (b'pending', b'pending'), (b'quote', b'quote requested'), (b'ordered', b'ordered'), (b'received', b'received'), (b'cancelled', b'cancelled')], default=b'pending', max_length=20, verbose_name=b'Status')),
                ('date_created', models.DateField(auto_now_add=True, help_text=b'Date when order was created', verbose_name=b'requested')),
                ('date_ordered', models.DateField(blank=True, help_text=b'Date when order was placed', null=True, verbose_name=b'ordered')),
                ('date_received', models.DateField(blank=True, help_text=b'Date when item was received', null=True, verbose_name=b'received')),
                ('unit_size', models.CharField(blank=True, help_text=b'e.g. "10 l", "1 kg", "500 tips"', max_length=20, null=True)),
                ('quantity', models.IntegerField(default=1, help_text=b'number of units ordered')),
                ('price', models.DecimalField(blank=True, decimal_places=2, help_text=b'cost per unit (!)', max_digits=6, null=True, verbose_name=b'Unit price')),
                ('grant_category', models.CharField(choices=[(b'consumables', b'consumables'), (b'equipment', b'equipment')], default=b'consumables', max_length=20, verbose_name=b'Grant category')),
                ('comment', models.TextField(blank=True, help_text=b'Order-related remarks. Please put catalog number and descriptions not here but into the item page.')),
                ('created_by', models.ForeignKey(help_text=b'user who created this order', on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL, verbose_name=b'requested by')),
                ('grant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='labhamster.Grant')),
                ('item', models.ForeignKey(help_text=b'Click the magnifying lens to select from the list of existing items.\nFor a new item, first click the lens, then click "Add Item" and fill out and save the Item form.', on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='labhamster.Item', verbose_name=b'Item')),
                ('ordered_by', models.ForeignKey(blank=True, help_text=b'user who sent this order out', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name=b'ordered by')),
            ],
            options={
                'ordering': ('date_created', 'id'),
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=b'short descriptive name of this supplier', max_length=30, unique=True, verbose_name=b'Vendor name')),
                ('link', models.URLField(blank=True, help_text=b'URL Link to Vendor home page')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name=b'Phone')),
                ('email', models.CharField(blank=True, max_length=30, verbose_name=b'E-mail')),
                ('contact', models.CharField(blank=True, max_length=30, verbose_name=b'Primary contact name')),
                ('login', models.CharField(blank=True, max_length=50, verbose_name=b'Account Login')),
                ('password', models.CharField(blank=True, max_length=30, verbose_name=b'Password')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='item',
            name='vendor',
            field=models.ForeignKey(help_text=b'select normal supplier of this item', on_delete=django.db.models.deletion.CASCADE, to='labhamster.Vendor', verbose_name=b'Vendor'),
        ),
    ]