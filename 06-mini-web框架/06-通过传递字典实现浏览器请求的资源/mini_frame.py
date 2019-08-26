def index():
    return "这是主页"


def login():
    return "这是登录"


def application(env, start_trsponse):
    file_name = env['PATH_INFO']
    start_trsponse('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    if file_name == '/index.py':
        return index()
    elif file_name == '/login.py':
        return login()
    else:
        return 'Hello World 我爱你中国。。。'
