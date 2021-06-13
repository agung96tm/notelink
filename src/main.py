from typing import Union, List

import click

from commands.list import ask_to_choose_hostname, ask_to_choose_action, ask_to_choose_list_hostname
from commands.search import ask_for_search_action
from core import NoteMe
from core import helpers


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = NoteMe()


@cli.command()
@click.argument('link', nargs=-1)
@click.pass_obj
def nsave(note_me: NoteMe, link: Union[str, List[str]]):
    note_me.bulk_save(link)


@cli.command()
@click.pass_obj
@click.option('--list-host', is_flag=True)
@click.option('--reverse/--no-reverse', default=False)
def nlist(note_me: NoteMe, list_host: bool, reverse: bool):
    if list_host:
        link_chosen, action = ask_to_choose_list_hostname(note_me, reverse)
        helpers.helper_for_hostname_action(note_me=note_me, link_chosen=link_chosen, action=action)

    else:
        hostname = ask_to_choose_hostname(note_me, reverse)

        if note_me.is_list_empty_for(hostname):
            if hostname:
                click.echo(f'link for hostname "{hostname}" is empty')
            else:
                click.echo(f'hostname is empty')
            return

        link_chosen, action = ask_to_choose_action(note_me, hostname)
        helpers.helper_for_action(note_me=note_me, link_chosen=link_chosen, action=action)


@cli.command()
@click.pass_obj
@click.argument('search', type=str)
@click.option('-l', '--limit', type=int)
@click.option('-h', '--hostname', type=str)
def nsearch(note_me: NoteMe, search: str, limit: int, hostname: str) -> None:
    list_links = note_me.search(search_value=search, limit=limit, hostname=hostname)

    if len(list_links) == 0:
        click.echo('Your search did found')
        return

    link_chosen, action = ask_for_search_action(list_links)
    helpers.helper_for_action(note_me=note_me, link_chosen=link_chosen, action=action)


if __name__ == '__main__':
    cli()
