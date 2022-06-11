# Generated by Django 4.0.5 on 2022-06-10 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('CRÉER ET LIRE', 'Créer et Lire'), ('LIRE', 'Lire')], default='CRÉER ET LIRE', max_length=18)),
                ('role', models.CharField(choices=[("L'AUTEUR", "L'Auteur"), ('CONTRIBUTOR', 'Contributor')], default="L'AUTEUR", max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.CharField(blank=True, max_length=1028, null=True)),
                ('type', models.CharField(choices=[('BACK-END', 'Back-end'), ('FRONT-END', 'Front-end'), ('iOS', 'iOS'), ('Android', 'Android')], default='BACK-END', max_length=18)),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('desc', models.CharField(blank=True, max_length=1028, null=True)),
                ('tag', models.CharField(choices=[('BUG', 'Bug'), ('AMÉLIORATION', 'Amélioration'), ('TÂCHE', 'Tâche')], default='BUG', max_length=18)),
                ('priority', models.CharField(choices=[('FAIBLE', 'Faible'), ('MOYENNE', 'Moyenne'), ('ÉLEVÉE', 'Élevée')], default='FAIBLE', max_length=18)),
                ('status', models.CharField(choices=[('À FAIRE', 'À faire'), ('EN COURS', 'En cours'), ('TERMINÉ', 'Terminé')], default='À FAIRE', max_length=18)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('assignee_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigne', to='SoftDesk.contributors')),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SoftDesk.projects')),
            ],
        ),
        migrations.AddField(
            model_name='contributors',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='SoftDesk.projects'),
        ),
        migrations.AddField(
            model_name='contributors',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1028)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issues_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue', to='SoftDesk.issues')),
            ],
        ),
    ]
