import sys
import inspect
sys.tracebacklimit=0
class BlockErrors:

    def __init__(self, err_types):
        self.err_types = err_types

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):

        for err in self.err_types:
            if (err == type or err in inspect.getmro(type)):
                return True

        return False
if __name__=='__main__':
    err_types = {Exception}
    with BlockErrors(err_types):
        a = 1 / '0'
    print('Выполнено без ошибок')