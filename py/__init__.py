#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package py
Python Cookbook

  - Testing
  - Memory-Mapped File
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

        def f(x:int, y:int) -> int:
            return x + y


## PEP

  - [PEP 20 -- The Zen of Python](http://legacy.python.org/dev/peps/pep-0020/)
  - [PEP 8 - Style Guide for Python Code](http://legacy.python.org/dev/peps/pep-0008/)
  - [PEP 257 - Docstring Conventions](http://legacy.python.org/dev/peps/pep-0257/)
  - [PEP 440 - Version Identification and Dependency Specification](http://legacy.python.org/dev/peps/pep-0440/)
  

## References

  - Why I Love Python (2001)
  - [Think Python](http://www.greenteapress.com/thinkpython/html/index.html)
  - [Python 3 Documentation](https://docs.python.org/3/)
  - Core Python Programming, 2nd Edition (2009)
  - Core Python Applications Programming, 3rd Edition (2012)
  - Python Cookbook, 3rd Edition (2013)
  
      
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

def loop():
    '''Loop technique.
    
    Case 1: To change a sequence you are iterating over while inside the loop
    (for example to duplicate certain items), it is recommended that you first
    make a copy.
    
        assert isinstance(words, list)
        for word in words[:]:  # Loop over a slice copy of the entire list.
            if len(word) > 6:
                words.insert(0, word)
            
    Case 2: Loop over dictionaries.
    
        assert isinstance(mydict, dict)
        for key, value in mydict.items(): # Python 2: mydict.iteritems()
            pass
    
    @see enumerate()
    @see zip()
    @see itertools
    '''
    seq = [1, 2, 3]
    seq2 = ['a', 'b']
    start_index = 1
    seq_tmp = []
    
    # enumerate()
    for index, value in enumerate(seq):
        assert index in range(len(seq))
        assert seq[index] == value
    for index, value in enumerate(seq, start=start_index):
        assert index-start_index in range(len(seq))
        assert seq[index-start_index] == value
        
    # Multiple containers simultaneously.
    #
    # zip(), itertools.zip_longest()
    # Python 2: itertools.izip_longest()
    for value1, value2 in zip(seq, seq2):
        assert value1 in seq
        assert value2 in seq2
        assert seq.index(value1) == seq2.index(value2)
    import itertools
    for value1, value2 in itertools.zip_longest(seq, seq2):
        assert value1 in seq
        if value2 not in seq2:
            assert value2 is None and seq.index(value1) == len(seq) - 1
    fillvalue = 0
    for value1, value2 in itertools.zip_longest(seq, seq2, fillvalue=fillvalue):
        assert value1 in seq
        if value2 not in seq2:
            assert value2 is fillvalue and seq.index(value1) == len(seq) - 1
        
    # itertools.chain()
    #
    # Join multiple containers with avoiding nested loops without losing the
    # readability of the code.
    #
    # Reference implementation of `chain()`:
    #
    #     def chain(iterators):
    #         for i in iterators:
    #             yield from i
    #
    for item in itertools.chain(seq, seq2):
        assert item in seq or item in seq2
        
    def my_generator(n):
        '''Generator

        Python’s _generators_ provide a convenient way to implement the
        _iterator_ protocol. If a container object’s `__iter__()` method is
        implemented as a _generator_, it will automatically return an _iterator_
        object (technically, a _generator_ object) supplying the `__iter__()`
        and `next()` methods.
        
        Replace infinitive while loop with an iterator:

            while True:
                a = get()
                if a == b:
                    break
            set(a)
        
                ||
                \/
        
            for a in iter(lambda: get(), b):
                set(a)

        The `yield` keyword could be implemented by _iterators_.
        
            # My iterator.
            #
            # Python supports a concept of iteration over containers. This is
            # implemented using two distinct methods (`__iter__()`, and
            # `next()`); these are used to allow user-defined classes to support
            # iteration.
            class MyIterator(object):
        
                def __init__(self, seq):
                    self._container = seq
                    self._index = -1
        
                def __iter__(self):
                    return iter(self._container)
    
                def __next__(self):
                    if self._index == len(self._container) - 1:
                        raise StopIteration
                    self._index += 1
                    return self._container[self._index]
            
                def __reversed__(self):
                    pass
        
        '''
        while True:
            yield n
            n += 1
    container = []
    for i in my_generator(0):
        if len(container) == 3:
            break
        container.append(i)
    assert container == [0, 1, 2]
    assert type(my_generator).__name__ == 'function'
    assert type(my_generator(10)).__name__ == 'generator'
    import types
    assert isinstance(my_generator, types.FunctionType)
    assert isinstance(my_generator(10), types.GeneratorType)
    
    # Iterator/Generator Slicing
    #
    # **NOTE**: It’s important to emphasize that `islice()` will consume data
    # on the supplied iterator. Since iterators can’t be rewound, that is
    # something to consider. If it’s important to go back, you should probably
    # just turn the data into a list first.
    for item in itertools.islice(my_generator(0), 5, 9):
        assert item in [5 ,6 ,7, 8]
        
    # Permutations & Combinations
    for item in itertools.permutations(seq):
        assert item in (
            (1, 2, 3),
            (1, 3, 2),
            (2, 1, 3),
            (2, 3, 1),
            (3, 1, 2),
            (3, 2, 1)
        )
    for item in itertools.permutations(seq, 2):
        assert item in (
            (1, 2),
            (1, 3),
            (2, 1),
            (2, 3),
            (3, 1),
            (3, 2)
        )
    for item in itertools.combinations(seq, 3):
        assert item in (
            (1, 2, 3),
        )
    for item in itertools.combinations(seq, 2):
        assert item in (
            (1, 2),
            (1, 3),
            (2, 3)
        )
    for item in itertools.combinations_with_replacement(seq, 3):
        assert item in (
            (1, 1, 1),
            (1, 1, 2),
            (1, 1, 3),
            (1, 2, 2),
            (1, 2, 3),
            (1, 3, 3),
            (2, 2, 2),
            (2, 2, 3),
            (2, 3, 3),
            (3, 3, 3)
        )
        
    # The easiest way to filter a sequence data is often to use a list (or
    # dictionary, tuple, etc.) comprehension.
    l = [1, 3, 5, -2, 0, 8]
    assert [i for i in l if i > 0] == [1, 3, 5, 8]
    assert [i if i > 0 else 0 for i in l] == [1, 3, 5, 0, 0, 8]
    d = {'A': 1, 'B': 2, 'C': 3}
    assert {key: value for key, value in d.items() if value > 1} == \
            {'B': 2, 'C': 3}  # Python 2: d.iteritems()
            
    # One potential downside of using a list comprehension is that it might
    # produce a large result if the original input is large. If this is a
    # concern, generator expression could be used to produce the filtered
    # values iteratively.
    for i in (i for i in l if i > 0):
        pass
        
    # Sometimes, the filtering criteria cannot be easily expressed in a list
    # comprehension or generator expression. For example, suppose that the
    # filtering process involves exception handling or some other complicated
    # detail.
    #
    # NOTE: the `filter()` returns a list in python 2, and an iterable in
    # Python 3.
    def is_int(val):
        try:
            int(val)
            return True
        except ValueError:
            return False
    assert list(filter(is_int, ['1', '-', '2', 'N/A', '-'])) == ['1', '2']

        
def float_format():
    '''Float number formatting.
    
    @see format()
    '''
    f = 12345.678
    assert format(f, '0.2f') == '12345.68' # two-digits accuracy
    assert format(f, '>10.2f') == '  12345.68' # right justified
    assert format(f, '<10.2f') == '12345.68  ' # left justified
    assert format(f, '^10.2f') == ' 12345.68 ' # centred
    assert format(f, ',') == '12,345.678' # thousands separator
    assert format(f, '0,.2f') == '12,345.68' # # thousands separator
    assert format(f, 'e') == '1.234568e+04' # exponential notation
    assert format(f, '0.2E') == '1.23E+04' # exponential notation
    
    
def int_format():
    '''int type formatting.
    
    @see format()
    @see bin()
    @see hex()
    @see oct()
    '''
    i = 2
    assert bin(i) == '0b10' == format(i, '#b') # binary prefix
    assert format(i, 'b') == '10' # binary digit
    assert format(i, '08b') == '00000010' # binary padding
    assert format(i, '#010b') == '0b00000010' # binary prefix & padding
    
    assert hex(i) == '0x2' == format(i, '#x') # hex prefix
    assert format(i, 'x') == '2' # hex digit
    assert format(i, '02x') == '02' # hex padding
    assert format(i, '#04x') == '0x02' # hex prefix & padding
    
    assert oct(i) == '0o2' == format(i, '#o') # Python 2: oct(i) == '02'
    assert format(i, 'o') == '2' # hex digit
    assert format(i, '03o') == '002' # hex padding
    assert format(i, '#05o') == '0o002' # hex prefix & padding
    
    
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
        assert str(err) == 'too many values to unpack (expected 3)'

        # "star expressions" in Python 3
        v1, *v2, v3 = seq
        assert isinstance(v2, list)

    # Too many variables
    try:
        v1, v2, v3, v4, v5, v6 = seq
    except ValueError as err:
        assert str(err) == 'need more than 5 values to unpack'
        
        
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
                
                
def context_manager():
    '''Context Manager.
    
    Python’s `with` statement supports the concept of a runtime context defined
    by a _context manager_. This is implemented using two separate methods
    (`__enter__()`, and `__exit__()`) that allow user-defined classes to define
    a runtime context that is entered before the statement body is executed and
    exited when the statement ends.
    
    @see http://www.python.org/dev/peps/pep-0343/
    @see contextlib
    '''
    # contextlib.suppress(*exception)
    #
    # Replace `try-except-pass`:
    #
    #     try:
    #         os.remove('not-exists')
    #     except FileNotFoundError:
    #         pass
    #
    # **NOTE**: This context manager is *reentrant*.
    # @since Python 3.4
    from contextlib import suppress
    import os
    with suppress(FileNotFoundError):
        os.remove('not-exists')
                
        
    from contextlib import contextmanager
    @contextmanager
    def closing(thing):
        '''Reference implementation of contextlib.closing().
        
        @see contextlib#closing()
        '''
        try:
            yield thing
        finally:
            thing.close()
            
            
    # contextlib.ExitStack
    #
    # Replace `try-finally`:
    #
    #     cleanup_needed = True
    #     def do():
    #         return False
    #     def cleanup():
    #         pass
    #     try:
    #         result = do()
    #         if result:
    #             cleanup_needed = False
    #     finally:
    #         if cleanup_needed:
    #             cleanup()
    #
    # @since Python 3.3
    from contextlib import ExitStack
    def do():
        return False
    def cleanup():
        pass
    with ExitStack() as stack:
        stack.callback(cleanup)
        result = do()
        if result:
            stack.pop_all()
            
            
    # contextlib.ContextDecorator
    #
    # Replace:
    #
    #     class MyContextManager(object):
    #         def __init__(self):
    #             # initialization here ...
    #             # if error, raise Exception.
    #             pass
    #
    #        
    #         def close(self):
    #             # clearing context here ...
    #             pass
    #
    #
    #         def do(self):
    #             # do something here ...
    #             # if error, raise Exception.
    #             pass
    #
    #     
    #         def __enter__(self):
    #            return self
    #
    # 
    #         def __exit__(self, etype, evalue, traceback):
    #            if etype is not None:
    #                print(etype, evalue, traceback)
    #                self.close()
    #
    # @since Python 3.2
    from contextlib import ContextDecorator
    stack = []
    class mycontext(ContextDecorator):
        def __enter__(self):
            stack.append('Enter')
            return self
        def __exit__(self, *exc): # etype, evalue, traceback
            stack.append('Exit')
            return False
    @mycontext()
    def mycontextfunc():
        stack.append('Do')
    mycontextfunc()
    assert stack == ['Enter', 'Do', 'Exit']
            
            
    # contextlib.redirect_stdout(new_file)
    #
    # **NOTE**: This context manager is *reusable* but *not reentrant*.
    # @since Python 3.4
    from contextlib import redirect_stdout
    import io
    f = io.StringIO()
    with redirect_stdout(f):
        help(io)
    s = f.getvalue()
    
    
def re_pattern():
    '''Regular Expression (RE) pattern.
    
    re1|re2 - or
    re1.re2 - any character except `\n`
    ^str - start of string
    str$ - end of string
    re* - 0+ occurrences
    re+ - 1+ occurrences
    re? - 0 or 1 occurrences
    re{N} - N occurrences
    re{M,N} - from M to N occurrences
    [...] - any single character from character set
    [x-y] - any single character from x to y
    [^...] - NOT any character from character set
    (...) - subgroup
    
    \d - digit, `[0-9]`
    \D - NOT digit, `[^0-9]`
    \w - alphanumeric character, `[A-Za-z0-9_]`
    \W - NOT alphanumeric character, `[^A-Za-z0-9_]`
    \s - white space, `[ \n\t\r\v\f]`
    \S - NOT white space, `[^ \n\t\r\v\f]`
    \bword\b - word boundary
    \A - ^
    \Z - $
    
    @see re    
    '''
    import re
    
    # Compile pattern object
    pattern = re.compile(r'patern-string')
    
    # Get match object
    match = pattern.match('string')          # Search from beginning
    match = pattern.search('string')         # Search until end

    # Get match object list with scanning the whole string
    match_list = pattern.findall('string')

    # Loop over a iterator with scanning the whole string
    for match in pattern.finditer('string'): 
        # handle match
        pass
    
    # Handle match object
    if match is not None:          # Match found
        result = match.group()     # string
        pos_start = match.start()  # int
        pos_end = match.end()      # int
        pos = match.span()         # tuple: (pos_start, pos_end)
    else:
        # Not match
        pass
    
    # Search and replace with strings
    # repl_tuple = (repl_str, count)
    repl_str = pattern.sub('replacement', 'origin', count=0)
    repl_tuple = pattern.subn('replacement', 'origin', count=0)
    
    # Search and replace with strings returned by functions
    def repl_func(match_obj):
        if match_obj.group() == 'something':
            return 'string 1'
        else:
            return 'string 2'
    repl_str = pattern.sub(repl_func, 'string', count=0)
    repl_tuple = pattern.subn(repl_func, 'string', count=0)    

    # Split strings on any of multiple delimiters
    #
    # **NOTE**: When using `re.split()`, you need to be a bit careful should
    # the regular expression pattern involve a capture group enclosed in
    # parentheses. If capture groups are used, then the matched text is also
    # included in the result.
    s = 'a b; cd, efg,hijkl,     mn'
    assert re.split(r'[;,\s]\s*', s) == ['a','b','cd','efg','hijkl','mn']
    assert re.split(r'(;|,|\s)\s*', s) == \
            ['a',' ','b',';','cd',',','efg',',','hijkl',',','mn']
    assert re.split(r'(?:;|,|\s)\s*', s) == ['a','b','cd','efg','hijkl','mn']
    
    
def shell_pattern():
    '''Shell-style wildcards pattern matching.
    
    Pattern | Meaning
    ---------------------------------------------
    *       | matches everything
    ---------------------------------------------
    ?       | matches any single character
    ---------------------------------------------
    [seq]   | matches any character in _seq_
    ---------------------------------------------
    [!seq]  | matches any character not in _seq_
    ---------------------------------------------
    
    For a literal match, wrap the meta-characters in brackets. Note that the
    filename separator ('/' on Unix) is not special to `fnmatch` module.
    
    Unlike `fnmatch.fnmatch()`, `glob` module treats file names beginning with
    a dot (.) as special cases.
    
    **NOTE**: The matching performed by `fnmatch` module sits somewhere
    between the functionality of simple string methods, such as
    `startswith()`, `endswith()`, and the full power of regular expressions.
    If you're just trying to provide a simple mechanism for allowing wildcards
    in data processing operations, it's often a reasonable solution.
    '''
    import fnmatch
    #import glob
    import os
    
    assert fnmatch.fnmatch('aaa.txt', '*.txt') == True
    assert fnmatch.fnmatch('aaa.txt', '?aa.txt') == True

    if os.name == 'posix': # On POSIX
        assert fnmatch.fnmatch('aaa.txt', '*.TXT') == False
    elif os.name == 'nt': # On Windows
        assert fnmatch.fnmatch('aaa.txt', '*.TXT') == True
        
    # Both POSIX and Windows (Case-insensitive)
    assert fnmatch.fnmatchcase('aaa.txt', '*.TXT') == False
    
    # Filter
    assert fnmatch.filter(['a.txt','b.txt', 'c.log'], '*.txt') == \
            ['a.txt','b.txt']
            
            
def sort_algorithm():
    '''Sort Algorithms.
    
    The reference implementation of `operator.itemgetter()`:

        def itemgetter(*items):
            if len(items) == 1:
                item = items[0]
                def g(obj):
                    return obj[item]
            else:
                def g(obj):
                    return tuple(obj[item] for item in items)
            return g
            
    The reference implementation of `operator.attrgetter()`:

        def attrgetter(*items):
            if len(items) == 1:
                attr = items[0]
                def g(obj):
                    return resolve_attr(obj, attr)
            else:
                def g(obj):
                    return tuple(resolve_attr(obj, attr) for attr in items)
            return g
        def resolve_attr(obj, attr):
            for name in attr.split("."):
                obj = getattr(obj, name)
            return obj
        
    @see sorted()
    @see operator.itemgetter()
    @see operator.attrgetter()
    '''
    import operator

    d = [
        {'name': 'b', 'value': 3},
        {'name': 'a', 'value': 2},
        {'name': 'c', 'value': 1}
    ]

    # Sort a list of dictionaries by name
    assert sorted(d, key=operator.itemgetter('name')) == [
        {'name': 'a', 'value': 2},
        {'name': 'b', 'value': 3},
        {'name': 'c', 'value': 1}
    ]

    # Sort a list of dictionaries by value
    assert sorted(d, key=operator.itemgetter('value')) == [
        {'name': 'c', 'value': 1},
        {'name': 'a', 'value': 2},
        {'name': 'b', 'value': 3}
    ]

    # Sort a list of dictionaries by two keys
    d = [
        {'name': 'b', 'v': 3, 'v2': 2},
        {'name': 'a', 'v': 3, 'v2': 1},
        {'name': 'c', 'v': 2, 'v2': 3}
    ]

    assert sorted(d, key=operator.itemgetter('v', 'v2')) == [
        {'name': 'c', 'v': 2, 'v2': 3},
        {'name': 'a', 'v': 3, 'v2': 1},
        {'name': 'b', 'v': 3, 'v2': 2}
    ]

    # Sort objects without native comparison support 
    class App:
        def __init__(self, id):
            self.id = id
    apps = [App(1), App(2), App(3)]
    assert sorted(apps, key=operator.attrgetter('id'))
    
    
def search_algorithm():
    '''Find the largest or smallest N items in a collection.

    **NOTE**: If you are looking for the _N_ smallest or largest items, and _N_
    is small compared to the overall size of the collection, the `nsmallest()`
    and `nlargest()` methods of `heapq` module provide superior performance.

    For larger _N_, it is more efficient to use the `sorted()` function first,
    and take a slice. Also, when `N==1`, it is more efficient to use the
    built-in `min()` and `max()` functions.

    **NOTE**: When doing these calculations, be aware that `zip()` creates an
    iterator that can only consumed once.
    '''
    import heapq

    # Find in a list of integers
    seq = [1, 8, 2, 23, 7, -2, 18, 23, 42, 37, 2]
    assert heapq.nlargest(3, seq) == [42, 37, 23]
    assert heapq.nsmallest(3, seq) == [-2, 1, 2]

    # Find in a list of dictionaries
    list_of_dict = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.74},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name':'ACME', 'shares': 75, 'price': 115.65}
    ]
    assert heapq.nsmallest(3, list_of_dict, key=lambda s: s['price']) == [
            {'name': 'YHOO', 'shares': 45, 'price': 16.35},
            {'name': 'FB', 'shares': 200, 'price': 21.09},
            {'name': 'HPQ', 'shares': 35, 'price': 31.74}
        ]
            
    # Find in a dictionary
    d = {
        'IBM': 91.1,
        'AAPL': 543.22,
        'FB': 21.09
    }
    assert min(zip(d.values(), d.keys())) == (21.09, 'FB')
    assert max(zip(d.values(), d.keys())) == (543.22, 'AAPL')

    # Order a list as a heap, transformed in-place, in linear time
    heapq.heapify(seq)

    # Pop and return the smallest item from the heap, maintaining the heap
    # invariant.
    try:
        assert heapq.heappop(seq) == -2
    except IndexError as e:
        # Heap is empty
        pass
    

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 1 and sys.argv[1] == 'install-python':
        # Install Python 3
        import subprocess
        subprocess.check_call('sudo apt-get update', shell=True)
        subprocess.check_call('sudo apt-get install \
                python3 python3-pip python3-dev build-essential', shell=True)
        subprocess.check_call('sudo pip3 install --upgrade virtualenv',
                shell=True)
    print('Hello Python!')
    
    # Loop technique
    loop()
    
    # Formatting Output
    float_format()
    int_format()
    
    unpack_iterable()
    
    assert isinstance(A(), A)
    assert issubclass(B, A)
    
    context_manager()
    
    # Text Pattern
    re_pattern()
    shell_pattern()
    
    # Sort & Search Algorithms
    sort_algorithm()
    search_algorithm()
