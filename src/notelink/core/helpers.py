import click

from notelink.core import NoteMe


OPEN_BROWSER = 'open_browser'
REMOVE = 'remove'


def helper_for_action(note_me: NoteMe, link_chosen: str, action: str) -> None:
    if action.lower() == OPEN_BROWSER:
        click.launch(link_chosen)
    elif action.lower() == REMOVE:
        note_me.remove_link(link_chosen)


def helper_for_hostname_action(note_me: NoteMe, link_chosen: str, action: str) -> None:
    if action.lower() == OPEN_BROWSER:
        click.launch('https://' + link_chosen)
    elif action.lower() == REMOVE:
        note_me.remove_hostname(link_chosen)
