#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import sys


def main():
    """Run administrative tasks."""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Could not import required packages. "
            "Are they installed and available on your PYTHONPATH environment variable? "
            "Did you forget to activate a virtual environment?"
        ) from exc

    # Bootstrap the application.
    from config.bootstrap import bootstrap
    bootstrap()

    # Execute the management utility.
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
