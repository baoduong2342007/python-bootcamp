"""Unit tests for the personal study planner CLI in members/pqquyenn/w3/cli.py."""

import subprocess
import sys
from pathlib import Path

from members.pqquyenn.w3.cli import main

SAMPLES = Path(__file__).resolve().parents[4] / "samples"


def test_cli_subprocess_happy_path():
    """Verify standard happy path execution via python -m subprocess."""
    cmd = [
        sys.executable,
        "-m",
        "members.pqquyenn.w3.cli",
        str(SAMPLES / "tasks.csv"),
        "--hours",
        "2",
        "--today",
        "2026-10-26",
    ]
    res = subprocess.run(cmd, check=False, capture_output=True, text=True)
    assert res.returncode == 0
    assert "Assignment: 1.5 h" in res.stdout
    assert "DS exam: 0.5 h" in res.stdout


def test_cli_subprocess_missing_file():
    """Verify missing CSV file returns exit code 1 with error on stderr."""
    cmd = [
        sys.executable,
        "-m",
        "members.pqquyenn.w3.cli",
        str(SAMPLES / "nonexistent.csv"),
        "--hours",
        "2",
        "--today",
        "2026-10-26",
    ]
    res = subprocess.run(cmd, check=False, capture_output=True, text=True)
    assert res.returncode == 1
    assert "Error: Tasks file" in res.stderr
    assert "does not exist" in res.stderr


def test_cli_subprocess_invalid_hours_nan_and_inf():
    """Verify non-finite hours return exit code 2."""
    cmd_nan = [
        sys.executable,
        "-m",
        "members.pqquyenn.w3.cli",
        str(SAMPLES / "tasks.csv"),
        "--hours",
        "nan",
        "--today",
        "2026-10-26",
    ]
    res_nan = subprocess.run(cmd_nan, check=False, capture_output=True, text=True)
    assert res_nan.returncode == 2

    cmd_inf = [
        sys.executable,
        "-m",
        "members.pqquyenn.w3.cli",
        str(SAMPLES / "tasks.csv"),
        "--hours",
        "inf",
        "--today",
        "2026-10-26",
    ]
    res_inf = subprocess.run(cmd_inf, check=False, capture_output=True, text=True)
    assert res_inf.returncode == 2


def test_cli_invalid_arguments():
    """Verify main direct calls with invalid arguments return exit code 2."""
    assert main([str(SAMPLES / "tasks.csv"), "--hours", "-1"]) == 2
    assert main([str(SAMPLES / "tasks.csv"), "--hours", "0"]) == 2
    assert main([str(SAMPLES / "tasks.csv"), "--hours", "nan"]) == 2
    assert main([str(SAMPLES / "tasks.csv"), "--hours", "inf"]) == 2
    assert (
        main([str(SAMPLES / "tasks.csv"), "--hours", "2", "--today", "not-a-date"]) == 2
    )


def test_cli_bad_csv_file():
    """Verify invalid CSV returns exit code 1."""
    code = main([str(SAMPLES / "tasks_bad.csv"), "--hours", "2"])
    assert code == 1
