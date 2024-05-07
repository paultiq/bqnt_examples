from pathlib import Path
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pytest
import dotenv
import os

dotenv.load_dotenv(dotenv_path="test/.default_env", override=False)

NOTEBOOK_DIR = Path(os.environ["NOTEBOOK_DIR"])
SEARCH = os.environ["SEARCH"]
SKIP_NOTEBOOKS = os.environ["SKIP_NOTEBOOKS"].split(" ")


@pytest.mark.parametrize(
    "notebook",
    [
        f
        for f in NOTEBOOK_DIR.glob(SEARCH)
        if f.name not in SKIP_NOTEBOOKS
        and ".ipynb_checkpoints" not in str(f.absolute())
    ],
)
def test_notebook(notebook):
    with open(notebook) as f:
        nb = nbformat.read(f, as_version=4)
    ep = ExecutePreprocessor(timeout=600)
    ep.preprocess(nb)


# pytest -n 10
