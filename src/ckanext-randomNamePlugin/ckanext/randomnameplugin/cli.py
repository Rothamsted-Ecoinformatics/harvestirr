import click


@click.group(short_help="randomnameplugin CLI.")
def randomnameplugin():
    """randomnameplugin CLI.
    """
    pass


@randomnameplugin.command()
@click.argument("name", default="randomnameplugin")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [randomnameplugin]
