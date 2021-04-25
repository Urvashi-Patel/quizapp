# Generated by Django 3.2 on 2021-04-25 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'exam',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=512)),
                ('answer1', models.CharField(max_length=512)),
                ('answer2', models.CharField(max_length=512)),
                ('answer3', models.CharField(max_length=512)),
                ('correct_ans', models.CharField(max_length=512)),
                ('exam_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.exam')),
            ],
            options={
                'db_table': 'quiz',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=512)),
                ('exam_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.exam')),
                ('quiz_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.quiz')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
