# Generated by Django 4.1.7 on 2023-04-02 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_document_document_guid'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Ongoing', 'Ongoing'), ('Done', 'Done')], default='Pending', max_length=250, null=True),
        ),
    ]
