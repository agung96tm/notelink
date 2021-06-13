from typing import Union, List
from urllib.parse import urlparse
from src.configs import config as main_config


URL_SAVED_NAME = 'URL_SAVED'


def get_hostname_from_url(url):
    return urlparse(url).hostname


def ensure_config_hostname(config, hostname):
    """
    Ensure doesnt make any error
    when hostname configure want to be filled
    """
    if hostname and hostname not in config[URL_SAVED_NAME].keys():
        config[URL_SAVED_NAME][hostname] = []


class NoteMe:
    def __init__(self, config=None):
        self.config = config or main_config

    def save(self, link):
        hostname = get_hostname_from_url(link)
        ensure_config_hostname(self.config, hostname=hostname)

        list_urls = self.config[URL_SAVED_NAME][hostname]
        list_urls.append(link) if link not in list_urls else None
        self.config.write()

    def bulk_save(self, links: Union[str, List[str]]):
        for link in links:
            self.save(link)

    def search(self, search_value, limit=None, hostname=None):
        search_hostnames = [
            h for h in self.config['URL_SAVED'] if h == hostname
        ] if hostname else self.config['URL_SAVED']

        list_links = []
        for hostname in search_hostnames:
            for link in self.config['URL_SAVED'][hostname]:
                if search_value in link:
                    list_links.append(link)

        return list_links[:limit] if isinstance(limit, int) else list_links

    def list_hostname(self):
        return self.config['URL_SAVED'].keys()

    def get_links(self, hostname):
        link = []
        if hostname in self.config['URL_SAVED'].keys():
            link = self.config['URL_SAVED'][hostname]
        return link

    def is_empty_list_for(self, hostname):
        ensure_config_hostname(config=self.config, hostname=hostname)
        return len(self.config['URL_SAVED'][hostname]) < 1 if hostname else True

    def remove_link(self, link):
        hostname = get_hostname_from_url(link)
        ensure_config_hostname(config=self.config, hostname=hostname)
        self.config['URL_SAVED'][hostname].remove(link)
        self.config.write()

    def remove_hostname(self, hostname):
        del self.config['URL_SAVED'][hostname]
        self.config.write()
