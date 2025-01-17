# Generated by Django 5.0.3 on 2024-05-27 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_decency_last_2_weeks_alter_decency_last_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('picture', models.ImageField(upload_to='users/pictures/')),
            ],
        ),
    ]
