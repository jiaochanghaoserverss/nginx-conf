from nginx_conf.uwsgi import Uwsgi
from nginx_conf.base_setting import BaseSetting


uwsgi_conf = {
    'service_dir': '/Users/jiaochanghao/gitee_clone/django-rest-framework/api',
    'conf_dir': 'conf',
    'virtualenv_dir': '/Users/jiaochanghao/.virtualenvs/api',
}

def main():
    base = BaseSetting(service_dir='', conf_dir='', virtualenv_dir='')
    gen_service = Uwsgi()
    uwsgi_file = gen_service.gen_uwsgi()
    print(uwsgi_file)


if __name__ == "__main__":
    main()
