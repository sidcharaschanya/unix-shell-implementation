import unittest
from commands.impl.pipe import Pipe
from commands.impl.call import Call
from collections import deque
import os
import shutil

class TestPipe(unittest.TestCase):

    def setUp(self) -> None:
        self.out=deque()
        self.temp_dir = "resources"
        os.mkdir(self.temp_dir)
        self.paths = dict()

        self.files = {
            "test1.txt": "hello\n",
            "test2.txt":"helloworld\naaa"
        }

        for file_name, file_content in self.files.items():
            with open(os.path.join(self.temp_dir, file_name), "w") as file:
                file.write(file_content)
                self.paths[file_name] = file.name

    def test_pipe(self):
        pipe=Pipe(Call("echo",["Interesting String"],None,None),Call("grep",["In"],None,None))
        pipe.eval(None,self.out)
        self.assertEqual(self.out.popleft(),"Interesting String\n")

    def test_nested_pipe(self):
        pipe = Pipe(
            Pipe(Call("cat", [self.paths["test2.txt"]], None, None), Call("grep", ["he"], None, None)),
            Call("grep", ["h"], None, None))
        pipe.eval(None,self.out)
        self.assertEqual(self.out.popleft(),"helloworld\n")

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

