# Generated by Django 2.2.6 on 2019-10-20 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_folder')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=200)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'images',
                'ordering': ['-post_date'],
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='contact_info',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterModelTable(
            name='profile',
            table='profile',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='projects',
            name='profile',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='mysite.Profile'),
        ),
    ]