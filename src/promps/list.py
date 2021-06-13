import inquirer

from src.core import NoteMe


def ask_to_choose_hostname(note_me, reverse=None):
    list_sites = note_me.list_hostname()

    if reverse:
        list_sites.sort(reverse=reverse)

    questions = [
        inquirer.List(
            name='hostname',
            message='Choose list from hostname',
            choices=list_sites,
        )
    ]

    answer = inquirer.prompt(questions).get('hostname') if len(list_sites) > 0 else None
    return answer


def ask_to_choose_action(note_me: NoteMe, hostname, reverse=None):
    list_links = note_me.get_links(hostname)

    if reverse:
        list_links.sort(reverse=reverse)

    questions = [
        inquirer.List(
            name='link_chosen',
            message='Choose link',
            choices=list_links,
        ),
        inquirer.List(
            name='action',
            message='What action do you want',
            choices=['open_browser', 'remove']
        )
    ]
    answers = inquirer.prompt(questions)
    return answers['link_chosen'], answers['action']


def ask_to_choose_hostname_with_action(note_me: NoteMe, reverse=None):
    list_hostname = note_me.list_hostname()

    if reverse:
        list_hostname.sort(reverse=reverse)

    if len(list_hostname) == 0:
        return None, None

    questions = [
        inquirer.List(
            name='hostname',
            message='Choose Host',
            choices=list_hostname,
        ),
        inquirer.List(
            name='action',
            message='What action do you want',
            choices=['open_browser', 'remove']
        )
    ]
    answers = inquirer.prompt(questions)
    return answers['hostname'], answers['action']
