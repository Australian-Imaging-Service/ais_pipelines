import os
from pathlib import Path
from click.testing import CliRunner
from pipeline2app.core.cli import make_docs

PKG_PATH = Path(__file__).parent.parent.absolute()

runner = CliRunner()

os.chdir(PKG_PATH)

results = runner.invoke(
    make_docs,
    [
        "australian-imaging-service",
        "docs/pipelines",
        "--flatten",
        "--default-data-space",
        "arcana.common:Clinical",
    ],
    catch_exceptions=False,
)
