# Generated by Django 3.2.6 on 2021-08-02 19:58

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issueentry',
            options={'verbose_name_plural': 'Entries'},
        ),
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=markdownx.models.MarkdownxField(),
        ),
        migrations.AlterField(
            model_name='issueentry',
            name='description',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
