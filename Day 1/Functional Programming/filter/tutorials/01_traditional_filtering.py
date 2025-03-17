

# Traditional imperative approach
def get_active_users(users):
    active_users = []
    for user in users:
        if user['status'] == 'active':
            active_users.append(user)
    return active_users

users = [
    {'id': 1, 'name': 'John', 'status': 'active'},
    {'id': 2, 'name': 'Jane', 'status': 'inactive'},
    {'id': 3, 'name': 'Jim', 'status': 'active'},
]

print(get_active_users(users))
