# Generated by Django 5.1.2 on 2024-12-03 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crowdsourcing", "0008_alter_task_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userproject",
            name="role",
            field=models.CharField(
                choices=[
                    ("manager", "Manager"),
                    ("verifier", "Verifier"),
                    ("transcriber", "Transcriber"),
                    ("Candidate", "candidate"),
                    ("block", "Block"),
                ],
                default="Transcriber",
                max_length=100,
            ),
        ),
    ]
