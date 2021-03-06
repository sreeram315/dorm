# Generated by Django 2.1.5 on 2019-01-07 13:29

from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='cgpa',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='section',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[students.validators.validate_section]),
        ),
    ]
