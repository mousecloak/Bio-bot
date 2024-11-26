# Bio-bot

A Discord bot, built in python.

## Installation

This project can be built with [poetry](https://python-poetry.org/docs/).

First ensure that [poetry is installed](https://python-poetry.org/docs/#installation) and available on your path.

To install the dependencies of this project, run

```shell
poetry install
```

## Configuration

Copy the `.envtemplate` file to a new file named `.env` and update the placeholder values accordingly.

## Run

To run the project inside a poetry virtual environment, run


```shell
poetry run python main.py
```

## Development

After updating your codebase with new commits, dependencies added or updated by other developers can be introduced to your working environment by 
running

```shell
poetry update
```

For more information on using poetry to manage dependencies, refer to the [poetry documentation.](https://python-poetry.org/docs/basic-usage/#using-your-virtual-environment)