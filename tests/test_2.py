"""file doc string -> tells us what it does
addition of 2 numberes"""

import os
import sys
from script import addition

sys.path.insert(0, os.getcwd())


def test_add():
    """adds 2 numbers"""
    subj = addition(7, 9)
    assert subj == 16
    assert isinstance(subj, int)


test_add()  # call
