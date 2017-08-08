import socket
import click

@click.group()
def cli():
    pass

@cli.command()
def menu():
    menu = 'main'
    while True:
        if menu == 'main':
            click.clear()
            printbanner()
            click.echo('\nMain menu:')
            click.echo('    1. Recieve a file')
            click.echo('    2. Send a file')
            click.echo('    3. Instructions')
            click.echo('    4. About')
            click.echo('    q. Quit')
            click.echo('\n    Version 0.0.1')
            click.echo('    By Tommy Riska')
            char = click.getchar()
            if char == '1':
                click.clear()
                printbanner()
                click.echo('\n\nFILE RECIEVED')
                click.echo('\nb: back')
                char = click.getchar()
                if char == 'b':
                    menu = 'main'
                else:
                    click.echo('Invalid input')
            elif char == '2':
                click.clear()
                printbanner()
                click.echo('\n\nFILE SENT!')
                char = click.getchar()
                if char == 'b':
                    menu = 'main'
                else:
                    click.echo('Invalid input')
            elif char == '3':
                click.clear()
                printbanner()
            elif char == '4':
                click.clear()
                printbanner()
                click.echo('ABOUT EzPz:\n\n')
                click.echo('Made by Tommy Riska')
                click.echo('Version 0.0.1')
                click.echo('\nb: back')
                char = click.getchar()
                if char == 'b':
                    menu = 'main'
                else:
                    click.echo('Invalid input')
            elif char == 'q':
                return

def printbanner():
    click.echo(click.style("""
_________________________________________________________________________
|                     _______     _____                                 |
|                    |  ____|   |  __  |                                |
|                    | |__   ___| |__) |___                             |
|                    |  __| |_  /  ___/_  /                             |
|                    | |____ / /| |    / /                              |
|                    |______/___|_|   /___|                             |
|_______________________________________________________________________|""",fg='green', bg='black'))

@cli.command()
def sender():
    """THIS ACTS AS THE SERVER"""

@cli.command()
def reciever():
    """THIS ACTS AS THE CLIENT"""
if __name__ == '__main__':
    cli()
