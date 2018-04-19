=============
tox-envreport
=============

.. image:: https://img.shields.io/pypi/v/tox-envreport.svg
    :target: https://pypi.org/project/tox-envreport
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/tox-envreport.svg
    :target: https://pypi.org/project/tox-envreport
    :alt: Python versions

.. image:: https://travis-ci.org/useblocks/tox-envreport.svg?branch=master
    :target: https://travis-ci.org/useblocks/tox-envreport
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/useblocks/tox-envreport?branch=master
    :target: https://ci.appveyor.com/project/useblocks/tox-envreport/branch/master
    :alt: See Build Status on AppVeyor

`tox-envreport` is a plugin for `tox <https://tox.readthedocs.io/en/latest/>`_
to document the setup of used virtual environments.

Collected information are stored in a file called ``env_report.json`` inside the `.tox` folder.
For example: ``MY_PROJECT/.tox/env_report.json``.

Installation
------------
``pip install tox-envreport``

Usage
-----

The installation of the plugin is enough to automatically activate it for each tox run.

There is nothing more to do or to configure.

Access reports
--------------
`tox-envreport` creates one common ``env_report.json`` file, which contains all information about all used virtual
environments (venv) by tox.

Beside this a venv specific file is generated as well and contains information about the related venv only.
You can find this file in the venv-specific tox-folder. E.g: ``MY_PROJECT/.tox/py27/env_report_py27.json``
for a venv called *py27*.

The report file itself contains the venv-name as postfix. E.g.: ``env_report_py27.json``.
