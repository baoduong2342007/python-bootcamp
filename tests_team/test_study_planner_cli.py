"""Huy's T3-04 contract tests; draft until CLI dependency #54 lands.

These tests deliberately fail when the shared entry point is missing. No skip,
fake CLI, personal-module substitute, or altered expected result hides that gate.
"""

import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-10-26"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    """Exercise the real module in a child process from the bootcamp root."""
    return subprocess.run(
        [sys.executable, "-m", "shared.study_planner", *args],
        cwd=ROOT,
        env={**os.environ, "PYTHONPATH": str(ROOT)},
        capture_output=True,
        text=True,
        timeout=10,
    )


def assert_input_error(result: subprocess.CompletedProcess[str], code: int) -> None:
    """Require useful stderr and no traceback for expected user input errors."""
    assert result.returncode == code
    assert result.stdout == ""
    assert result.stderr.strip()
    assert "Traceback" not in result.stderr
    assert "No module named" not in result.stderr


def test_sample_partial_plan_order_hours_and_budget():
    result = run_cli("samples/tasks.csv", "--hours", "2", "--today", TODAY)
    assert result.returncode == 0
    assert result.stderr == ""
    assert result.stdout == "Assignment: 1.5 h\nDS exam: 0.5 h\n"
    hours = [
        float(line.rsplit(": ", 1)[1].removesuffix(" h"))
        for line in result.stdout.splitlines()
    ]
    assert all(value > 0 for value in hours)
    assert sum(hours) <= 2


def test_missing_file(tmp_path):
    path = tmp_path / "missing.csv"
    result = run_cli(str(path), "--hours", "2", "--today", TODAY)
    assert_input_error(result, 1)
    assert "missing.csv" in result.stderr


@pytest.mark.parametrize("contents", ["", "title,importance,effort_h,deadline\n"])
def test_empty_and_header_only_csv(tmp_path, contents):
    path = tmp_path / "empty.csv"
    path.write_text(contents, encoding="utf-8")
    result = run_cli(str(path), "--hours", "2", "--today", TODAY)
    assert result.returncode == 0
    assert result.stdout == "No tasks.\n"
    assert result.stderr == ""


def test_bad_csv_retains_line_context():
    result = run_cli("samples/tasks_bad.csv", "--hours", "2", "--today", TODAY)
    assert_input_error(result, 1)
    assert "line 3" in result.stderr


def test_wrong_schema_is_not_empty_input(tmp_path):
    path = tmp_path / "schema.csv"
    path.write_text("wrong,columns\n", encoding="utf-8")
    result = run_cli(str(path), "--hours", "2", "--today", TODAY)
    assert_input_error(result, 1)
    assert "line 1" in result.stderr


def test_require_all_reports_insufficient_hours():
    result = run_cli(
        "samples/tasks.csv", "--hours", "2", "--today", TODAY, "--require-all"
    )
    assert_input_error(result, 1)
    assert "7.5" in result.stderr
    assert "2" in result.stderr


def test_require_all_sufficient_hours():
    result = run_cli(
        "samples/tasks.csv", "--hours", "7.5", "--today", TODAY, "--require-all"
    )
    assert result.returncode == 0
    assert result.stdout == "Assignment: 1.5 h\nDS exam: 6 h\n"
    assert result.stderr == ""


@pytest.mark.parametrize("hours", ["0", "-1", "nan", "inf", "-inf", "abc"])
def test_hours_must_be_finite_and_positive(hours):
    result = run_cli("samples/tasks.csv", f"--hours={hours}", "--today", TODAY)
    assert_input_error(result, 2)
    assert "usage:" in result.stderr


def test_invalid_date_is_argparse_error():
    result = run_cli("samples/tasks.csv", "--hours", "2", "--today", "2026-02-29")
    assert_input_error(result, 2)
    assert "usage:" in result.stderr


def test_unknown_option_is_argparse_error():
    result = run_cli("samples/tasks.csv", "--hours", "2", "--not-a-real-option")
    assert_input_error(result, 2)
    assert "usage:" in result.stderr
