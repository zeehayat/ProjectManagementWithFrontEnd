import os
import django
from django.urls import get_resolver

# Set the default settings module for your project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_management.settings")

# Initialize Django
django.setup()

# List all URLs
def show_urls():
    urls = get_resolver().url_patterns
    for url in urls:
        print(url)

show_urls()
