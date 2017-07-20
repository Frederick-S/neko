import os
import shutil
import unittest
from neko.site import Site


class TestSite(unittest.TestCase):
    def setUp(self):
        current_path = os.getcwd()
        posts_path = '{0}/_posts/'.format(current_path)
        layouts_path = '{0}/_layouts/'.format(current_path)
        site_path = '{0}/_site/'.format(current_path)

        self.site = Site(posts_path, layouts_path, site_path)

    def test_init(self):
        target_path = os.path.join(os.getcwd(), '.')

        self.site.init(target_path)
        self.site.build()

        self.assertTrue(len(self.site.posts) > 0)
        self.assertTrue(os.path.exists(self.site.posts_path))
        self.assertTrue(os.path.exists(self.site.layouts_path))

    def tearDown(self):
        remove_folder(self.site.posts_path)
        remove_folder(self.site.layouts_path)
        remove_folder(self.site.site_path)


def remove_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)

if __name__ == '__main__':
    unittest.main()
