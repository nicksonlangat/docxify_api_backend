# Generated by Django 4.1.7 on 2023-04-02 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_document_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Ongoing', 'Ongoing'), ('Done', 'Done')], default='Pending', max_length=250, null=True),
        ),
    ]