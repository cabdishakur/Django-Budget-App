# Generated by Django 3.0.5 on 2020-04-29 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200429_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('exp', 'Expense'), ('inc', 'Income')], default='inc', max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='budget',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category'),
        ),
    ]
