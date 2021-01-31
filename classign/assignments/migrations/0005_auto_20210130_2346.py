# Generated by Django 3.1.5 on 2021-01-30 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0004_auto_20210130_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='CanvasFileSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assignments.canvasassignment')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assignments.canvascourse')),
                ('lms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.canvas')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CanvasTextSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assignments.canvasassignment')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assignments.canvascourse')),
                ('lms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.canvas')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='SimpleCanvasAssignment',
        ),
    ]
