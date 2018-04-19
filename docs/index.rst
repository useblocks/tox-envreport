.. image:: https://img.shields.io/pypi/l/tox-envreport.svg
    :target: https://pypi.python.org/pypi/tox-envreport
    :alt: License
.. image:: https://img.shields.io/pypi/pyversions/tox-envreport.svg
    :target: https://pypi.python.org/pypi/tox-envreport
    :alt: Supported versions
.. image:: https://readthedocs.org/projects/tox-envreport/badge/?version=latest
    :target: https://readthedocs.org/projects/tox-envreport/
.. image:: https://travis-ci.org/useblocks/tox-envreport.svg?branch=master
    :target: https://travis-ci.org/useblocks/tox-envreport
    :alt: Travis-CI Build Status
.. image:: https://img.shields.io/pypi/v/tox-envreport.svg
    :target: https://pypi.python.org/pypi/tox-envreport
    :alt: PyPI Package latest release

tox-envreport
=============

``tox-envreport`` is a plugin for `tox <https://tox.readthedocs.io/en/latest/>`_
to document the setup of used virtual environments.

By installing this plugin, **2** types of files are created automatically during each tox run:

| **env-report.json**
| A virtual environment specific file, which is created for each used virtual environment.
| Stored inside each virtual environment folder. E.g: ``.tox/py34/env-report.json``.


| **tox-report.json**
| A global report file, which bundles data from all virtual environment specific files.
| Stored inside ``.tox`` folder. E.g: ``.tox/tox-report.json``.


.. warning::

   This plugin is an early alpha version and under heavy development.
   The used structure inside export files may change in future.

A report contains the following information and more:

* **System**: host, platform,
* **Virtual environment**: name, path, tested package (incl. hashes)
* **Python**: executable, version, installed packages (incl. version)
* **Executed commands** : setup, test (all incl. output and return code)


Installation
------------
``pip install tox-envreport``

Usage
-----

The installation of the plugin is enough to automatically activate it for each tox run.

There is nothing more to do or to configure.

Access reports
--------------
``tox-envreport`` creates one common ``tox-report.json`` file, which contains all information about all used virtual
environments (venv) by tox.

Beside this a venv specific file is generated as well and contains information about the related venv only.
You can find this file in the venv-specific tox-folder. E.g: ``MY_PROJECT/.tox/py27/env-report.json``
for a venv called *py27*.

Motivation
----------
``tox-envreport`` was created for an automotive project, which needs to archive beside test results also used
test environments.
The goal is to provide enough information to be able to setup an identical test environment in 20+ years.

``tox-envreport`` is part of a software bundle, which was designed to fulfill
the parameters of the `ISO 26262 <https://en.wikipedia.org/wiki/ISO_26262>`_ standard
for safety critical software in automotive companies.
Other tools are: `sphinx-needs <http://sphinxcontrib-needs.readthedocs.io/en/latest/>`_.


Content
-------

.. toctree::
	:maxdepth: 2

	examples
	contribute
	changelog

Acknowledgments
---------------

Thanks to `Lazur URH <https://openclipart.org/detail/204460/big-shot-remix>`_ , who designed the tox-envreport logo.


