# Generated by Django 5.1.3 on 2024-11-13 10:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_profile_generalinfo_linkedin_link_generalinfo_x_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="work_place",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
