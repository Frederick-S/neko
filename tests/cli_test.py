import io
import os
import sys
from contextlib import redirect_stdout
import unittest
from neko.main import main
from .site_test import remove_folder


class TestCli(unittest.TestCase):
    def setUp(self):
        current_path = os.getcwd()
        self.posts_path = '{0}/_posts/'.format(current_path)
        self.layouts_path = '{0}/_layouts/'.format(current_path)
        self.site_path = '{0}/_site/'.format(current_path)

    def test_invalid_command(self):
        sys.argv[1:] = []
        f = io.StringIO()

        with redirect_stdout(f):
            main()

        self.assertEqual('Usage: neko init/build/serve\n', f.getvalue())

        sys.argv[1:] = ['abc']
        f = io.StringIO()

        with redirect_stdout(f):
            main()

        self.assertEqual('Invalid command\n', f.getvalue())

    def test_life_cycle(self):
        sys.argv[1:] = ['init']
        main()

        sys.argv[1:] = ['build']
        main()

        self.assertTrue(os.path.exists(self.posts_path))
        self.assertTrue(os.path.exists(self.layouts_path))
        self.assertTrue(os.path.exists(self.site_path))

    def tearDown(self):
        remove_folder(self.posts_path)
        remove_folder(self.layouts_path)
        remove_folder(self.site_path)

if __name__ == '__main__':
    unittest.main()
