from users.models import CustomUser

users = []
for i in range(10):

    user = CustomUser()
    user.email = f'user{i}@test.com'
    user.password = f'password{i}'
    user.display_name = f'User {i}'
    users.append(user)

CustomUser.objects.bulk_create(users)
