# Generated by Django 2.2 on 2019-04-30 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_customer', models.BooleanField(default=False)),
                ('is_courier', models.BooleanField(default=False)),
                ('is_merchant', models.BooleanField(default=False)),
                ('contact_number', models.CharField(max_length=10, unique=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('picture', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourierProfile',
            fields=[
                ('drivers_license', models.PositiveSmallIntegerField()),
                ('drivers_license_expiry', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('suburb', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=4)),
                ('state', models.CharField(choices=[('NSW', 'New South Wales'), ('VIC', 'Victoria'), ('SA', 'South Australia'), ('WA', 'Western Australia'), ('NT', 'Northern Territory'), ('TAS', 'Tasmania')], max_length=3)),
                ('country', models.CharField(default='Australia', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile')),
            ],
        ),
    ]
