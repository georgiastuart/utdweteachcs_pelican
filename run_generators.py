import jinja2 as j2
import os
import json
from htmlmin import minify

loader = j2.FileSystemLoader(['utdweteachcs_theme/templates/partials/', 'utdweteachcs_theme/templates/'])
env = j2.Environment(loader=loader, autoescape=j2.select_autoescape(['html', 'xml']))

for root, dirs, files in os.walk('content/'):
    root_list = root.split('/')
    if root_list[-1] == 'html_generators':
        for file in files:
            with open(os.path.join(root, file), 'r') as fp:
                template_info = json.load(fp)
            template = env.get_template(template_info['template'])
            rendered_template = template.render(settings=template_info['settings'])
            with open(template_info['outfile'], 'w') as fp:
                fp.write(minify(rendered_template))

