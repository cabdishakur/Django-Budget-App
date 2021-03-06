# Generated by Django 3.0.5 on 2020-04-29 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200429_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('exp', 'Expense'), ('inc', 'Income')], default='inc', max_length=3)),
                ('name', models.CharField(max_length=80)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
        migrations.DeleteModel(
            name='Income',
        ),
    ]
