# Generated by Django 2.2.6 on 2022-04-18 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='credentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('isVerified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=300)),
                ('product_category', models.CharField(max_length=300)),
                ('base_price', models.IntegerField()),
                ('product_defects', models.CharField(max_length=300)),
                ('current_price', models.IntegerField()),
                ('recieved_date', models.CharField(max_length=100)),
                ('shipping_date', models.CharField(max_length=100)),
                ('delivered_date', models.CharField(max_length=100)),
                ('isApproved', models.BooleanField(default=False)),
                ('bidder', models.ManyToManyField(to='user.Users')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='user.Users')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='user.Users')),
            ],
        ),
    ]
