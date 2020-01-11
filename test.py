import contextlib
from io import StringIO
import unittest
from preorder import generatePreorder
import sys

class TestPreorder(unittest.TestCase):
    def test_1(self):
        inorder = [4, 2, 1, 5, 3]; 
        postorder = [4, 2, 5, 3, 1]; 
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            generatePreorder(len(inorder), inorder, postorder)
        output = temp_stdout.getvalue().strip()

        assert output == '1 2 4 3 5'
        print()

    def test_2(self):
        inorder = [6, 4, 7, 2, 1, 5]; 
        postorder = [6, 7, 4, 2, 5, 1]; 
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            generatePreorder(len(inorder), inorder, postorder)
        output = temp_stdout.getvalue().strip()

        assert output == '1 2 4 6 7 5'
        print()

    def test_3(self):
        inorder = [2, 1, 6, 4, 7, 3, 8, 5, 9]; 
        postorder = [2, 6, 7, 4, 8, 9, 5, 3, 1]; 
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            generatePreorder(len(inorder), inorder, postorder)
        output = temp_stdout.getvalue().strip()

        assert output == '1 2 3 4 6 7 5 8 9'
        print()



if __name__ == "__main__":
    unittest.main()

