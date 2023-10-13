from nginx_conf.nginx import Nginx

# 'nginx_conf_dir': '/opt/homebrew/etc/nginx',

uwsgi_path = 'conf/uwsgi.ini'
service_dir = '/Users/jiaochanghao/gitee_clone/django-rest-framework1/api'


def main():
    gen_service = Nginx(service_dir=service_dir, uwsgi_path=uwsgi_path)
    gen_service.gen_nginx()


if __name__ == "__main__":
    main()
