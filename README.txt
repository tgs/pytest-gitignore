pytest-gitignore
================

This py.test plugin will tell py.test to ignore any file that git
ignores, when it's collecting tests.  For example, if you keep virtualenvs
in your source directory, you can have both git and py.test ignore them
by putting them in your .gitignore.  To see whether a file is ignored
by git, run `git check-ignore (filename)`.

This plugin is registered as 'gitignore'.
