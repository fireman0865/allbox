# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 17:14
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0003_ipam_add_vlangroups'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vlan',
            options={'ordering': ['site', 'group', 'vid'], 'verbose_name': 'VLAN', 'verbose_name_plural': 'VLANs'},
        ),
        migrations.AlterModelOptions(
            name='vlangroup',
            options={'ordering': ['site', 'name'], 'verbose_name': 'VLAN group', 'verbose_name_plural': 'VLAN groups'},
        ),
        migrations.AlterUniqueTogether(
            name='vlan',
            unique_together=set([('group', 'name'), ('group', 'vid')]),
        ),
    ]
