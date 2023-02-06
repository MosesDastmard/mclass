import unittest
from mclass import DictClass
import numpy as np
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        obj = DictClass({'id':1, 'data':{'name':'John', 'age':31, 'wife':{'name':'Jessica', 'age':np.nan}}})
        self.assertEqual(obj.id, 1)

if __name__ == '__main__':
    unittest.main()