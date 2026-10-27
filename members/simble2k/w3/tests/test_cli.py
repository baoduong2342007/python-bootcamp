"""Unit tests for the personal study planner CLI."""

import subprocess
import sys
from pathlib import Path

from members.simble2k.w3.cli import main

SAMPLES = Path(__file__).resolve().parents[4] / "samples"


def test_cli_subprocess_happy_path():
    cmd = [
        sys.executable,
        "-m",
        "members.simble2k.w3.cli",
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
    cmd = [
        sys.executable,
        "-m",
        "members.simble2k.w3.cli",
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


def test_cli_invalid_arguments():
    # Negative hours
    code = main([str(SAMPLES / "tasks.csv"), "--hours", "-1"])
    assert code == 2

    # Invalid ISO date format
    code_bad_date = main(
        [str(SAMPLES / "tasks.csv"), "--hours", "2", "--today", "not-a-date"]
    )
    assert code_bad_date == 2


def test_cli_bad_csv_file():
    # tasks_bad.csv has invalid format
    code = main([str(SAMPLES / "tasks_bad.csv"), "--hours", "2"])
    assert code == 1
