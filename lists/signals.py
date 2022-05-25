from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from lists.websocket import send_websocket_data
from lists.models import Todo, TodoList
from lists.utils import clean_up
import json

@receiver(post_save, sender=Todo)
def todos_updated(sender, instance, created, **kwargs):
    if instance.id:
        qs = TodoList.objects.filter(id=instance.todolist.id)
        clean_data = json.dumps(clean_up(qs))
        send_websocket_data(instance.creator.id, clean_data)
        