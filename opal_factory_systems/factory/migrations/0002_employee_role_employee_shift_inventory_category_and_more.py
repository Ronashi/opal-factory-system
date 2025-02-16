# Generated by Django 5.1.5 on 2025-02-13 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.CharField(choices=[('Engineer', 'Engineer'), ('Operator', 'Operator'), ('Technician', 'Technician'), ('Manager', 'Manager')], default='Operator', max_length=50),
        ),
        migrations.AddField(
            model_name='employee',
            name='shift',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='category',
            field=models.CharField(choices=[('Resistor', 'Resistor'), ('Capacitor', 'Capacitor'), ('IC', 'Integrated Circuit'), ('PCB', 'Printed Circuit Board'), ('Other', 'Other')], default='Other', max_length=50),
        ),
        migrations.AddField(
            model_name='inventory',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='supplier',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='inventory_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='factory.inventory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='priority',
            field=models.CharField(choices=[('Low', 'Low'), ('Normal', 'Normal'), ('Urgent', 'Urgent')], default='Normal', max_length=50),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
