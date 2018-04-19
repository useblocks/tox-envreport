# -*- coding: utf-8 -*-
import logging
import os

import pluggy
import json

hookimpl = pluggy.HookimplMarker("tox")
log = logging.getLogger('envreport')
env_data = {}


@hookimpl
def tox_runtest_post(venv):
    """
    Hooks into each test to collect and store information about used
    virtual environments.

    :param venv: actual virtual environment
    :return: None
    """

    # Collect paths from current configuration
    # ----------------------------------------
    venv_path = venv.path.strpath
    # venv_logdir = os.path.join(venv_path, "log")
    toxworkdir = venv.session.config.toxworkdir.strpath
    report_path = os.path.join(toxworkdir, "env_report.json")
    venv_report_path = os.path.join(venv_path,
                                    "env_report_{0}.json".format(venv.name))

    # Collect needed data
    # -------------------
    env_data.update(collect_data(venv))

    # Create json based string from collected data
    # --------------------------------------------
    # complete list of venvs
    data_json = json.dumps(env_data,
                           sort_keys=True,
                           indent=4)

    # current venv only
    data_venv_json = json.dumps(env_data[venv.name],
                                sort_keys=True,
                                indent=4)

    # Store json files
    # ----------------

    # ToDo: This needs to be done only once! But this hook gets called for
    # each test. Another "global" hook would be great, but tox does not
    # provide anything useful right now.
    with open(report_path, "w") as report_file:
        report_file.write(data_json)

    with open(venv_report_path, "w") as venv_report_file:
        venv_report_file.write(data_venv_json)


def collect_data(current_venv):
    """
    Collects needed data and constructs a dictionary, which gets returned

    :param current_venv: actual virtual environment
    :return: dict of collected data
    """
    data = {}
    data[current_venv.name] = {
        "name": current_venv.name,
        "path": current_venv.path.strpath,
    }
    data[current_venv.name].update(current_venv.session.resultlog.dict)

    data[current_venv.name].pop("testenvs", None)
    data[current_venv.name].update(
        current_venv.session.resultlog.dict["testenvs"][current_venv.name])

    return data
