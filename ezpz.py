import socket
import click
import time
import random
import os
import json
import io

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
            click.echo('    4. Settings')
            click.echo('    5. About')
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
                if checkconfig() == True:
                    with open('config.json', 'r') as f:
                        config = json.load(f)
                    click.echo(config)

            elif char == '5':
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

def checkconfig():
    if os.path.isfile('config.json') and os.access('config.json', os.R_OK):
        return True
    else:
        click.echo('No configuration file found. Creating one.')
        currentdir = os.getcwd()
        click.echo('CURRENT DIR:' + currentdir)
        with io.open(os.path.join(currentdir, 'config.json'), 'w') as db_file:
            db_file.write(json.dumps({"name":"Tommers"}))
        click.echo('New configuration file was created. Please restart the program now.')
        click.pause(info='Press any key to quit ...')
        os._exit(1)
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
    # Socket configurations
    host = ''
    port = click.prompt(text='Choose a port between 10000-30000', default=1337, confirmation_prompt=True, show_default=True)

    # File configurations
    filesize = ''
    filename = click.prompt(text='File to send:')
    if os.path.isfile(filename):
        filesize = os.path.getsize(filename)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen(1)
            click.echo('Setup done, waiting for connection..')
            conn, addr = s.accept()
            with conn:
                click.echo(conn.getpeername, 'connected.')
                click.echo('Sending over metadata.')
                conn.sendall(filesize)
                click.echo('Metadata successfully sent!')
                click.echo('Starting filetransfer.')
                with open(filename, 'rb') as f:
                    bytestosend = f.read(1024)
                    conn.sendall(bytestosend)
                    while bytestosend != '':
                        bytestosend = f.read(1024)
                        conn.sendall(bytestosend)

@cli.command()
def reciever():
    """THIS ACTS AS THE CLIENT"""
    printbanner()
    host = click.prompt(text='Choose what IP to connect to:')
    port = click.prompt(text='Choose what port to connect to:')




if __name__ == '__main__':
    cli()
