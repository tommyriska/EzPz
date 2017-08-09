import socket
import click
import time
import random
import os
import json
import io
from pathlib import Path
import ntpath

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

            # Recieve a file
            if char == '1':
                click.clear()
                printbanner()
                reciever()
                click.echo('\n\nFILE RECIEVED')
                click.echo('\nb: back')
                char = click.getchar()
                if char == 'b':
                    menu = 'main'
                else:
                    click.echo('Invalid input')

            # Send a file
            elif char == '2':
                click.clear()
                printbanner()
                sender()

                #click.echo('\n\nFILE SENT!')
                #click.echo('\nb: back')
                #char = click.getchar()
                #if char == 'b':
                #    menu = 'main'
                #else:
                #    click.echo('Invalid input')

            # Instructions
            elif char == '3':
                click.clear()
                printbanner()
                click.echo('INSTRUCTIONS:')
                click.echo("""
    1. Reciever selects menu option #2.
    2. Sender selects menu option #1.
    3. Sender chooses a file to send.

    Important! All files will currently be saved in users home directory.
               More configurations will come later.
        """)
                click.echo('\nb: back')
                char = click.getchar()
                if char == 'b':
                    menu = 'main'
                else:
                    click.echo('Invalid input')

            # Configuration
            elif char == '4':
                click.clear()
                printbanner()

                with open('config.json', 'r') as f:
                    config = json.load(f)
                    click.echo(json.dumps(config))

                char = click.getchar()
                if char == 'b':
                    menu == 'main'

            # About section
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
            elif char == '6':
                downloadpath = Path.home()
                filename = 'fissa.txt'
                joinedpath = Path.joinpath(downloadpath, filename)
                click.echo(joinedpath)
                char = click.getchar()
                if char == 'b':
                    menu = 'main'
                else:
                    click.echo('Invalid input')
            # Quit
            elif char == 'q':
                click.clear()
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
    port = click.prompt(text='Choose a port between 10000-30000', default=1337, show_default=True)

    # File configurations
    filesize = ''
    filepath = click.prompt(text='File to send')
    if os.path.isfile(filepath):
        filesize = os.path.getsize(filepath)
        if not filesize:
            click.echo('ERROR!!! NO DATA FOUND')
        else:
            click.echo(type(filesize))
            click.echo(filesize)
        filename = ntpath.basename(filepath)
        if not filename:
            click.echo('ERROR!!! NO FILENAME FOUND')
        else:
            click.echo(type(filename))
            click.echo(filename)
        click.echo('File to send: ' + str(filename))

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((host, port))
            s.listen(3000)
            click.echo('Setup done, waiting for connection..')
            conn, addr = s.accept()
            with conn:
                connip = str(conn.getpeername())
                click.echo('%s connected.' % connip)
                click.echo('Sending metadata.')
                filesize = bytes(str(filesize), 'utf-8')
                conn.sendall(filesize)
                response = conn.recv(32)
                response = response.decode('utf-8')
                click.echo('RESPONSE: ' + response)
                if response == 'Filesize recieved':
                    filename = bytes(filename, 'utf-8')
                    conn.sendall(filename)
                    response = conn.recv(32)
                    response = response.decode('utf-8')
                    click.echo('RESPONSE: ' + response)
                    if response == 'Filename recieved':
                        click.echo('Metadata successfully sent!')
                        click.echo('Starting filetransfer.')
                        with open(filepath, 'rb') as f:
                            conn.sendfile(file=f)
                            click.echo('Download complete!')
                            click.echo('Click M to go back to menu.')
                            char = click.getchar()
                            if char == 'm':
                                menu = 'main'
                            else:
                                click.echo('Invalid input')
                    else:
                        click.echo('NO FILENAME RESPONSE')
                else:
                    click.echo('NO FILESIZE RESPONSE')
                    conn.shutdown(socket.SHUT_RDWR)

def reciever():
    """THIS ACTS AS THE CLIENT"""
    click.clear()
    printbanner()
    host = click.prompt(text='Choose what IP to connect to', default='localhost')
    port = int(click.prompt(text='Choose what port to connect to'))
    downloadpath = Path.home()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        click.echo('Connected to ' + host + ' at port: ' + str(port))
        click.echo('Retrieving metadata')
        filesize = s.recv(20)
        s.sendall(b'Filesize recieved')
        filesize = filesize.decode('utf-8')
        click.echo(filesize)
        filename = s.recv(20)
        s.sendall(b'Filename recieved')
        filename = filename.decode('utf-8')
        click.echo('\n\nFilesize: ' + filesize)
        click.echo('\n\nFilename: ' + filename)
        click.echo('Recieving file...')
        fullpath = Path.joinpath(downloadpath, filename)
        with open('FUCKMEINTHEASS', 'wb') as f:
            data = s.recv(1024)
            totaldata = len(data)
            f.write(data)
            while totaldata < float(filesize):
                data = s.recv(1024)
                totaldata += len(data)
                f.write(data)
                print('{0:.2f}'.format((totaldata/float(filesize))*100)+ '%'+ ' done')
        click.echo('Download is complete')
        click.echo('Click M to go back to menu')
        char = click.getchar()
        if char == 'm':
            s.shutdown(socket.SHUT_RDWR)
            menu = 'main'
    else:
        click.echo('Invalid input')

if __name__ == '__main__':
    cli()
