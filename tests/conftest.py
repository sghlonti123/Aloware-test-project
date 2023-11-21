import time

from config.base import Base

base = Base()


def pytest_runtest_setup(item):
    time.sleep(1)
    base.setup_method()
    print("setup", item)


def pytest_runtest_teardown(item):
    time.sleep(1)
    base.quit_driver()
    print("teardown", item)
