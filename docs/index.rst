.. tox-envreport documentation master file, created by
   sphinx-quickstart on Thu Oct  1 00:43:18 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

tox-envreport
=============

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


Common report: env_report.json
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following json-code contains information about **5** virtual environments: flake8, py27, py34, py35, py36.

.. literalinclude:: env_report.json

Contribute
----------
Please check our github project at https://github.com/useblocks/tox-envreport.
