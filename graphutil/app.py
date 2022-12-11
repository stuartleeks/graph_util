import click

from graphutil.commands.user import user_command


@click.group()
def cli():
    pass


cli.add_command(user_command)


if __name__ == "__main__":
    cli()
