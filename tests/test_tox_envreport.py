# -*- coding: utf-8 -*-


def test_dummy(cmd, initproj, monkeypatch):
    monkeypatch.delenv(str("TOXENV"), raising=False)

    path = initproj(
        'envreport_123',
        filedefs={
            'tox.ini': """
            [tox]
            envlist = a
            [testenv]
            deps=tox-envreport
            commands=echo "yehaaa"
        """
        })

    assert path

    result = cmd('all')
    assert result
