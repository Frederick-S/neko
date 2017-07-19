import os
import frontmatter
import markdown
import jinja2
import shutil
from neko.post import Post


def init(target_path):
    layouts_path = os.path.join(os.path.dirname(__file__), './_layouts/')
    posts_path = os.path.join(os.path.dirname(__file__), './_posts/')

    shutil.copytree(layouts_path, os.path.join(target_path, '_layouts'))
    shutil.copytree(posts_path, os.path.join(target_path, '_posts'))


def parse_posts(posts_path):
    posts = []
    entries = os.scandir(posts_path)

    for entry in entries:
        with open(entry.path) as f:
            metadata, content = frontmatter.parse(f.read())

            posts.append(Post(metadata, markdown.markdown(content)))

    return posts


def build_site(posts, layouts_path, site_path):
    if os.path.exists(site_path):
        shutil.rmtree(site_path)

    os.mkdir(site_path)

    template_loader = jinja2.FileSystemLoader(searchpath=layouts_path)
    template_environment = jinja2.Environment(loader=template_loader)

    template = template_environment.get_template('index.html')
    html = template.render(posts=posts)

    with open('{0}index.html'.format(site_path), 'wb') as f:
        f.write(html.encode())

    for post in posts:
        title = post.metadata['title']

        template = template_environment.get_template('post.html')
        html = template.render(title=title, content=post.content)

        with open('{0}{1}.html'.format(site_path, title), 'wb') as f:
            f.write(html.encode())
