import subprocess

import click


@click.group(
    help="CLI tool for managing the project with Docker. Run 'dc COMMAND --help' for more information about a command."
)
def dc():
    pass


@dc.command(
    help="Builds the Docker images for the project. Run 'dc build --help' for more information."
)
def build():
    subprocess.run(["echo", "Building..."])
    subprocess.run(["docker-compose", "build"])


@dc.command(
    help="Starts the Docker containers for the project. Run 'dc start --help' for more information."
)
def start():
    subprocess.run(["echo", "Starting..."])
    subprocess.run(["docker-compose", "up", "-d"])


@dc.command(
    help="Stops the Docker containers for the project. Run 'dc stop --help' for more information."
)
def stop():
    subprocess.run(["echo", "Stopping..."])
    subprocess.run(["docker-compose", "down"])


@dc.command(
    help="Restarts the Docker containers for the project. Run 'dc restart --help' for more information."
)
def restart():
    subprocess.run(["echo", "Restarting..."])
    subprocess.run(["docker-compose", "restart"])


@dc.command(
    help="Enter the Docker container for the project. Run 'dc enter --help' for more information."
)
def enter():
    subprocess.run(["echo", "Executing..."])
    subprocess.run(["docker-compose", "exec", "app", "bash"])


@dc.command(
    help="Destroy the Docker containers for the project. Run 'dc destroy --help' for more information."
)
def destroy():
    subprocess.run(["echo", "Destroying..."])
    subprocess.run(["docker-compose", "down", "-v"])
