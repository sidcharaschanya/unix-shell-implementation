import unittest

from collections import deque
from commands.impl.call import Call
from hypothesis import given, strategies as st
import os
import shutil


class TestCall(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.temp_dir = "resources"
        os.mkdir(self.temp_dir)
        self.paths = dict()

        self.files = {
            "test1.txt": "hello\n",
            "test2.txt": ""
        }

        for file_name, file_content in self.files.items():
            with open(os.path.join(self.temp_dir, file_name), "w") as file:
                file.write(file_content)
                self.paths[file_name] = file.name

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    @given(st.text())
    def test_call(self, text):
        Call(
            "echo", [text], None, None
        ).eval(None, self.out)
        self.assertEqual(self.out.popleft(), f"{text}\n")
        self.assertEqual(len(self.out), 0)

    @given(st.text())
    def test_call_stdin(self, text):
        Call(
            "cat", [], None, None
        ).eval(text, self.out)
        self.assertEqual(self.out.popleft(), text)
        self.assertEqual(len(self.out), 0)

    @given(st.text())
    def test_call_input_redirection(self, text):
        Call(
            "cat", [], self.paths["test1.txt"], None
        ).eval(text, self.out)
        self.assertEqual(self.out.popleft(), self.files["test1.txt"])
        self.assertEqual(len(self.out), 0)

    def test_call_output_redirection(self):
        Call(
            "echo", ["Interesting String"], None, self.paths["test2.txt"]
        ).eval(None, self.out)
        self.assertEqual(len(self.out), 0)
        with open(self.paths["test2.txt"]) as out_file:
            self.assertEqual(out_file.readline(), "Interesting String\n")

    def test_call_input_redirection_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            Call(
                "cat", [], os.path.join(self.temp_dir, "file.txt"), None
            ).eval(None, self.out)
