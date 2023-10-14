from nginx_conf.public import Public


def main():
    public = Public(service_dir='/Users/jiaochanghao/gitee_clone/django-rest-framework1/api',
                    conf_dir='conf', virtualenv_dir='/Users/jiaochanghao/.virtualenvs/api',
                    uwsgi_path='conf/uwsgi.ini')
    public.uwsgi.gen_uwsgi()
    public.nginx.gen_nginx()


if __name__ == "__main__":
    main()
