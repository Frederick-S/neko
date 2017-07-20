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

        shutil.copytree(layouts_path, os.path.join(target_path, '_layouts'))
        shutil.copytree(posts_path, os.path.join(target_path, '_posts'))

    def parse_posts(self):
        self.posts = []
        entries = os.scandir(self.posts_path)

        for entry in entries:
            with open(entry.path) as f:
                metadata, content = frontmatter.parse(f.read())

                self.posts.append(Post(metadata, markdown.markdown(content)))

    def build(self):
        self.parse_posts()

        if os.path.exists(self.site_path):
            shutil.rmtree(self.site_path)

        os.mkdir(self.site_path)

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
