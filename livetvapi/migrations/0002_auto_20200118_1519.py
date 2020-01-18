# Generated by Django 2.2 on 2020-01-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livetvapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdsService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectedAddService', models.CharField(default='google', max_length=100)),
                ('status', models.CharField(default='yes', max_length=100)),
                ('cnt', models.IntegerField(default=4, max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='tvlink',
            name='tv1link',
            field=models.CharField(default='tvlink', max_length=300),
        ),
        migrations.AlterField(
            model_name='tvlink',
            name='tv1name',
            field=models.CharField(default='tvname', max_length=300),
        ),
        migrations.AlterField(
            model_name='tvlink',
            name='tv1ylink',
            field=models.CharField(default='youtubelink', max_length=300),
        ),
        migrations.AlterField(
            model_name='tvlink',
            name='tv2link',
            field=models.CharField(default='tvlink', max_length=300),
        ),
        migrations.AlterField(
            model_name='tvlink',
            name='tv2name',
            field=models.CharField(default='tvname', max_length=300),
        ),
        migrations.AlterField(
            model_name='tvlink',
            name='tv2ylink',
            field=models.CharField(default='youtubelink', max_length=300),
        ),
        migrations.AlterField(
            model_name='tvlink',
            name='tv3link',
            field=models.CharField(default='tvlink', max_length=300),
        ),
        migrations.AlterField(
            model_name='tvlink',
            name='tv3name',
            field=models.CharField(default='tvname', max_length=300),
        ),
        migrations.AlterField(
            model_name='tvlink',
            name='tv3ylink',
            field=models.CharField(default='youtubelink', max_length=300),
        ),
        migrations.AlterField(
            model_name='tvlink',
            name='tv4link',
            field=models.CharField(default='tvlink', max_length=300),
        ),
        migrations.AlterField(
            model_name='tvlink',
            name='tv4name',
            field=models.CharField(default='tvname', max_length=300),
        ),
        migrations.AlterField(
            model_name='tvlink',
            name='tv4ylink',
            field=models.CharField(default='youtubelink', max_length=300),
        ),
        migrations.AlterField(
            model_name='tvlink',
            name='tv5link',
            field=models.CharField(default='tvlink', max_length=300),
        ),
        migrations.AlterField(
            model_name='tvlink',
            name='tv5name',
            field=models.CharField(default='tvname', max_length=300),
        ),
        migrations.AlterField(
            model_name='tvlink',
            name='tv5ylink',
            field=models.CharField(default='youtubelink', max_length=300),
        ),
    ]