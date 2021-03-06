# Generated by Django 3.0.5 on 2020-05-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20200509_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='galleryitem',
            name='categories',
            field=models.ManyToManyField(related_name='photos', to='gallery.Category'),
        ),
    ]
