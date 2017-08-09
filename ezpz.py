import socket
import click
import time
import random
import os

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
                reciever()
                #click.echo('\n\nFILE RECIEVED')
                #click.echo('\nb: back')
                #char = click.getchar()
                #if char == 'b':
                #    menu = 'main'
                #else:
                #    click.echo('Invalid input')
            elif char == '2':
                click.clear()
                printbanner()
                sender()
                click.pause
                #click.echo('\n\nFILE SENT!')
                #click.echo('\nb: back')
                #char = click.getchar()
                #if char == 'b':
                #    menu = 'main'
                #else:
                #    click.echo('Invalid input')
            elif char == '3':
                click.clear()
                printbanner()
                click.echo('INSTRUCTIONS:')
                click.echo("""
    1. Reciever selects menu option #2.
    2. Sender selects menu option #1.
    3. Sender chooses a file to send.
        """)
                click.echo('\nb: back')
                char = click.getchar()
                if char == 'b':
                    menu = 'main'
                else:
                    click.echo('Invalid input')
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


def sender():
    """THIS ACTS AS THE SERVER"""
    host = ''
    port = click.prompt(text='Choose a port between 10000-30000', default=1337, confirmation_prompt=True, show_default=True)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        click.echo('Setup done, waiting for connection..')
        conn, addr = s.accept()
        with conn:
            click.echo('%s connected to the server' % conn.getpeername)
            msg = conn.recv(1024)
            if not msg:
                click.echo('No message returned, exiting..')
                return
            else:
                click.echo(msg)
            click.pause()
            os._exit(1)

@cli.command()
def reciever():
    """THIS ACTS AS THE CLIENT"""
    printbanner()



if __name__ == '__main__':
    cli()
