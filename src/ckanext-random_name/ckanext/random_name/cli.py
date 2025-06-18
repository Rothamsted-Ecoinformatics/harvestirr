import click


@click.group(short_help="random_name CLI.")
def random_name():
    """random_name CLI.
    """
    pass


@random_name.command()
@click.argument("name", default="random_name")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [random_name]
