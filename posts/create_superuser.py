# create_superuser.py
from django.contrib.auth import get_user_model
import os

def run():
    User = get_user_model()
    username = os.getenv("DJANGO_SUPERUSER_USERNAME", "blogadmin")
    email = os.getenv("DJANGO_SUPERUSER_EMAIL", "blog@admin.com")
    password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "blogadmin@05")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print("✅ Superuser created")
    else:
        print("ℹ️ Superuser already exists")
