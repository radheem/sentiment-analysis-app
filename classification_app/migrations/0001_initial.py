# Generated by Django 4.1.2 on 2023-10-22 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserClassifications',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('user_name', models.TextField()),
                ('input_text', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('sentiment', models.CharField(choices=[('positive', 'positive'), ('negative', 'negative'), ('neutral', 'neutral')], default='neutral', max_length=10)),
            ],
            options={
                'db_table': 'UserClassificationRecord',
                'managed': True,
                'index_together': {('user_id', 'createdAt')},
            },
        ),
    ]