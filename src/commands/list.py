import inquirer

from core import NoteMe


def ask_to_choose_hostname(note_me):
    list_site = note_me.list_hostname()
    questions = [
        inquirer.List(
            name='hostname',
            message='Choose list from hostname',
            choices=list_site,
        )
    ]

    answer = inquirer.prompt(questions).get('hostname')
    return answer


def ask_to_choose_action(note_me: NoteMe, hostname):
    list_links = note_me.get_links(hostname)
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
