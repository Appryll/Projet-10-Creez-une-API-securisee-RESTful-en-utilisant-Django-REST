from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Projects(models.Model):

    TYPES = (
    ("BACK-END","Back-end"),
    ("FRONT-END","Front-end"),
    ("iOS","iOS"),
    ("Android","Android"),
    )

    title = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=1028, null=True, blank=True)
    type = models.CharField(max_length=18, choices=TYPES, default="BACK-END")
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")

    def __str__(self):
        return f'Project : {self.title}'

class Contributors(models.Model):

    PERMISSIONS = (
    ("CRÉER ET LIRE", "Créer et Lire"),
    ("LIRE", "Lire")
    )

    ROLES = (
        ("L'AUTEUR", "L'Auteur"),
        ("CONTRIBUTOR", "Contributor"),
    )

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contributor')
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="project")
    permission = models.CharField(max_length=18, choices=PERMISSIONS, default="CRÉER ET LIRE")
    role = models.CharField(max_length=18, choices=ROLES, default="L'AUTEUR")

    def __str__(self):
        return f'Contributors : {self.user_id}'

class Issues(models.Model):
    PRIORITIES = (
    ("FAIBLE", "Faible"),
    ("MOYENNE", "Moyenne"),
    ("ÉLEVÉE", "Élevée"),
    )

    TAGS = (
    ("BUG", "Bug"),
    ("AMÉLIORATION", "Amélioration"),
    ("TÂCHE", "Tâche"),
    )

    STATUS = (
    ("À FAIRE", "À faire"),
    ("EN COURS", "En cours"),
    ("TERMINÉ", "Terminé"),
    )

    title = models.CharField(max_length=128, null=True, blank=True)
    desc = models.CharField(max_length=1028, null=True, blank=True)
    tag = models.CharField(choices=TAGS, default = "BUG", max_length=18)
    priority = models.CharField(choices=PRIORITIES, default="FAIBLE", max_length=18)
    status = models.CharField(max_length=18, choices=STATUS, default="À FAIRE")
    created_time = models.DateTimeField(default=timezone.now)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee_user_id = models.ForeignKey(Contributors, on_delete=models.CASCADE, related_name="assigne")
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return f'Issue : {self.title}'

class Comments(models.Model):
    description = models.CharField(max_length=1028)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issues, on_delete=models.CASCADE, related_name="issue")
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comments : {self.description}'
