from nginx.nginx import Nginx


nginx_conf = {
    'nginx_host': '127.0.0.1',
    'nginx_port': 12000,
    'nginx_conf_dir': '/opt/homebrew/etc/nginx_conf',
    'service_name': 'api',
    'uwsgi_path': '/Users/jiaochanghao/gitee_clone/django-rest-framework/api/conf/uwsgi.ini',
    'service_dir': '/Users/jiaochanghao/gitee_clone/django-rest-framework/api',
    'logs_dir': 'logs',
    'uwsgi_port': 11000,
    'static_dir': 'static',
}

def main():
    gen_service = Nginx(nginx_conf)
    gen_service.gen_nginx()


if __name__ == "__main__":
    main()
