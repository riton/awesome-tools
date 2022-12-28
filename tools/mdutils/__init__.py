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

from pathlib import PosixPath
from typing import Iterator

README_FILE_PATH = PosixPath("../README.md")


def readme_get_tools_links() -> Iterator[str]:
    # very naive parsing but I know I'm not gonna
    # break the file format
    with open(README_FILE_PATH, "r", encoding="utf-8") as readme_fd:
        for line in readme_fd.readlines():
            if not line.startswith("*"):
                continue
            yield _naively_extract_link(line.strip())


def _naively_extract_link(line: str) -> str:
    # line is something like:
    # * [ripgrep](https://github.com/BurntSushi/ripgrep) - ...

    link_start = line.index("(")
    link_end = line[link_start + 1 :].index(")")

    return line[link_start + 1 : link_start + link_end + 1]
