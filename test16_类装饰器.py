class Foo(object):
    def __init__(self):
        pass

    def __call__(self, func):
        def _call(*args, **kw):
            print('class decorator runing')
            return func(*args, **kw)

        return _call


class Bar(object):
    @Foo()
    def bar(self):
        print("bar")


Bar().bar()