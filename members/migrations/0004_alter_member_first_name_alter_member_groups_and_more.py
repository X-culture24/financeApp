# Generated by Django 5.1.6 on 2025-02-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('members', '0003_bill_created_at_bill_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(default='John', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(default='Doe', max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
