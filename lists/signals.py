from django.db.models.signals import post_save
from django.dispatch import receiver
from lists.websocket import send_websocket_data
from lists.models import Todo
from lists.utils import clean_up

@receiver(post_save, sender=Todo)
def todos_updated(sender, instance, created, **kwargs):
    if not instance.position: Todo.objects.filter(id=instance.id).update(position=instance.id)
    clean_data = clean_up(instance.id)
    send_websocket_data(instance.todolist.id, clean_data)