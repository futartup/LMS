# Generated by Django 3.2.9 on 2021-12-01 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_library_parent_library_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='parent_library_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='library.library'),
        ),
    ]