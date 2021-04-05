# ipython - a better command shell

This talk is an introduction to `ipython`, which is a much nicer command shell than the default python shell. Presentation slides are here: <https://docs.google.com/presentation/d/1rI9iQT9OJHKL7wsaFqNkdGRwI32q3W3F0ojg6Df0Dcg/edit?usp=sharing>.

## Getting to the `ipython` shell

You have a few options:

1. The no install way: Click on [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/christine-e-smit/python-community/master?filepath=ipython). Once the interface finishes loading, click on New -> Terminal. Once the terminal comes up, type `ipython`.

2. The slightly harder way: install anaconda python, a python distribution that comes with ipython included. <https://docs.anaconda.com/anaconda/install/>. Once anaconda is installed and in your path, type `ipython`.

3. The hard core way: install ipython in your current python distribution. Generally, this will be `pip install ipython`. Once installed, type `ipython`.

## Tutorial instructions

1. Make sure you have a prompt that looks something like this. Note that your versions may be slightly different, but you should see the a prompt that says `In [1]:` rather than `>>>`.

    ```ipython
    Python 3.9.2 | packaged by conda-forge | (default, Feb 21 2021, 05:02:46) 
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.21.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]: 
    ```

1. Print "hello world": type `print("hello world")`

1. Clear the screen: type `clear`

1. Get the docstring for the `print` function: type `print?`

1. Execute an os shell command to list the current directory: type `!ls`

1. Be super lazy and don't even bother with the `!` for common os commands like `ls`: type `ls`

1. Take advantage of automatic indendation:

    ```ipython
    In [1]: def foo():
       ...:     print("foo!")
       ...:     print("baz!")
       ...: 
    ```

1. Exit `ipython` and start it up again. Hit the up arrow until you get the `foo` function definition from the previous session:

    ```ipython
    In [3]: exit
    $ ipython
    Python 3.9.2 | packaged by conda-forge | (default, Feb 21 2021, 05:02:46) 
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.21.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]: def foo():
       ...:     print("foo!")
       ...:     print("baz!")
    ```

1. Search through your command history for the last line that started `pr`: type `pr` at a new prompt and hit the up arrow.

1. Carelessly copy and paste a code snippet that still has the `ipython` prompt _or_ the `python` prompt and execute. Copy and paste: `>>> print("hello world")`

1. Read <https://ipython.readthedocs.io/en/stable/overview.html> for more!
