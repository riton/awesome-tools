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

from typing import Iterator
import requests


def get_user_starred_repos(user: str, per_page: int = 100) -> Iterator[dict]:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    query_params = {
        "per_page": per_page,
    }

    session = requests.Session()

    def get_url(url: str):
        resp = session.get(url, params=query_params, headers=headers)
        resp.raise_for_status()
        return resp

    resp = get_url(f"https://api.github.com/users/{user}/starred")
    yield from resp.json()

    while True:
        next_page_url = resp.links.get("next", None)
        if next_page_url is None:
            break

        resp = get_url(next_page_url["url"])
        yield from resp.json()
