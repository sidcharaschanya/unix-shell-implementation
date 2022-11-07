import unittest

from applications.application_factory import ApplicationFactory
from applications.impl.cat import Cat
from applications.impl.cd import Cd
from applications.impl.cut import Cut
from applications.impl.echo import Echo
from applications.impl.find import Find
from applications.impl.grep import Grep
from applications.impl.head import Head
from applications.impl.ls import Ls
from applications.impl.pwd import Pwd
from applications.impl.sort import Sort
from applications.impl.tail import Tail
from applications.impl.uniq import Uniq
from applications.impl.unsafe_decorator import UnsafeDecorator
from hypothesis import assume, given, strategies as st


class TestApplicationFactory(unittest.TestCase):
    apps = {
        "cat": Cat,
        "cd": Cd,
        "cut": Cut,
        "echo": Echo,
        "find": Find,
        "grep": Grep,
        "head": Head,
        "ls": Ls,
        "pwd": Pwd,
        "sort": Sort,
        "tail": Tail,
        "uniq": Uniq
    }

    @given(st.sampled_from(list(apps.keys())))
    def test_application_factory(self, name):
        self.assertIsInstance(
            ApplicationFactory.by_name(name), TestApplicationFactory.apps[name]
        )

    @given(st.sampled_from([f"_{app}" for app in apps.keys()]))
    def test_application_factory_unsafe_decorator(self, name):
        self.assertIsInstance(
            ApplicationFactory.by_name(name), UnsafeDecorator
        )

    @given(st.text())
    def test_application_factory_invalid(self, name):
        assume(name not in TestApplicationFactory.apps.keys())
        assume(name not in [
            f"_{app}" for app in TestApplicationFactory.apps.keys()
        ])
        with self.assertRaises(KeyError):
            ApplicationFactory.by_name(name)
