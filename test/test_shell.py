# import unittest
#
# from shell import eval
# from collections import deque
#
#
# class TestShell(unittest.TestCase):
#     def test_cut_normal(self):
#         out = deque()
#         eval("cut -b 1,2,3 res/dir1/test6.txt", out)
#         self.assertEqual(list(out), ["hel\n", "aaa\n", "bbb\n"])
#
#     def test_cut_pattern2(self):
#         out = deque()
#         eval("cut -b 1-3,5-7 res/dir1/test6.txt", out)
#         self.assertEqual(list(out), ["helo w\n", "aaa\n", "bbbccc\n"])
#
#     def test_cut_pattern3(self):
#         out = deque()
#         eval("cut -b -3,6- res/dir1/test6.txt", out)
#         self.assertEqual(list(out), ["hel world\n", "aaa\n", "bbbcc\n"])
#
#     def test_cut_overlap(self):
#         out = deque()
#         eval("cut -b 2-,3- res/dir1/test6.txt", out)
#         self.assertEqual(list(out), ["ello world\n", "aa\n", "bb ccc\n"])
