from nginx.uwsgi import Uwsgi


uwsgi_conf = {
    'uwsgi_port': 11000,
    'conf_dir': 'conf',
    'service_dir': '/Users/jiaochanghao/gitee_clone/django-rest-framework/api',
    'gen_uwsgi': True,
    'logs_dir': 'logs',
    'virtualenv_dir': '/Users/jiaochanghao/.virtualenvs/api',
}

def main():
    gen_service = Uwsgi(uwsgi_conf)
    uwsgi_file = gen_service.gen_uwsgi()
    print(uwsgi_file)


if __name__ == "__main__":
    main()
