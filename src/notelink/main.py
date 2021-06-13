from typing import Union, List

import click

from notelink.promps.list import (
    ask_to_choose_hostname,
    ask_to_choose_action,
    ask_to_choose_hostname_with_action,
)
from notelink.promps.search import ask_for_search_action
from notelink.core import NoteMe, ensure_config
from notelink.core import helpers


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = NoteMe()
    ensure_config(ctx.obj.config)


@cli.command()
@click.argument('link', nargs=-1)
@click.pass_obj
def nsave(note_me: NoteMe, link: Union[str, List[str]]) -> None:
    note_me.bulk_save(link)


@cli.command()
@click.option('--list-host', is_flag=True)
@click.option('--reverse/--no-reverse', default=False)
@click.option('-h', '--hostname', type=str)
@click.pass_obj
def nlist(note_me: NoteMe, list_host: bool, reverse: bool, hostname: str) -> None:
    if list_host:
        link_chosen, action = ask_to_choose_hostname_with_action(note_me, reverse)
        if not link_chosen:
            click.echo(f'hostname is empty')
            return

        helpers.helper_for_hostname_action(note_me=note_me, link_chosen=link_chosen, action=action)

    else:
        hostname_ = ask_to_choose_hostname(note_me, reverse) if not hostname else hostname

        if note_me.is_empty_list_for(hostname_):
            if hostname_:
                click.echo(f'link for hostname "{hostname_}" is empty')
            else:
                click.echo(f'hostname is empty')
            return

        link_chosen, action = ask_to_choose_action(note_me, hostname_)
        helpers.helper_for_action(note_me=note_me, link_chosen=link_chosen, action=action)


@cli.command()
@click.argument('search', type=str)
@click.option('-l', '--limit', type=int)
@click.option('-h', '--hostname', type=str)
@click.pass_obj
def nsearch(note_me: NoteMe, search: str, limit: int, hostname: str) -> None:
    list_links = note_me.search(search_value=search, limit=limit, hostname=hostname)

    if len(list_links) == 0:
        click.echo('Your search did found')
        return

    link_chosen, action = ask_for_search_action(list_links)
    helpers.helper_for_action(note_me=note_me, link_chosen=link_chosen, action=action)


if __name__ == '__main__':
    cli()
