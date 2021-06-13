import inquirer


def ask_for_search_action(list_links=None):
    list_links = list_links or []

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
