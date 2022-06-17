import subprocess
import sys
from pathlib import Path

from typer.testing import CliRunner

from builder2ibek import __version__
from builder2ibek.__main__ import cli

runner = CliRunner()


def test_cli_version():
    cmd = [sys.executable, "-m", "builder2ibek", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__


def run_cli(*args):
    result = runner.invoke(cli, [str(x) for x in args])
    if result.exception:
        raise result.exception
    assert result.exit_code == 0, result


def test_mo_01(tmp_path: Path, samples: Path):
    """read and convert p45s 1st motion IOC"""

    ioc_xml_file = samples / "BL45P-MO-IOC-01.xml"
    yaml_file = tmp_path / "/tmp/bl45p-mo-ioc-01.yaml"
    yaml_file = Path("/tmp/bl45p-mo-ioc-01.yaml")
    run_cli("file", ioc_xml_file, "--yaml", yaml_file)
