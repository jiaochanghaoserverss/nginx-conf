from nginx_conf.nginx import Nginx
from nginx_conf.uwsgi import Uwsgi


class Public:

    def __init__(self, *args, **kwargs):
        self.nginx = Nginx(*args, **kwargs)
        self.uwsgi = Uwsgi(*args, **kwargs)
