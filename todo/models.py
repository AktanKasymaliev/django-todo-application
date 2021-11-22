from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):

    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    description = models.TextField(verbose_name="Описание")
    deadline = models.DateTimeField(auto_now_add=False)


    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        db_table = "tasks"

class MemberOfTeam(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="member")

    def __str__(self) -> str:
        return f"{self.user} в составе {self.task}"

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
        db_table = "member"