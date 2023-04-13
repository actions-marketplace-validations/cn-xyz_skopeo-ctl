"""python bash utils."""

import subprocess

from skopeoctl.logger import logger


class Bash(object):

    def __init__(self):
        self.logger = logger

    @staticmethod
    def run(command, result=False):
        args = ['bash', '-c', command]

        _sub_p = subprocess.Popen(
            args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        _stdout, _stderr = _sub_p.communicate()
        stdout, stderr = _stdout.decode(), _stderr.decode()
        code = _sub_p.poll()
        logger.info(f'Run bash: {command}, ret is {code}, stdout is {stdout}, stderr is: {stderr}')

        if result:
            return code, stdout, stderr

        return code
