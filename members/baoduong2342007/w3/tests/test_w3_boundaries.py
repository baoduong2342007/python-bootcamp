"""Boundary and subprocess checks for Dương's Week 3 work."""

import subprocess
import sys
from datetime import date

import pytest

from members.baoduong2342007.w3.dates import parse_due
from members.baoduong2342007.w3.log_stats import analyse


def test_dates_boundary_and_case():
    assert parse_due(" TOMORROW ", date(2024, 2, 28)) == date(2024, 2, 29)
    assert parse_due("in 3 days", date(2026, 12, 30)) == date(2027, 1, 2)
    assert parse_due("TUE", date(2026, 10, 6)) == date(2026, 10, 13)
    with pytest.raises(ValueError):
        parse_due("2026-02-29", date(2026, 1, 1))


def test_statistics_empty_percentile_ties_and_no_mutation():
    assert analyse([]) == {"counts": {}, "p95": {}, "slowest": None}
    values = [("a", n) for n in reversed(range(1, 21))] + [("b", 19)]
    original = values.copy()
    result = analyse(values)
    assert result == {"counts": {"a": 20, "b": 1}, "p95": {"a": 19, "b": 19}, "slowest": "a"}
    assert values == original


def test_cli_output_and_errors(tmp_path):
    command = [sys.executable, "-m", "members.baoduong2342007.w3.cli"]
    good = subprocess.run(
        [*command, "samples/tasks.csv", "--hours", "2", "--today", "2026-10-26"],
        capture_output=True, text=True, check=False,
    )
    assert good.returncode == 0
    assert good.stdout == "Assignment: 1.5 h\nDS exam: 0.5 h\n"
    assert good.stderr == ""
    bad = subprocess.run([*command, str(tmp_path / "missing.csv"), "--hours", "2"],
                         capture_output=True, text=True, check=False)
    assert bad.returncode == 1 and bad.stderr and not bad.stdout
    invalid = subprocess.run([*command, "samples/tasks.csv", "--hours", "nan"],
                             capture_output=True, text=True, check=False)
    assert invalid.returncode == 2 and invalid.stderr and not invalid.stdout
