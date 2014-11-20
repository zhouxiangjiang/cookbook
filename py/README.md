Python Cookbook
======

Setup Python environment:

```bash
python3 __init__.py install-python
```

## [The Zen of Python](http://legacy.python.org/dev/peps/pep-0020/ "PEP 20")

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

 - [PEP 8 - Style Guide for Python Code](http://legacy.python.org/dev/peps/pep-0008/)
 - [PEP 257 - Docstring Conventions](http://legacy.python.org/dev/peps/pep-0257/)
 
******

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

  
## References

  - Why I Love Python (2001)
  - [Think Python](http://www.greenteapress.com/thinkpython/html/index.html)
  - [Python 3 Documentation](https://docs.python.org/3/)
  - Core Python Programming, 2nd Edition (2009)
  - Core Python Applications Programming, 3rd Edition (2012)
  - Python Cookbook, 3rd Edition (2013)