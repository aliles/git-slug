========
git-slug
========

A code name for every Git commit.

*git-slug* deploys a new Git command that will generate a code name for each
and every commit derived from that commit's hash value.

------------
Installation
------------

*git-slug* will install from the `Python Package Index`_ on both Python2 and
Python3. It does however depend on `pygit2`_. This will require you to have
installed `libgit2`_ and `cffi`_. For further details on installing pygit2's
dependencies refer to `pygit2's installation instructions`_.

---
Use
---

Once installed, *git-slug* can be called either directly, or as Git's ``slug``
sub-command. For example::

    $ git slug

This will display each commit hash and generate cover name.

.. _Git: http://git-scm.com
.. _Pip: http://www.pip-installer.org
.. _Python Package Index: https://pypi.python.org/pypi
.. _cffi: http://cffi.readthedocs.org
.. _libgit2: https://libgit2.github.com
.. _pygit2: http://www.pygit2.org
.. _pygit2's installation instructions: http://www.pygit2.org/install.html
