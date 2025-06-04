import click


@click.group(short_help="random CLI.")
def random():
    """random CLI.
    """
    pass


@random.command()
@click.argument("name", default="random")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [random]
