# Generated by Django 2.0.7 on 2018-07-18 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default='Correct', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=1000),
        ),
        migrations.AddField(
            model_name='team',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riddles.Question'),
        ),
    ]