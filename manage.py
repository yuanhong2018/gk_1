#!/usr/bin/env python
import os
import sys

print(123123123123123)
print(4564564564564645)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gk_1.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
