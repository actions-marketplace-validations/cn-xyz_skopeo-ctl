"""python git utils."""

import os

from jinja2 import Template

from skopeoctl import constants
from skopeoctl import utils


class Render(object):

    def __init__(self):
        pass

    def readme(self, images_list, src_org, src_repo):
        # for readme.md
        in_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'template/README.md')
        out_path = os.path.join(constants.GIT_REPO, 'README.md')
        with open(in_path, 'r') as in_file, open(out_path, 'w') as out_file:
            tmpl = Template(in_file.read())
            out_file.write(tmpl.render({
                'images_list': images_list,
                'image_count': len(images_list),
                'date': utils.now(),
                'src_org': src_org,
                'src_repo': src_repo,
                'dest_repo': constants.DEST_REPO.split('/')[-1]
            }))
