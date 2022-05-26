from lists.models import Todo

def clean_up(id):
    todo = Todo.objects.get(id=id)
    data = {
        'id': todo.id,
        'position': todo.position,
        'description': todo.description,
        'is_finished': todo.is_finished
    }
    return data