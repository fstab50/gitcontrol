#!/usr/bin/env python3
"""
Summary:
    Project giteven
        - giteven manages and updates all the repositories on your local maachine
        - reproduce

Module Args:

"""

import os


def get_repositories(origin):
    """
    Walks local fs directories identifying all git
    repositories
    """
    repositories = []
    for root, dirs, files in os.walk(origin):
        for path in dirs:
            if '.git' in path:
                repositories.append(
                        '/'.join(
                            os.path.abspath(os.path.join(root, path)).split('/')[:-1]
                        )
                )
    return repositories

home = os.getenv('HOME')
r = get_repositories(home)
