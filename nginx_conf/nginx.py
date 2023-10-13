from nginx_conf.base_setting import BaseSetting
from nginx_conf.utils import execute_command
from nginx_conf import const
from nginx_conf.error import MyNginxException


class Nginx(BaseSetting):

    def __init__(self, service_dir, uwsgi_path):
        super().__init__()
        nginx_conf_dir = f'{self.nginx_exists()}/{const.NginxConf.NGINX_OTHER}'
        service_name = self.get_service_name(service_dir)
        uwsgi_path = self.get_uwsgi_path(service_dir, uwsgi_path)
        nginx_parser = self.parser
        nginx_parser.add_argument("--nginx_host", type=str, help="nginx域名",
                                  default=const.NginxConf.NGINX_HOST)
        nginx_parser.add_argument("--nginx_port", type=int, default=const.NginxConf.NGINX_PORT)
        nginx_parser.add_argument("--uwsgi_port", type=int, default=const.UwsgiConf.UWSGI_PORT, help="uwsgi端口号")
        nginx_parser.add_argument("--nginx_conf_dir", type=str, default=nginx_conf_dir,
                                  help="nginx配置目录")
        nginx_parser.add_argument("--service_name", type=str, default=service_name,
                                  help="nginx配置文件名称/项目名称")
        nginx_parser.add_argument("--uwsgi_path", type=str, default=uwsgi_path,
                                  help="uwsgi.ini文件路径")

        nginx_parser.add_argument("--logs_dir", type=str, default=const.ProjectConf.LOGS, help="nginx日志目录")
        nginx_parser.add_argument("--static_dir", type=str, default=const.ProjectConf.STATIC, help="静态文件目录")
        nginx_parser.add_argument("--service_dir", type=str, default=service_dir, help="项目目录")

        self.nginx_args = self.args_func(nginx_parser)

    def gen_nginx(self):
        assert self.folder_exists(self.args.uwsgi_path), '生成uwsgi才可以生成nginx配置'
        assert self.args.nginx_host, "请设置nginx域名"
        nginx_file_path = self.nginx_conf_file
        nginx_file_path.write_text(f"""
server{{
  listen {self.args.uwsgi_port};
  server_name {self.args.nginx_host};
  access_log {self.logs_path}/nginx-access.log;
  error_log {self.logs_path}/nginx-error.log;
  location /static/ {{
    alias {self.static_path}/;
  }}

  location / {{
    if ($request_method ~* HEAD)
    {{
      return 200;
    }}
    include uwsgi_params;
    uwsgi_connect_timeout   10;
    uwsgi_send_timeout      600;
    uwsgi_read_timeout      600;
    uwsgi_pass 127.0.0.1:{self.args.uwsgi_port};
  }}
}}
""", encoding='utf8')
        return nginx_file_path

    def nginx_exists(self):
        returncode, result, _ = execute_command(f"which {const.NginxConf.NGINX}")
        if returncode == 0:
            return result
        else:
            raise MyNginxException('Nginx does not exist')

    def get_uwsgi_path(self, service_dir, uwsgi_path):
        return f"{service_dir}/{uwsgi_path}"

    def get_service_name(self, service_name):
        return service_name.split('/')[-1]
