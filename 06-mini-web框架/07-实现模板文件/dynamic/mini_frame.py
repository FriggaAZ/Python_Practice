def index():
    # 注意这个路径！！！
    with open("./templates/index.html") as f:
        return f.read()


def center():
    with open("./templates/center.html") as f:
        return f.read()


def application(env, start_trsponse):
    file_name = env['PATH_INFO']
    start_trsponse('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    if file_name == '/index.py':
        return index()
    elif file_name == '/center.py':
        return center()
    else:
        return 'Hello World 我爱你中国。。。'
