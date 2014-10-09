#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package py
Python Cookbook

  - Unit Testing
  - doctest
  - Loop Techniques
  - Output Format
  - Context Manager
  - Memory-Mapped File
  - Find & Sort Algorithms
  - Text Pattern
  - Network
  - Thread
  - Django (Web framework)
  

## Command Line Options

    `-t`  Issue a warning when a source file mixes tabs and spaces for indentation in a way that
          makes it depend on the worth of a tab expressed in spaces.
        
    `-tt` Issue a error when a source file mixes tabs and spaces for indentation in a way that
          makes it depend on the worth of a tab expressed in spaces.
        
    `-O`  Turn on basic optimizations. This changes the file name extension for compiled (bytecode)
          files from *.pyc* to *.pyo*, and set the `__debug__` to `False`.
       
    `-OO` Discard docstrings in addition to the <em>-O</em> optimizations.
    

## The Zen of Python

> Beautiful is better than ugly.
>
> Explicit is better than implicit.
>
> Simple is better than complex.
>
> Complex is better than complicated.
>
> Flat is better than nested.
>
> Sparse is better than dense.
>
> Readability counts.
>
> Special cases aren't special enough to break the rules.
>
> Although practicality beats purity.
>
> Errors should never pass silently.
>
> Unless explicitly silenced.
>
> In the face of ambiguity, refuse the temptation to guess.
>
> There should be one-- and preferably only one --obvious way to do it.
>
> Although that way may not be obvious at first unless you're Dutch.
>
> Now is better than never.
>
> Although never is often better than *right* now.
>
> If the implementation is hard to explain, it's a bad idea.
>
> If the implementation is easy to explain, it may be a good idea.
>
> Namespaces are one honking great idea -- let's do more of those!

    
## Python Coding Style

- Use 4-space indentation, and avoid tabs. ( `-t` option )

- Limit lines to a maximum of *100* characters, and docstrings/comments to *80*.

- Separate top-level function and class definitions with two blank lines, and
  method definitions inside a class are separated by a single blank line.

- Code should always use **UTF-8**.

- When possible, put comments on a line of their own.

- Always make a priority of keeping the comments up-to-date when the code
  changes!

- Using docstrings.

- Use spaces around operators and after commas, but not directly inside
  bracketing constructs. eg. `a = f(a, b)`

- Name your classes and functions consistently; the convention is to use
  `CamelCase` for classes and `lower_case_with_underscores` for functions and
  methods.

- Avoid using underscores to begin variable, function or class names.

> Generally, a variable name `_xxx` is considered "private" and should not be
> used outside that module or class. It's good practice to use `_xxx` to
> denote when a variable is private. Since variables named `__xxx__` often
> mean special things to Python, you should avoid using naming normal
> variables this way.

- Avoid recalculation of the same value.

- Avoid numeric indexing.

- Avoid numeric constants.

> You should name the constants, since it's much easier to read the code and
> therefore easier to get right and to modify later.

- Don't use fancy encodings if your code is meant to be used in international
  environments. Plain **ASCII** works best in any case.

- Absolute imports are recommended, as they are usually more readable and tend
  to be better behaved (or at least give better error messages) if the import
  system is incorrectly configured.

- Imports should usually be on separate lines.

- Module ordering for import statements.

> It is recommended that all module imports happen at the top of Python
> modules. Futhermore, imports should follow this ordering:
>
>      - Standard Library Modules
>      - Third-Party Modules
>      - Application-Specific Modules
>
> Seperate these groups with an empty line between the imports of these three
> types of modules.

- Restrict wildcard imports ( `from module import *` ).

> In practice, using `from module import *` is considered poor style because
> it "pollutes" the current namespace and has the potential of overriding
> names in the current namespace; however, it is extremely convenient if a
> module has many variables that are often accessed, or if the module has a
> very long name.

- Keep user interaction outside of functions.

> The functions should be kept "clean", meaning they shoule silently be used
> purely to take parameters and provide return values. More importantly, it is
> good practice to seperate functions into two categories: those that do
> things (i.e., interactive with users or set variables) and those that
> calculate things (usually returning results).

- Easier to ask for forgiveness than permission (EAFP).

> This common Python coding style assumes the existence of valid keys or
> attributes and catches exceptions if the assumption proves false. This clean
> and fast style is characterized by the presence of many `try` and `except`
> statements. The technique contrasts with the **LBYL** style common to many
> other languages such as C.
>
>     LBYL = (L)ook (B)efore (Y)ou (L)eap:
>
> This coding style explicitly tests for pre-conditions before making calls or
> lookups. This style contrasts with the EAFP approach and is characterized by
> the presence of many if statements.
>
> In a multi-threaded environment, the **LBYL** approach can risk introducing
> a race condition between “the looking” and “the leaping”. For example, the
> code, if key in mapping: return mapping[key] can fail if another thread
> removes key from mapping after the test, but before the lookup. This issue
> can be solved with locks or by using the **EAFP** approach.

- Use local variables to subtitute for module attributes.

> Names like `os.linesep` require the interpreter to do two lookups: 1) lookup
> `os` to find that it is a module, and 2) loopup the `linesep` attribute of
> that module. Because modules are also global variables, we pay another
> penalty. If you use an attribute like this oftern in a function, it's
> recommended that you alias it to a single local variable. Lookups are much
> faster -- local variables are always searched first before globals, and no
> attribute needs to be lookuped either. This is one of the tricks in making
> your program faster: replace often-used (and name-lengthy) module attributes
> with local references, your code runs fasters and has less clutter with a
> shorter name.


## Virtual Running Environment

```bash
# Create
sudo apt-get install python-virtualenv
virtualenv env-dir
cd env-dir

# Active
source bin/activate
```

## Function Annotations (Python 3 Only)
    
    The Python interpreter does not attach any semantic meaning to the attached
    annotations. They are not type checks, nor do they make Python behave any
    differently than it did before. However, they might give useful hints to
    others reading the source code about what you had in mind. Third-party
    tools and frameworks might also attach semantic meaning to the annotations.
    
    Although you can attach any kind of object to a function as an annotation
    (e.g., numbers, strings, instances, etc.), classes or strings often seem to
    make the most sense.
    
    Function annotations are merely stored in a function’s `__annotations__`
    attribute.
    
    For example:

        def f(x:int, y:int) --> int:
            return x + y


## PEP

  - [PEP 20 -- The Zen of Python](http://legacy.python.org/dev/peps/pep-0020/)
  - [PEP 8 - Style Guide for Python Code](http://legacy.python.org/dev/peps/pep-0008/)
  - [PEP 257 - Docstring Conventions](http://legacy.python.org/dev/peps/pep-0257/)
  - [PEP 0343 - The with Statement](http://www.python.org/dev/peps/pep-0343/)
  

## References

  - [Think Python](http://www.greenteapress.com/thinkpython/html/index.html)
  - [Python 2 Documentation](https://docs.python.org/2/)
  - [Python 3 Documentation](https://docs.python.org/3/)
  - [Django](https://www.djangoproject.com/)
  
      
Copyright (c) 2014 Li Yun <leven.cn@gmail.com>
All Rights Reserved.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
'''

def unpack_iterable():
    '''Unpack N elements from iterables.
    
    It works with sequences, tuples, strings, files, iterators, and generators.
    '''
    seq = [1, 2, 3, 4, 5]
    v1, v2, v3, v4, v5 = seq

    # Skip some elements
    v1, _, v3, _, v5 = seq

    # Too many elements
    try:
        v1, v2, v3 = seq
    except ValueError as err:
        # print(err): too many values to unpack

        # Python 3 "star expressions" can be used to address this problem.
        v1, *v2, v3 = seq
        assert isinstance(v2, list)

        # Python 2.7 star parameters in function can be a replacement.
        #def unpack3(v1, v2, *v3):
        #    return v1, v2, v3
        #v1, v2, v3 = unpack3(*seq)
        #assert isinstance(v3 ,tuple)

    # Too many variables
    try:
        v1, v2, v3, v4, v5, v6 = seq
    except ValueError as err:
        # print(err): need more than 5 values to unpack
        pass
        
        
def file_io(filename):
    '''File I/O.
    
    By reading and writing only large chunks of data even when the user asks for
    a single byte, **buffered I/O** is designed to hide any inefficiency in
    calling and executing the operating system’s unbuffered I/O routines. The
    gain will vary very much depending on the OS and the kind of I/O which is
    performed (for example, on some contemporary OSes such as Linux, unbuffered
    disk I/O can be as fast as buffered I/O). The bottom line, however, is that
    buffered I/O will offer you predictable performance regardless of the
    platform and the backing device. Therefore, _it is most always preferable to
    use buffered I/O rather than unbuffered I/O_.
    
    The I/O system is built from layers. Text files are constructed by adding a
    text encoding/decoding layer on top of a buffered binary-mode file. The
    `buffer` attribute simply points at this underlying file. If you access it,
    you’ll bypass the text encoding/decoding layer. You could write raw bytes to
    a file opened in text mode using this technique.
    '''
    # Text I/O
    try:
        with open(filename) as f:
            for line in f:
                print(line)
    except IOError as err:
        print(err)
        
    # Read fixed-size data directly into buffer without intermediate copying.
    #
    # Unlike `read()` method, `readinto()` method doesn't need to allocate new
    # objects and return them, avoiding making extra memory allocations.
    import functools
    size = 2
    buf = bytearray(size)
    try:
        with open(filename, 'rb') as f:
            for nbytes in iter(functools.partial(f.readinto, buf), 0):
                print(nbytes, buf)
    except IOError as err:
        print(err)
        
    # Read var-size binary file.
    try:
        with open(filename, 'rb') as f:
            print(f.read(2))
            print(f.read(6))
    except IOError as err:
        print(err)
        

def func_default_value(arg, L:list=None):
    '''Default Values of Function Arguments.

    The default values are evaluated at the point of function definition in
    the defining scope only once.

    **NOTE**: When the default is a mutable object such as a list, dictionary,
    or instances of most classes, and if you don't want the default to be
    shared between subsequent calls, you can write the function like this
    instead.
    '''
    if L is None:
        L = []
    L.append(arg)
    return L
    
    
def func_unpack_args(arg1, arg2):
    '''Unpack arguments from dictionary, tuple, or list.
    
    From dictionary,
    
        mydict = {'arg1': 1, 'arg2': 2}
        func_unpack_args(**mydict)
    
    From tuple or list,
    
        mytuple = ("a", "b")
        func_unpack_args(*mytuple)
    
    '''
    pass
    
    
def func_vargs(arg, other='o', *vargs, **args):
    '''Variable Length Arguments List of Function.

    1. `*vargs` must be before `**args`.

    2. Any formal parameters which occur after the `*vargs` parameter are
       keyword-only arguments, meaning that they can only be used as keywords
       rather than positional arguments.

    '''
    # All parameters of `vargs` argument will be wrapped up in a tuple
    for param in vargs:
        # handle `*vargs`
        pass

    # All parameters of `args` argument will be wrapped up in an OrderedDict
    # class
    for key, value in args.items():
        # handle `**args`
        pass

    
class A(object):
    '''A class.
    
    # Built-in Class Attributes:
    - __name__   : string name of class
    - __doc__    : documentation string
    - __bases__  : tuple of class's base classes
    - __slots__  : list of attribute names (reduce memory)
    
    # Built-in Instance Attributes:
    - __doc__    : documentation string
    - __class__  : class for instance
    - __module__ : module where class is defined
    
    # Built-in Methods:
    - __init__() : constructor
    - __str__()  : string representation, str(obj)
    - __len__()  : length, len(obj)
    
        # Context Manager
        - __enter__()
        - __exit__()
    
        # Iterator
        - __iter__()
        - __next__()
        - __reversed__()
    
    '''

    # Python does not provide any internal mechanism track how many instances
    # of a class have been created or to keep tabs on what they are. The best
    # way is to keep track of the number of instances using a class attribute.
    num_of_instances = 0

    def __init__(self, a1=None, a2=None):
        A.num_of_instances += 1
        self.public_instance_attribute = a1
        self.private_instance_attribute = a2
        

    def public_instance_method(self):
        return (A.num_of_instances,
                self.publuc_instance_attribute,
                self.private_instance_attribute)
                
    
    def _private_instance_method(self):
        pass
        

    @staticmethod
    def static_method():
        return A.num_of_instances
        

    @classmethod
    def class_method(cls):
        return cls.__name__
        
        
class B(A):
    '''Subclass of A.    
    '''

    def __init__(self, b, a1=None, a2=None):
        super(B, self).__init__(a1, a2)
        self.b = b
        
        
    def public_instance_method(self):
        print('Override method of {0}'.format(self.__class__.__bases__[0]))
        
        
    def new_method(self):
        print('New method without inheritance from {0}'
                .format(self.__class__.__bases__[0]))    
    

if __name__ == '__main__':
    print('Hello Python!')
    
    unpack_iterable()
    
    assert isinstance(A(), A)
    assert issubclass(B, A)
