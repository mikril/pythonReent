import unittest
from task_4.Redirect import Redirect
class TestBlockErrors(unittest.TestCase):
    def test_stdout(self):

        stdout_file = open('stdout.txt', 'w')
        stderr_file = open('stderr.txt', 'w')
        with Redirect(stdout=stdout_file, stderr=stderr_file):
            print('Hello stdout.txt')
        with open('stdout.txt', 'r') as file:
            assert('Hello stdout.txt' in file.read())



    def test_stderr(self):
            stdout_file = open('stdout.txt', 'w')
            stderr_file = open('stderr.txt', 'w')

            with Redirect(stdout=stdout_file, stderr=stderr_file):
                raise Exception('Hello stderr.txt')

            with open('stderr.txt', 'r') as file:
                assert (str(Exception('Hello stderr.txt')) in file.read())

