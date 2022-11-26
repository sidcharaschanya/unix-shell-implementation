import unittest
from collections import deque
from commands.command_visitor import CommandVisitor
from commands.impl.call import Call
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
            "test2.txt": "",
        }

        for file_name, file_content in self.files.items():
            with open(os.path.join(self.temp_dir, file_name), "w") as file:
                file.write(file_content)
                self.paths[file_name] = file.name

    def test_call(self):
        call = Call("echo", ["hello"], None, None)
        call.eval(None, self.out)
        self.assertEqual(self.out.popleft(), "hello\n")

    def test_call_with_input_redirection(self):
        call=Call("cat",[],self.paths["test1.txt"],None)
        call.eval(None,self.out)
        self.assertEqual(self.out.popleft(),"hello\n")

    def test_call_with_stdin(self):
        call=Call("grep",["he"],self.paths["test1.txt"],None)
        call.eval("hello world",self.out)
        self.assertEqual(self.out.popleft(),"hello\n")
        self.assertEqual(len(self.out),0)

    def test_call_with_output_redirection(self):
        call=Call("echo",["Interesting String"],None,self.paths["test2.txt"])
        call.eval(None,self.out)
        with open(self.paths["test2.txt"]) as f:
            self.assertEqual(f.readline(),"Interesting String\n")

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)
