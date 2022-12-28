#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) Rémi Ferrand <riton.github_at_gmail(dot)com>, 2022
#
# This software is governed by the CeCILL  license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.
#

from ghutils import get_user_starred_repos
from mdutils import readme_get_tools_links

IGNORE_REPOS_URL = set()


def main() -> int:
    readme_links = set(readme_get_tools_links())

    not_in_readme = []
    for repo in get_user_starred_repos("riton"):
        if repo["html_url"] in readme_links:
            continue

        if repo["html_url"] in IGNORE_REPOS_URL:
            continue

        not_in_readme.append(repo)

    if len(not_in_readme) > 0:
        print("Starred repositories not in README.md:")
        for repo in not_in_readme:
            print(
                # pylint: disable=consider-using-f-string
                "* [{name}]({html_url}) - {description}".format(
                    name=repo["name"],
                    html_url=repo["html_url"],
                    description=repo["description"],
                )
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
