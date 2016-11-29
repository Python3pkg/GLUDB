# Developing for GLUDB

## General Dev guidelines

Since everyone has space preferences, here's ours:

````
Indentation is 4 spaces. No tabs. No trailing whitespace.
````

We reserve the right to reformat pull requests not following this guideline.
Don't say we didn't warn you :)

For style, format, and linted code, we:

* Follow PEP 8
* Expect the PyFlakes lint tool to provide no warnings
* Expect Ned Batchelder's McCabe script to provide no warnings

The best way to conform to the above is to use Flake8, which combines warnings
from all three.

## Testing

Please see our [testing document](testing.md)

## Creating a new backend

We load backends dynamically from the modules in the package `gludb.backends`.
The easiest way to create a new backend is to clone an existing backend and
update it to suit your purposes. If you are writing a backend for a relational
database, you can refer to either `sqlite.py` or `postgresql.py`.

## Documentation

Please see the "Making a release" section below for the actual steps in
involved in creating documentation for a release (including our API documents)

We maintain this documentation in Markdown format in the docs directory. It
ReadTheDocs provides hosting (and styling and markdown conversion). The
current markdown conversion method is mkdocs (see `mkdocs.yml` in the root of
this project).

The [API document](api.md) is a pointer to HTML documents we generate with the
handy pdoc. Instead of calling pdoc directly, you should use our helper script
`docs/make_docs.sh` with the api command:

```
user@workstation:~/gludb$ docs/make_docs.sh api
```

If you want to see what the documentation looks like, then you can use the
document script with the 'serve' command: `docs/make_docs.sh serve`. To
include the latest docstrings, you might want to combine the 'api' and 'serve'
commands:

```
$ ./docs/make_docs.sh api
$ ./docs/make_docs.sh serve
```

## Making a release

Making a release is simple, but is a multi-step process:

1. Ensure that you have checked everything in, merged in to the master branch,
   and tested.
2. Update the version number in setup.py - be sure that you're following the
   version numbering guidelines from
   [PEP 440](https://www.python.org/dev/peps/pep-0440/)
3. Make sure that there is a matching entry in the [release notes](relnotes.md)
4. Make sure that the [API documentation](api.md) is up to date by running
   `docs/make_docs.sh api`. You can also get an idea of what the current
   documentation will look like by running `docs/make_docs.sh serve`
5. Build and deploy to PyPI by running `./build.sh`. Note that you'll need to
   install some tools, including pandoc. You'll also need a PyPI account
   that has the correct rights to deploy gludb.
6. Assuming that everything goes OK, you add, commit, tag, and push to GitHub.

Assuming that the version number is 1.1.1 and you've already updated files as
per steps 2 and 3, then steps 4 and following would like this:

````
user@GLUDB:~/gludb $ docs/make_docs.sh api
user@GLUDB:~/gludb $ ./build.sh
user@GLUDB:~/gludb $ git add -A
user@GLUDB:~/gludb $ git commit -m "release 1.1.1"
user@GLUDB:~/gludb $ git tag -a -m "tagging 1.1.1" v1.1.1
user@GLUDB:~/gludb $ git push --all
user@GLUDB:~/gludb $ git push --tags
````

## Top-level directory contents

Some newcomers might find the top-level directory for a little overwhelming.
Here's a complete breakdown of what you see here (in alphabetical order):

* .gitignore - This lists files that will be automatically ignored by git
* .travis.yml - The configuration file use by Travis CI (our continuous
  integration provider)
* build - Created when you use ./build.sh (in .gitignore)
* build.sh - A script to build distributions of the gludb library suitable for
  use by others (and upload to PyPI)
* dev-requirements.txt - Requirements install into a virtualenv used
  for development on gludb. Mainly used by our testing scripts
* dev-requirements-27.txt - Development requirements specific to Python 2.7.
  This is necessary because we support Google Cloud Datastore on Python
  2.7 and not 3.4
* dist - Holds the final output of the ./build.sh command (in .gitignore)
* docs - Our documentation in mkdocs format (which is one of the two formats
  used by ReadTheDocs.io)
* examples - Simple examples for gludb use
* gludb - Our actual package info
* gludb.egg-info - Created as part of a process developing the gludb package
* LICENSE - The license for the contents of this repository
* mkdocs.yml - The configuration file for the documentation in the docs
  directory
* README.md - This file
* setup.cfg - Parameters used by setup.py
* setup.py - The main setup file for the gludb package - used by ./build.sh and
  other sources for install, remove, etc
* tests - Location for our unit tests
