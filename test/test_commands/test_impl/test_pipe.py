import unittest

from collections import deque
from commands.impl.call import Call
from commands.impl.pipe import Pipe
from hypothesis import given, strategies as st
import os
import shutil


class TestPipe(unittest.TestCase):
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
    def test_pipe(self, text):
        Pipe(
            Call("echo", [text], None, None),
            Call("cat", [], None, None)
        ).eval(None, self.out)
        self.assertEqual(self.out.popleft(), f"{text}\n")
        self.assertEqual(len(self.out), 0)

    @given(st.text())
    def test_pipe_ignore_stdin_via_output_redirection(self, text):
        Pipe(
            Call("echo", [text], None, self.paths["test2.txt"]),
            Call("cat", [], None, None)
        ).eval(None, self.out)
        self.assertEqual(self.out.popleft(), "")
        self.assertEqual(len(self.out), 0)

    @given(st.text())
    def test_pipe_ignore_stdin_via_input_redirection(self, text):
        Pipe(
            Call("echo", [text], None, None),
            Call("cat", [], self.paths["test1.txt"], None)
        ).eval(None, self.out)
        self.assertEqual(self.out.popleft(), self.files["test1.txt"])
        self.assertEqual(len(self.out), 0)
