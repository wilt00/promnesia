import os
from functools import wraps
from pathlib import Path

import pytest # type: ignore

def skip_if_ci(reason):
    return pytest.mark.skipif('CI' in os.environ, reason=reason)


def uses_x(f):
    @skip_if_ci('Uses X server')
    @wraps(f)
    def ff(*args, **kwargs):
        return f(*args, **kwargs)
    return ff



@pytest.fixture
def tdir(tmp_path):
    yield Path(tmp_path)
