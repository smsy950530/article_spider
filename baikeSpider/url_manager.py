class urlManger():
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self,url):
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        self.new_url = self.new_urls.pop()
        self.old_urls.add(self.new_url)
        return self.new_url

    def add_new_urls(self, new_urls):
        if len(new_urls) == 0 or new_urls is None:
            return
        else:
            for new_url in new_urls:
                self.add_new_url(new_url)