from urllib.parse import urlparse
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

    def bulk_save(self, links):
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

    def is_list_empty_for(self, hostname):
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

    def remove_hostname(self, hostname):
        del self.config['URL_SAVED'][hostname]
        self.config.write()
