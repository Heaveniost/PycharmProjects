# 孙伟
# bjsunwei@tedu.cn
#1.最基本的服务器实现
#  ALT+ENTER万能提示快捷键
#2.利用配置文件设置端口号
#  2.1 定义端口号
#  2.2 从配置文件中读取端口号
#  2.3 使用端口号
#3.获取从客户端提交的各种参数
#  3.1 获取客户端以get/post形式发起请求时携带的参数
#  3.2 客户端上传文件


from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):

        login_html='<form method=post action=/login enctype=multipart/form-data>' \
                   '用户名:<input type=text name=username><br>' \
                   '密码:<input type=password name=password><br>' \
                   '<input type=file name=avatar><br>' \
                   '<input type=submit value=登录>&nbsp;&nbsp;' \
                   '<input type=reset value=重置>' \
                   '</form>'

        login_html_fail = '<form method=post action=/login>' \
                   '用户名:<input type=text name=username><br>' \
                   '密码:<input type=password name=password><br>' \
                   '<span style=color:red;font-weight:bolder;>用户名或密码错误</span><br>' \
                   '<input type=submit value=登录>&nbsp;&nbsp;' \
                   '<input type=reset value=重置>' \
                   '</form>'


        #self.write('hello tornado')
        #self.write(login_html)

        msg = self.get_argument('msg',None)

        if msg=='fail':
            self.write(login_html_fail)
        else:
            self.write(login_html)

    def post(self, *args, **kwargs):
        pass

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        #用户输入的用户名和密码
        username = self.get_argument('username')
        password = self.get_body_argument('password')

        #如果用户名是abc,密码是123
        if username=='abc' and password=='123':
            #如果用户有上传文件,将文件保存
            files = self.request.files
            if files:
                avatars = files.get('avatar')
                avatar = avatars[0]
                body = avatar['body']
                writer = open('upload/{}'.format(avatar['filename']),'wb')
                writer.write(body)
                writer.close()


            self.redirect('/blog')
        else:
            self.redirect('/?msg=fail')


class BlogHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('blog页面')
    def post(self, *args, **kwargs):
        pass


define('port',type=int,default=8888)
parse_config_file('config/config')

app = Application([('/',IndexHandler),('/login',LoginHandler),('/blog',BlogHandler)])
server = HTTPServer(app)
server.listen(options.port)
IOLoop().current().start()



