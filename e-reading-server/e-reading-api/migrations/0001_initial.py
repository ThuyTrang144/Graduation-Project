# Generated by Django 2.1.7 on 2019-04-04 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField()),
                ('word_result', models.TextField()),
                ('time_request', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='fk_document_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_request_history',
            },
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(max_length=50)),
                ('pronucation', models.CharField(max_length=50)),
                ('popularity', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tbl_vocabulary',
            },
        ),
        migrations.CreateModel(
            name='VocabularyFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_add', models.DateTimeField(auto_now_add=True)),
                ('difficult_level', models.CharField(max_length=25, null=True)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='fk_user_id_favorite', to=settings.AUTH_USER_MODEL)),
                ('vocabulary_id', models.ForeignKey(db_column='vocabulary_id', on_delete=django.db.models.deletion.CASCADE, related_name='fk_vocabulary_id_favorite', to='e-reading-api.Vocabulary')),
            ],
            options={
                'db_table': 'tbl_vocabulary_favorite',
            },
        ),
        migrations.CreateModel(
            name='VocabularyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_vocabulary', models.CharField(max_length=8)),
                ('mean_short', models.TextField(max_length=125)),
                ('mean', models.TextField()),
                ('example', models.TextField()),
                ('id_vocabulary', models.ForeignKey(db_column='id_vocabulary', on_delete=django.db.models.deletion.CASCADE, related_name='fk_vocabulary_id_type', to='e-reading-api.Vocabulary')),
            ],
            options={
                'db_table': 'tbl_vocabulary_type',
            },
        ),
        migrations.AlterUniqueTogether(
            name='vocabulary',
            unique_together={('word', 'pronucation')},
        ),
        migrations.AlterUniqueTogether(
            name='vocabularytype',
            unique_together={('id_vocabulary', 'type_vocabulary')},
        ),
        migrations.AlterUniqueTogether(
            name='vocabularyfavorite',
            unique_together={('user_id', 'vocabulary_id')},
        ),
    ]
