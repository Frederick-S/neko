import os
import sys
from neko.site import Site


def main():
    if len(sys.argv) == 1:
        print("Usage: neko init/build/serve")

        return

    command = sys.argv[1]

    if command not in ['init', 'build', 'serve']:
        print('Invalid command')

        return

    current_path = os.getcwd()
    posts_path = '{0}/_posts/'.format(current_path)
    layouts_path = '{0}/_layouts/'.format(current_path)
    site_path = '{0}/_site/'.format(current_path)

    site = Site(posts_path, layouts_path, site_path)

    if command == 'init':
        target_path = os.path.join(
            os.getcwd(), sys.argv[2] if len(sys.argv) == 3 else '.')

        site.init(target_path)
    elif command == 'build':
        site.build()
    elif command == 'serve':
        site.serve(8080)

if __name__ == '__main__':
    main()
