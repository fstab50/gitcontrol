#!/usr/bin/env python3
"""
Summary:
    Project gitcontrol
        - gitcontrol manages and updates all the repositories on your local maachine
        - reproduce

Module Args:

"""
import os
import sys
import json
import inspect
import argparse
import platform
import subprocess
from gitcontrol.statics import PACKAGE, CONFIG_SCRIPT, local_config
from gitcontrol.help_menu import menu_body
from gitcontrol.script_utils import export_json_object, import_file_object, read_local_config
from gitcontrol.script_utils import stdout_message, bool_assignment, debug_mode, os_parityPath
from gitcontrol.colors import Colors
from gitcontrol import about, logd, __version__

try:
    from gitcontrol.oscodes_unix import exit_codes
    os_type = 'Linux'
    user_home = os.getenv('HOME')
    splitchar = '/'                             # character for splitting paths (linux)
    ACCENT = Colors.ORANGE
    TEXT = Colors.LT2GRAY
    TITLE = Colors.WHITE + Colors.BOLD
except Exception:
    from gitcontrol.oscodes_win import exit_codes    # non-specific os-safe codes
    os_type = 'Windows'
    user_home = os.getenv('username')
    splitchar = '\\'                            # character for splitting paths (windows)
    ACCENT = Colors.CYAN
    TEXT = Colors.LT2GRAY
    TITLE = Colors.WHITE + Colors.BOLD


# globals
logger = logd.getLogger(__version__)
container = []


def build_index(root):
    """
    Summary:
        - Operation to index local git repositories
        - Create index in the form of json configuration file
        - Returns object containing list of dictionaries, 1 per
          git repository
    Args:
    Returns:
        - index, TYPE: list
        - Format:

         .. code-block:: json

                [
                    {
                        "location": fullpath-including-repository,
                        "path":  path-to-repository (not incl repo),
                        "source": repository git remote string
                    }
                ]

    """
    index = []
    for path in locate_repositories(root):
        if path:
            index.append(
                {
                    "location": path,
                    "path": '/'.join(path.split('/')[:-1]),
                    "source": source_url(path)
                }
            )
    return index


def write_index(display=False):
    stdout_message('Generating index...')
    index_list = build_index(os.path.join(user_home, 'git'))
    output_file = 'repository.json'
    output_path = os.path.join(user_home, 'Backup/usr/' + output_file)
    if display:
        export_json_object(dict_obj=index_list)
        summary(index_list)
        return export_json_object(
                    dict_obj=index_list,
                    filename=output_path
                )
    return export_json_object(dict_obj=index_list, filename=output_path)


def help_menu():
    """
    Displays help menu contents
    """
    print(
        Colors.BOLD + '\n\t\t\t  ' + PACKAGE + Colors.RESET +
        ' help contents'
        )
    print(menu_body)
    return


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
        # NOTE: >> add repo to exception list here <<
        return ''
    return url


def summary(repository_list):
    """ Prints summary stats """
    count = len(repository_list)
    stdout_message(
        '%s Local git repositories detected and indexed' %
        (TITLE + str(count) + Colors.RESET))
    return True


def main(operation, debug_mode):
    """ Main """
    return True


def option_configure(debug=False, path=None):
    """
    Summary:
        Initiate configuration menu to customize keyup runtime options.
        Console script ```keyconfig``` invokes this option_configure directly
        in debug mode to display the contents of the local config file (if exists)
    Args:
        :path (str): full path to default local configuration file location
        :debug (bool): debug flag, when True prints out contents of local
         config file
    Returns:
        TYPE (bool):  Configuration Success | Failure
    """
    if CONFIG_SCRIPT in sys.argv[0]:
        debug = True    # set debug mode if invoked from CONFIG_SCRIPT
    if path is None:
        path = local_config['PROJECT']['CONFIG_PATH']
    if debug:
        if os.path.isfile(path):
            debug_mode('local_config file: ', local_config, debug, halt=True)
        else:
            msg = """  Local config file does not yet exist. Run:

            $ keyup --configure """
            debug_mode(msg, {'CONFIG_PATH': path}, debug, halt=True)
    r = configuration.init(debug, path)
    return r


def options(parser, help_menu=False):
    """
    Summary:
        parse cli parameter options
    Returns:
        TYPE: argparse object, parser argument set
    """
    parser.add_argument("-i", "--index", dest='index', action='store_true', required=False)
    parser.add_argument("-C", "--configure", dest='configure', action='store_true', required=False)
    parser.add_argument("-d", "--debug", dest='debug', action='store_true', required=False)
    parser.add_argument("-h", "--help", dest='help', action='store_true', required=False)
    parser.add_argument("-r", "--create-repos", dest='create', type=str, required=False)
    parser.add_argument("-u", "--update", dest='update', type=str, default='all', required=False)
    parser.add_argument("-V", "--version", dest='version', action='store_true', required=False)
    return parser.parse_args()


def package_version():
    """
    Prints package version and requisite PACKAGE info
    """
    print(about.about_object)
    sys.exit(exit_codes['EX_OK']['Code'])


def init_cli():
    # parser = argparse.ArgumentParser(add_help=False, usage=help_menu())
    parser = argparse.ArgumentParser(add_help=False)

    try:
        args = options(parser)
    except Exception as e:
        help_menu()
        stdout_message(str(e), 'ERROR')
        sys.exit(exit_codes['E_BADARG']['Code'])

    if len(sys.argv) == 1:
        help_menu()
        sys.exit(exit_codes['EX_OK']['Code'])

    elif args.help:
        help_menu()
        sys.exit(exit_codes['EX_OK']['Code'])

    elif args.version:
        package_version()

    elif args.configure:
        r = option_configure(args.debug, local_config['PROJECT']['CONFIG_PATH'])
        return r

    elif args.index:
        if write_index(display=True):
            sys.exit(exit_codes['EX_OK']['Code'])
        #with open(output_path, 'w') as f1:
        #    f1.write(json.dumps(index_list, indent=4))
    else:
        if precheck():              # if prereqs set, run
            # execute keyset operation
            success = main(
                        operation=args.update,
                        debug_mode=args.debug
                        )
            if success:
                logger.info('repository operation complete')
                sys.exit(exit_codes['EX_OK']['Code'])
        else:
            stdout_message(
                'Dependency check fail %s' % json.dumps(args, indent=4),
                prefix='AUTH',
                severity='WARNING'
                )
            sys.exit(exit_codes['E_DEPENDENCY']['Code'])

    failure = """ : Check of runtime parameters failed for unknown reason.
    Please ensure you have both read and write access to local filesystem. """
    logger.warning(failure + 'Exit. Code: %s' % sys.exit(exit_codes['E_MISC']['Code']))
    print(failure)