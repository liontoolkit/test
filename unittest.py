from nose.tools import with_setup
from MyModule import MyModule

count = 0

def setup_module():
    print('<<<Setup Module>>>')

def teardown_module():
    print('<<<Teardown Module>>>')

def setup_function():
    print('<<<Setup Function>>>')
    global count
    count = 1

def teardown_function():
    print('<<<Teardown Function>>>')
    global count
    count = 0

@with_setup(setup_function, teardown_function)
def test_function():
    print('<<<Test function>>>')
    global count
    assert count == 1

@with_setup(setup_function, teardown_function)
def test_generator():
    print('<<<Test generator>>>')
    for i in range(5):
        yield generator_function, 2, i

def setup_generator_function():
    print('<<<Setup generator_function>>>')

def teardown_generator_function():
    print('<<<Teardown generator_function>>>')

@with_setup(setup_generator_function, teardown_generator_function)
def generator_function(step,i):
    print('<<<generator_function {}>>>'.format(i+1))
    global count
    count = count + step
    assert count == 1 + step*(i+1)

class TestMyModule:
    @classmethod
    def setup_class(cls):
        print('<<<Setup Class>>>')
        cls.obj = MyModule()
    
    @classmethod
    def teardown_class(cls):
        print('<<<Teardown Class>>>')
        del cls.obj
    
    def setup(self):
        print('<<<Setup Method>>>')
        self.obj = self.__class__.obj

    def teardown(self):
        print('<<<Teardown Method>>>')
        self.obj = None
    
    def test___init__(self):
        print('<<<Test __init__>>>')
        assert self.obj.number1 == 1
        assert self.obj.number2 == 2

    def test_my_function(self):
        print('<<<Test my_function>>>')
        assert self.obj.my_function() == self.obj.number1 + self.obj.number2
        assert self.obj.my_function(3,4) == 7
        assert self.obj.my_function(num1=5) == 5 + self.obj.number2
        assert self.obj.my_function(num2=3) == self.obj.number1 + 3
        assert self.obj.my_function(10,-5) == 5
        assert self.obj.my_function(-10,-5) == -15
