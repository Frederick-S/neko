import os
import frontmatter
import markdown
import jinja2
import shutil
import http.server
from neko.post import Post


class Site():
    def __init__(self, posts_path, layouts_path, site_path):
        self.posts = []
        self.posts_path = posts_path
        self.layouts_path = layouts_path
        self.site_path = site_path

    def init(self, target_path):
        layouts_path = os.path.join(os.path.dirname(__file__), './_layouts/')
        posts_path = os.path.join(os.path.dirname(__file__), './_posts/')

        copy_folder(layouts_path, os.path.join(target_path, '_layouts'), True)
        copy_folder(posts_path, os.path.join(target_path, '_posts'), True)

    def parse_posts(self):
        self.posts = []
        entries = os.scandir(self.posts_path)

        for entry in entries:
            with open(entry.path) as f:
                metadata, content = frontmatter.parse(f.read())

                self.posts.append(Post(metadata, markdown.markdown(content)))

    def build(self):
        self.parse_posts()

        create_folder(self.site_path, True)

        # Copy static files
        static_files_path = os.path.join(
            os.path.dirname(__file__), './_static')

        copy_folder(
            static_files_path, os.path.join(self.site_path, '_static'), True)

        template_loader = jinja2.FileSystemLoader(searchpath=self.layouts_path)
        template_environment = jinja2.Environment(loader=template_loader)

        render_to_file(template_environment, 'index.html',
                       '{0}index.html'.format(self.site_path),
                       {'posts': self.posts})

        for post in self.posts:
            title = post.metadata['title']
            content = post.content

            render_to_file(template_environment, 'post.html',
                           '{0}{1}.html'.format(self.site_path, title),
                           {'title': title, 'content': content})

    def serve(self, port):
        self.build()

        os.chdir(self.site_path)

        http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler,
                         port=port, bind='')


def render_to_file(template_environment, template_file_name,
                   target_file_path, data):
    template = template_environment.get_template(template_file_name)
    html = template.render(data)

    with open(target_file_path, 'wb') as f:
        f.write(html.encode())


def create_folder(path, delete_existing_folder):
    if delete_existing_folder and os.path.exists(path):
        shutil.rmtree(path)

    os.mkdir(path)


def copy_folder(source_path, target_path, delete_existing_folder):
    if delete_existing_folder and os.path.exists(target_path):
        shutil.rmtree(target_path)

    shutil.copytree(source_path, target_path)
