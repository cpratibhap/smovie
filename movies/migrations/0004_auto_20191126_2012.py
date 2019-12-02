# Generated by Django 2.2.6 on 2019-11-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20191125_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='active',
            field=models.CharField(default='Y', max_length=2),
        ),
        migrations.AlterField(
            model_name='actor',
            name='aexprc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='actor',
            name='aname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='active',
            field=models.CharField(default='Y', max_length=2),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='director',
            name='active',
            field=models.CharField(default='Y', max_length=2),
        ),
        migrations.AlterField(
            model_name='director',
            name='dexprc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='director',
            name='dname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='active',
            field=models.CharField(default='Y', max_length=2),
        ),
        migrations.AlterField(
            model_name='movie',
            name='mvcategory',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='mvname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='mvreviews',
            field=models.CharField(max_length=100),
        ),
    ]