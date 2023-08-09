from arcana.core.utils.misc import show_cli_trace
from arcana.core.cli.deploy import make_docs


def test_make_docs(bids_app_spec_path, cli_runner, work_dir):
    result = cli_runner(make_docs, [bids_app_spec_path, str(work_dir)])

    assert result.exit_code == 0, show_cli_trace(result)
