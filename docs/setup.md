# Setup

## Requirements

- Python 3.10 or higher
- Poetry
- Git
- Docker & Docker Compose (optional)

## Installation

With Poetry installed, you can install the project dependencies by running:

```bash
poetry install
```

## Development

To start the development server, run:

```bash
poetry run dc build
poetry run dc start
```

## Migrations

To run migrations, run:

```bash
poetry run dc migrate
```

## Run the app

To run the development server, run:

```bash
poetry run dc up
```
