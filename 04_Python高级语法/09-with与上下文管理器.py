class File(object):
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        print("entering...")
        self.f = open(self.file_name, self.mode)
        return self.f

    def __exit__(self, *args):
        print("will exit")
        self.f.close()

with File('out.txt', 'w') as f:
    print("writing")
    f.write('Hello, World!')
