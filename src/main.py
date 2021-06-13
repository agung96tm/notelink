import click

from commands.list import ask_to_choose_hostname, ask_to_choose_action
from commands.search import ask_for_search_action
from core import NoteMe


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = NoteMe()


@cli.command()
@click.argument('link')
@click.pass_obj
def nsave(note_me: NoteMe, link: str):
    """ save link to site dict """
    note_me.save(link)


@cli.command()
@click.pass_obj
def nlist(note_me: NoteMe):
    hostname = ask_to_choose_hostname(note_me)

    if not note_me.is_empty_list_for(hostname):
        link_chosen, action = ask_to_choose_action(note_me, hostname)

        click.launch(link_chosen) if action == 'open_browser' \
            else note_me.remove_from_list(link_chosen)

    else:
        click.echo(f'link for hostname "{hostname}" is empty')


@cli.command()
@click.pass_obj
@click.argument('search')
def nsearch(note_me: NoteMe, search: str):
    list_links = note_me.search(search)
    if len(list_links) > 0:
        link_chosen, action = ask_for_search_action(list_links)

        click.launch(link_chosen) if action == 'open_browser' \
            else note_me.remove_from_list(link_chosen)


if __name__ == '__main__':
    cli()
