git-slug
==========

Skeleton template for Python projects.
Derived from my usual project structure
and `Kenneth Reitz <https://twitter.com/#!/kennethreitz>`_'s repository structure
`blog post <http://kennethreitz.com/repository-structure-and-python.html>`_.

Features
--------

In addition to the structure outlined in Kenneth's post,
git-slug has the following features:

* Apache Software License 2.0.
* Python `Distribute <http://packages.python.org/distribute/>`_ ready.
* Single point of control for version in ``git-slug.version.py``.
* ``load_rst()`` function in ``setup.py`` to load long description from docs.
* Prepare Sphinx documentation configuration including intersphinx.
* Populated MANIFEST.in including tests and documentation in packages.
* Empty change log.

Set Up
------

To unpack git-slug into clean repository. ::

    $ wget -O - https://github.com/aliles/git-slug/tarball/master | tar -s /aliles-git-slug-......././ -zx
    $ find . -type f -exec sed -i .bak 's/git-slug/NEWNAME/g' {} \;
    $ find . -type f -exec sed -i .bak 's/TestGitSlug/TestNEWNAME/g' {} \;
    $ find . -type f -name \*.bak -exec rm {} \;
    $ for ORIG in `find . -name \*git-slug\*`; do NEW=`echo $ORIG | sed s/git-slug/NEWNAME/`; mv $ORIG $NEW; done

This will replace all instances of ``git-slug``
with your new project name.
**You also need to edit
the README.rst 
and LICENSE files.**

The ``requirements.txt`` file has been populated
with dependencies for documentation,
static type analysis
and test coverage.
To install these dependencies
execute make's ``deps`` target. ::

    $ make deps

Make Targets
------------

The makefile has the following targets:

* ``deps``, install Python dependencies using ``pip``.
* ``docs``, build package documention using ``Sphinx``.
* ``lint``, static code analysis of package using ``flake8``.
* ``dist``, build source distribution for package.
* ``tests``, run unit tests using test runner from ``setup.py``.
* ``unittest``, run unit tests using ``unittest`` module test runner.
* ``coverage``, generate coverage report from test coverage.
* ``clean``, remove all build artifacts.
