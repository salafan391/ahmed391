# Generated by Django 4.1.3 on 2022-11-30 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alfreed', '0002_remove_outcomes_person_remove_outcomes_sales_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='products',
            field=models.CharField(blank=True, default='لا يوجد', max_length=150, null=True),
        ),
    ]
