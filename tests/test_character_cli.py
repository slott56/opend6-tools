"""Test Character CLI
"""
from typer.testing import CliRunner

from opend6_tools.character.cli import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["--format", "LATEX"])
    assert result.exit_code == 0
    assert r"\title{OpenD6 Fantasy Character Sheet}" in result.output
    assert r"\textbf{Character Name}:  \hrulefill" in result.output
