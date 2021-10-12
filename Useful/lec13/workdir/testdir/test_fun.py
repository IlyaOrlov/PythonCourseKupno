from unittest import TestCase, main
import os
import sys
sys.path.append('..')
from example import fun, copyfun


class TestExample(TestCase):
    def setUp(self):
        self._src_filepath = 'src.txt'
        self._content = 'abcdef'
        with open(self._src_filepath, 'w') as f:
            f.write(self._content)
        self._dst_filepath = 'dst.txt'

    def test_fun(self):
        self.assertEqual(fun(10, 20), 200)

    def test_copyfun(self):
        copyfun(self._src_filepath, self._dst_filepath)
        self.assertTrue(os.path.exists(self._dst_filepath))
        with open(self._dst_filepath, 'r') as f:
            self.assertEqual(f.read(), self._content)


    def tearDown(self):
        if os.path.exists(self._src_filepath):
            os.remove(self._src_filepath)
        if os.path.exists(self._dst_filepath):
            os.remove(self._dst_filepath)


if __name__ == "__main__":
    main()
