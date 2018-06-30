#1.在dbbasic的基础上,对数据库操作的代码进行封装

import json


from os.path import join, dirname

import pymysql
import time

from os import remove
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler, UIModule

from day0308.util.dbutil import DBUtil


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):

        #CTRL + /
        # result = ''
        # msg = self.get_argument('msg',None)
        # if msg:
        #     result='用户名或密码错误'

        self.render('login.html')

    def post(self, *args, **kwargs):
        pass

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        #用户输入的用户名和密码
        username = self.get_argument('username')
        password = self.get_body_argument('password')

        #根据用户输入的用户名和密码到用户表中查询
        #如果有符合的数据记录,跳转到blog页面
        #否则说明用户名或密码错误,重新登录

        dbutil = DBUtil()
        if dbutil.isloginsuccess(username,password):
            self.redirect('/blog')
        else:
            self.redirect('/?msg=fail')

class BlogHandler(RequestHandler):
    def get(self, *args, **kwargs):

        self.render('blog.html')

    def post(self, *args, **kwargs):
        pass


class RegistHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('regist.html')
    def post(self, *args, **kwargs):
        #获取用户提交的注册信息
        #用户名,密码,城市,有可能有头像
        username = self.get_argument('username')
        password = self.get_argument('password')
        city = self.get_argument('city')
        if username and password and city:
            #判断用户是否上传了头像
            #avatar_file表示用户上传的头像文件
            #保存在服务器上的名称
            avatar_file = None
            files = self.request.files
            if files:#用户上传了头像文件
                avatar = files.get('avatar')[0]
                filename = str(time.time())+avatar['filename']#避免重名
                body = avatar['body']
                fw = open('mystatics/images/{}'.format(filename),'wb')
                fw.write(body)
                fw.close()
                avatar_file = filename

            dbutil = DBUtil()
            try:
                dbutil.saveuser(username=username,
                                password=password,
                                city=city,
                                avatar_file=avatar_file)
            except Exception as e:
                if avatar_file:
                    remove('mystatics/images/{}'.format(avatar_file))
                self.redirect('/regist?msg={}'.format(e))
            else:
                self.redirect('/')

        else:
            self.redirect('/regist?msg=empty')



class LoginModule(UIModule):
    def render(self, *args, **kwargs):
        # uri = path + ?query
        u =self.request.uri
        p = self.request.path
        q = self.request.query

        print('uri',u)
        print('path',p)
        print('query',q)

        result = ''
        if q:
           result = '用户名或密码错误'

        return self.render_string('mymodule/login_module.html',result=result)


class BlogModule(UIModule):
    def render(self, *args, **kwargs):
        return self.render_string('mymodule/blog_module.html',blogs=[{
          'title':'女王节快乐',
            'tag':['女人','购物'],
            'content':'买买买,随便花,哈哈哈',
            'comment':8,
            'author':'大旭旭',
            'avatar':'a.jpg'
        },{
            'title': '晚饭吃啥好',
            'tag': ['情感', '文艺','家庭'],
            'content': '宫保鸡丁,鱼香肉丝,红烧排骨,一碗米饭',
            'comment': 0,
            'author': '冯华的小号',
            'avatar':None
        },{
            'title': '今天下课早',
            'tag': ['达内', 'python','学习'],
            'content': '今天又学习了好多东西,呵呵',
            'comment': 2,
            'author': '王伟奇',
            'avatar':None
        }])


class RegistModule(UIModule):
    def render(self, *args, **kwargs):

        result = ''
        q = self.request.query
        #msg=empty
        #msg=duplicate
        print('query', q)
        #msg = q.split('=')[1]
        #msg = q[4:]
        msg = q[q.find('=')+1:]
        if msg=='empty':
            result = '请输入完整'
        if msg=='duplicate':
            result = '用户名重复'

        return self.render_string('mymodule/regist_module.html',result=result)

define('port',type=int,default=8888)
parse_config_file('config/config')

app = Application([('/',IndexHandler),('/login',LoginHandler),('/blog',BlogHandler),('/regist',RegistHandler)],
                  template_path=join(dirname(__file__),'mytemplate'),
                  ui_modules={'loginmodule':LoginModule,'blogmodule':BlogModule,'registmodule':RegistModule},
                  static_path='mystatics')
server = HTTPServer(app)
server.listen(options.port)
IOLoop().current().start()



