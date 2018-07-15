#!/usr/bin/env python3
"""
Summary:
    Project giteven
        - giteven manages and updates all the repositories on your local maachine
        - reproduce

Module Args:

"""
import os
import inspect
import platform
import subprocess
from giteven.statics import PACKAGE, seed_config
from giteven.script_utils import export_json_object, import_file_object, read_local_config
from giteven.script_utils import stdout_message, bool_assignment, debug_mode, os_parityPath
from giteven.colors import Colors
from giteven import logd, __version__


try:
    from giteven.oscodes_unix import exit_codes
    os_type = 'Linux'
    user_home = os.getenv('HOME')
    splitchar = '/'                             # character for splitting paths (linux)
    ACCENT = Colors.BLUE
    TEXT = Colors.LT2GRAY
except Exception:
    from giteven.oscodes_win import exit_codes    # non-specific os-safe codes
    os_type = 'Windows'
    user_home = os.getenv('username')
    splitchar = '\\'                            # character for splitting paths (windows)
    ACCENT = Colors.CYAN
    TEXT = Colors.LT2GRAY


# globals
logger = logd.getLogger(__version__)
container = []


def build_index(root):
    """
    Summary:
        - Operation to index local git repositories
        - Create index in the form of json configuration file
    Args:
    Returns:
        - index, TYPE: list
    """
    index = []
    for path in locate_repositories(root):
        index.append[
            {}
        ]


def locate_repositories(origin):
    """
    Summary:
        Walks local fs directories identifying all git repositories
    Returns:
        paths, TYPE: list
    """
    repositories = []
    for root, dirs, files in os.walk(origin):
        for path in dirs:
            try:
                if path.endswith('.git'):
                    repositories.append(
                        '/'.join(
                            os.path.abspath(os.path.join(root, path)).split('/')[:-1]
                        )
                    )
            except OSError as e:
                logger.exception(
                    '%s: Read error while examining local filesystem path (%s)' %
                    (inspect.stack()[0][3], path)
                )
                continue
    return repositories


def source_url(path):
    """
    Returns:
        git repository source url, TYPE: str
    """
    cmd = 'git remote -v | head -n 1'
    os.chdir(path)

    try:
        url = subprocess.getoutput(cmd).split('\t')[1].split(' ')[0]
    except IndexError:
        logger.exception(
                '%s: problem retrieving git source url for %s' %
                (inspect.stack()[0][3], path)
            )
        return ''
    return url
