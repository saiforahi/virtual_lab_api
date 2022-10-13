# Generated by Django 4.1.1 on 2022-10-06 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="age",
            field=models.IntegerField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="fb_profile_link",
            field=models.TextField(
                blank=True, max_length=1050, null=True, verbose_name="Facebook Profile"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.IntegerField(
                blank=True, choices=[(1, "PAYMENT"), (0, "REFUND")], null=True
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="linkedin_profile_link",
            field=models.TextField(
                blank=True, max_length=1050, null=True, verbose_name="Linkedin Profile"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="twitter_profile_link",
            field=models.TextField(
                blank=True, max_length=1050, null=True, verbose_name="Twitter Profile"
            ),
        ),
    ]