def application(environ, start_trsponse):
    start_trsponse('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    return 'Hello World 我爱你中国。。。'
