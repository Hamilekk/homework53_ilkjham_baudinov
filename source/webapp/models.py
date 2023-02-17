from django.db import models


class ToDoList(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('done', 'Сделано'),
    ]
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Заголовок")
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(verbose_name='Статус', max_length=20,
                              choices=STATUS_CHOICES,
                              default='new')
    due_date = models.DateField(verbose_name='Дата выполнения', blank=True, null=True)

    def __str__(self):
        return f"{self.description}"

    def set_status(self, new_status):
        if new_status in [choice[0] for choice in self.STATUS_CHOICES]:
            self.status = new_status
            self.save()
        else:
            raise ValueError(f"{new_status} is not a valid status.")
