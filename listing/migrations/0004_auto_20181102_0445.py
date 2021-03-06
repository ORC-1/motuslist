# Generated by Django 2.1.2 on 2018-11-02 03:45

from django.db import migrations, models
import django.utils.timezone
import listing.models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0003_auto_20181102_0414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=255)),
                ('Image_files', models.FileField(upload_to='photos/', validators=[listing.models.file_size])),
                ('Uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='Created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='Logo',
            field=models.FileField(blank=True, null=True, upload_to='photos/', validators=[listing.models.file_size]),
        ),
        migrations.AddField(
            model_name='asset',
            name='Owner',
            field=models.ForeignKey(on_delete='cascade', to='listing.Listing'),
        ),
    ]
