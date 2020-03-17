import click

@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo('Hello from me!')

@cli.command()
def goodbye():
    click.echo('Goodbye from me!')
