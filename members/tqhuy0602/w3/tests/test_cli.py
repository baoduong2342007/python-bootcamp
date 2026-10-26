"""Exercise the real personal entry point in child processes."""

import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[4]
MODULE = "members.tqhuy0602.w3.cli"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    """Run offline from the repo root, with bounded time and separate streams."""
    env = {**os.environ, "PYTHONPATH": str(ROOT)}
    return subprocess.run(
        [sys.executable, "-m", MODULE, *args],
        cwd=ROOT,
        env=env,
        check=False,
        capture_output=True,
        text=True,
        timeout=10,
    )


def test_reproducible_partial_plan():
    result = run_cli("samples/tasks.csv", "--hours", "2", "--today", "2026-10-26")
    assert result.returncode == 0
    assert result.stdout == "Assignment: 1.5 h\nDS exam: 0.5 h\n"
    assert result.stderr == ""


@pytest.mark.parametrize(
    ("first_effort", "second_effort", "first_hours", "second_hours"),
    [("0.125", "0.375", "0.125", "0.125"), ("0.1", "0.3", "0.1", "0.15")],
)
def test_fractional_effort_survives_task_conversion(
    tmp_path, first_effort, second_effort, first_hours, second_hours
):
    path = tmp_path / "fractional.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n"
        f"First,5,{first_effort},2026-10-26\n"
        f"Second,1,{second_effort},2026-10-26\n",
        encoding="utf-8",
    )
    result = run_cli(str(path), "--hours", "0.25", "--today", "2026-10-26")
    assert result.returncode == 0
    assert result.stdout == f"First: {first_hours} h\nSecond: {second_hours} h\n"
    assert result.stderr == ""
    hours = [float(line.rsplit(": ", 1)[1][:-2]) for line in result.stdout.splitlines()]
    assert sum(hours) == pytest.approx(0.25)


@pytest.mark.parametrize("file", ["missing.csv", "samples/tasks_bad.csv"])
def test_file_errors(file):
    result = run_cli(file, "--hours", "2", "--today", "2026-10-26")
    assert result.returncode == 1
    assert result.stdout == ""
    assert "Error:" in result.stderr
    assert "Traceback" not in result.stderr
    if "tasks_bad" in file:
        assert "line 3" in result.stderr


@pytest.mark.parametrize("contents", ["", "title,importance,effort_h,deadline\n"])
def test_empty_file(tmp_path, contents):
    path = tmp_path / "empty.csv"
    path.write_text(contents, encoding="utf-8")
    result = run_cli(str(path), "--hours", "2", "--today", "2026-10-26")
    assert result.returncode == 0
    assert result.stdout == "No tasks.\n"
    assert result.stderr == ""


@pytest.mark.parametrize("hours", ["0", "-1", "nan", "inf", "-inf", "abc"])
def test_invalid_hours(hours):
    result = run_cli("samples/tasks.csv", f"--hours={hours}")
    assert result.returncode == 2
    assert result.stdout == ""
    assert "usage:" in result.stderr
    assert "Traceback" not in result.stderr


def test_invalid_date():
    result = run_cli("samples/tasks.csv", "--hours", "2", "--today", "2026-02-29")
    assert result.returncode == 2
    assert "Traceback" not in result.stderr


@pytest.mark.parametrize("effort", ["nan", "inf", "-1"])
def test_invalid_task_effort(tmp_path, effort):
    path = tmp_path / "invalid.csv"
    path.write_text(
        f"title,importance,effort_h,deadline\nA,3,{effort},2026-10-30\n",
        encoding="utf-8",
    )
    result = run_cli(str(path), "--hours", "2")
    assert result.returncode == 1
    assert result.stdout == ""
    assert "finite and non-negative" in result.stderr
    assert "Traceback" not in result.stderr
