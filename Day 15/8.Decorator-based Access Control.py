# Decorator-based Access Control
# Roles dictionary
user_roles = {
    "admin": "admin",
    "user1": "user"
}

# Decorator
def require_role(role):
    def decorator(func):
        def wrapper(username, *args, **kwargs):
            if user_roles.get(username) == role:
                return func(username, *args, **kwargs)
            else:
                print("Access Denied!")
        return wrapper
    return decorator

@require_role("admin")
def delete_data(username):
    print(f"{username} deleted data")

@require_role("user")
def view_data(username):
    print(f"{username} viewed data")

# Test
delete_data("admin")
view_data("user1")
delete_data("user1")  # denied