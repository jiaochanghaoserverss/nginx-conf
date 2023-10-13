from nginx_conf.uwsgi import Uwsgi


uwsgi_conf = {
    'service_dir': '/Users/jiaochanghao/gitee_clone/django-rest-framework/api',
    'conf_dir': 'conf',
    'virtualenv_dir': '/Users/jiaochanghao/.virtualenvs/api',
}

def main():
    gen_service = Uwsgi(uwsgi_conf)
    uwsgi_file = gen_service.gen_uwsgi()
    print(uwsgi_file)


if __name__ == "__main__":
    main()
