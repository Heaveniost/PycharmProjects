#1.返回JSON格式字符串
#2.返回模板
#2.1 模板中嵌入变量{{变量}},数学表达式{{a+b}}
#    函数表达式{{' '.join([x,y,z])}}
#2.2 模板中嵌入语句 {%for blog in blogs%}...{%end%}
#    {%if blog['comment']%} xxx
#    {%else%}
#    {%end%}
#2.3 把各个模板中相同的内容可以提取为基础模板(块技术),
#    基础模板中体现各个模板的共同部分,但要利用{%block%}...{%end%}
#    来体现各个模板不同的部分,常见的title部分,head部分,body部分
#2.4 通过模块的提取,可以在不同的模板中复用这些模块,
#    减少重复代码的编写
#3. 静态资源的使用
#3.1 在Application中声明存放静态资源的文件夹
#    static_path = 'mystatics'
#3.2 在使用静态资源时,要写成static/xxx/xxxx资源 (static是tornado关键字)
#    tornado会根据3.1中static_path参数值更换static

import json


from os.path import join, dirname
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler, UIModule


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

        self.render('blog.html')

    def post(self, *args, **kwargs):
        pass


class RegistHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('regist.html')
    def post(self, *args, **kwargs):
        pass


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
        return self.render_string('mymodule/login_module.html',result='')

define('port',type=int,default=8888)
parse_config_file('config/config')

app = Application([('/',IndexHandler),('/login',LoginHandler),('/blog',BlogHandler),('/regist',RegistHandler)],
                  template_path=join(dirname(__file__),'mytemplate'),
                  ui_modules={'loginmodule':LoginModule,'blogmodule':BlogModule,'registmodule':RegistModule},
                  static_path='mystatics')
server = HTTPServer(app)
server.listen(options.port)
IOLoop().current().start()



