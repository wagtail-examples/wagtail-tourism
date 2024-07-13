import subprocess

import click


@click.group(
    help="CLI tool for managing the Django project. Run 'dj COMMAND --help' for more information about a command."
)
def dj():
    pass


@dj.command(
    help="Run migrations in the Docker container for the project. Run 'dc migrate --help' for more information."
)
def migrate():
    subprocess.run(["echo", "Migrating..."])
    subprocess.run(["docker-compose", "exec", "app", "python", "manage.py", "migrate"])


@dj.command(
    help="Run collectstatic in the Docker container for the project. Run 'dc static --help' for more information."
)
def static():
    subprocess.run(["echo", "Collecting static files..."])
    subprocess.run(
        [
            "docker-compose",
            "exec",
            "app",
            "python",
            "manage.py",
            "collectstatic",
            "--noinput",
        ]
    )
