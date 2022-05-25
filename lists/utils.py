def clean_up(todolist):
    data = []
    print('reamon')
    print(todolist)
    for instance in todolist:
        collection = {
            'title': instance.title,
            'count_open': instance.count_open,
            'todos': []
        }
        for todo in instance.todos.all():
            collection['todos'].append(
                {
                    'id': todo.id,
                    'position': todo.position,
                    'description': todo.description,
                    'is_finished': todo.is_finished
                }
            )
    return data