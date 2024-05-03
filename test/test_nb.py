import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pytest

skip_notebooks = ["bqnt_profiling.ipynb", "bqnt_iql_magics.ipynb"]


@pytest.mark.parametrize(
    "notebook",
    [f for f in os.listdir("..") if f.endswith(".ipynb") and f not in skip_notebooks],
)
def test_notebook(notebook):

    with open(os.path.join("..", notebook)) as f:
        nb = nbformat.read(f, as_version=4)
    ep = ExecutePreprocessor(timeout=600)
    ep.preprocess(nb)
