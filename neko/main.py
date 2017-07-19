import os
import sys
from neko.generate import init, parse_posts, build_site


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

    if command == 'init':
        target_path = os.path.join(
            os.getcwd(), sys.argv[2] if len(sys.argv) == 3 else '.')

        init(target_path)
    elif command == 'build':
        posts = parse_posts(posts_path)

        build_site(posts, layouts_path, site_path)
    elif command == 'serve':
        pass

if __name__ == '__main__':
    main()
