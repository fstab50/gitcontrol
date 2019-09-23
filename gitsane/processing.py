"""
Processing Module
    - Create repositories and associated directory path structure
      on local filesystem

Return:
    Success | Failure, TYPE: bool

"""
import os
import inspect
import subprocess
from libtools import stdout_message
from gitsane.input import ParseInputFile
from gitsane import logger


def parse_input(filepath):
    if os.path.exists(filepath):
        p = ParseInputFile(filepath)
        return p.parse()
    return None


def create_directory_structure(path_list):
    for path in [x['path'] for x in path_list]:
        if os.path.exists(path):
            continue
        else:
            os.makedirs(path)
    return True


def create_repositories(path_list):
    for pdict in path_list:
        # constants
        _root = pdict['repo'].split('/')[-1].split('.')[0]
        _location = pdict['path'].strip()
        _repository = pdict['repo'].strip()

        # cd to location
        os.chdir(_location)

        # log status
        stdout_message(f'Creating repository {_root} at location {_location}')

        # clone repository
        cmd = 'git clone {}'.format(_repository)
        stdout = subprocess.getoutput(cmd)
        for line in stdout.split('\n'):
            print(line)
    return True


def replicate_gitspace(filepath):
    parsed_json = parse_input(filepath)
    if create_directory_structure(parsed_json):
        return create_repositories(parsed_json)
    return False
