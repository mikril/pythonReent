import unittest
from task_3.block_errors import BlockErrors
class TestBlockErrors(unittest.TestCase):
    def test_zero(self):
        try:
            err_types = {ZeroDivisionError, TypeError}
            with BlockErrors(err_types):
                a = 1 / 0
            assert (True)
        except:
            assert(False)
    def test_TypeError(self):
        try:
            err_types = {ZeroDivisionError}
            with BlockErrors(err_types):
                a = 1 / "0"
            assert (False)
        except TypeError:
            assert (True)

    def test_blocks(self):
        try:
            outer_err_types = {TypeError}
            with BlockErrors(outer_err_types):
                inner_err_types = {ZeroDivisionError}
                with BlockErrors(inner_err_types):
                    a = 1 / '0'
            assert(True)
        except:
            assert(False)

    def test_exception(self):
        try:
            err_types = {Exception}
            with BlockErrors(err_types):
                a = 1 / '0'
            assert (True)
        except:
            assert (False)

    def test_baseexception(self):
        try:
            err_types = {BaseException}
            with BlockErrors(err_types):
                a = 1 / '0'
            assert (True)
        except:
            assert (False)