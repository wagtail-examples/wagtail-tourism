import subprocess

import click


@click.command()
def build():
    subprocess.run(["echo", "Building..."])
    subprocess.run(["docker-compose", "build"])


@click.command()
def start():
    subprocess.run(["echo", "Starting..."])
    subprocess.run(["docker-compose", "up", "-d"])


@click.command()
def stop():
    subprocess.run(["echo", "Stopping..."])
    subprocess.run(["docker-compose", "down"])


@click.command()
def restart():
    subprocess.run(["echo", "Restarting..."])
    subprocess.run(["docker-compose", "restart"])


@click.command()
def enter():
    subprocess.run(["echo", "Executing..."])
    subprocess.run(["docker-compose", "exec", "app", "bash"])


@click.command()
def migrate():
    subprocess.run(["echo", "Migrating..."])
    subprocess.run(["docker-compose", "exec", "app", "python", "manage.py", "migrate"])


@click.command()
def static():
    subprocess.run(["echo", "Collecting static files..."])
    subprocess.run(
        ["docker-compose", "exec", "app", "python", "manage.py", "collectstatic"]
    )


@click.command()
def destroy():
    subprocess.run(["echo", "Destroying..."])
    subprocess.run(["docker-compose", "down", "-v"])
