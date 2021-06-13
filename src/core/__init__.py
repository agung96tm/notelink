from urllib.parse import urlparse
import configobj
from configs import config as main_config


class NoteMe:
    def __init__(self, config=None):
        self.config = config or main_config

    def save(self, link):
        link_parsed = urlparse(link)
        hostname = link_parsed.hostname

        if hostname not in self.config['URL_SAVED'].keys():
            self.config['URL_SAVED'][hostname] = []

        list_urls = self.config['URL_SAVED'][hostname]
        list_urls.append(link) if link not in list_urls else None
        self.config.write()

    def search(self, value):
        list_links = []
        for hostname in self.config['URL_SAVED']:
            for link in self.config['URL_SAVED'][hostname]:
                if value in link:
                    list_links.append(link)
        return list_links

    def list_hostname(self):
        return self.config['URL_SAVED'].keys()

    def get_links(self, hostname):
        link = []
        if hostname in self.config['URL_SAVED'].keys():
            link = self.config['URL_SAVED'][hostname]
        return link

    def is_empty_list_for(self, hostname):
        if hostname not in self.config['URL_SAVED'].keys():
            self.config['URL_SAVED'][hostname] = []
        return len(self.config['URL_SAVED'][hostname]) < 1

    def remove_from_list(self, link):
        link_parsed = urlparse(link)
        hostname = link_parsed.hostname

        if hostname not in self.config['URL_SAVED'].keys():
            self.config['URL_SAVED'][hostname] = []

        self.config['URL_SAVED'][hostname].remove(link)
        self.config.write()
