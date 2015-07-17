"""
This test should be excluded by the command line arg in tox.ini.
"""


def test_should_not_run():
    assert "never" == "always"
