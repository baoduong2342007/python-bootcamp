import subprocess
import sys
from pathlib import Path

BOOTCAMP_ROOT = Path(__file__).resolve().parents[4]


def test_cli_success():
    cmd = [
        sys.executable,
        "-m",
        "members.luongnhatinh.w3.cli",
        str(BOOTCAMP_ROOT / "samples" / "tasks.csv"),
        "--hours",
        "2",
        "--today",
        "2026-10-26",
    ]
    proc = subprocess.run(
        cmd, capture_output=True, text=True, cwd=BOOTCAMP_ROOT, check=False
    )
    assert proc.returncode == 0
    assert "Assignment: 1.5 h" in proc.stdout
    assert "DS exam: 0.5 h" in proc.stdout


def test_cli_missing_file():
    cmd = [
        sys.executable,
        "-m",
        "members.luongnhatinh.w3.cli",
        "nonexistent_tasks.csv",
        "--hours",
        "2",
    ]
    proc = subprocess.run(
        cmd, capture_output=True, text=True, cwd=BOOTCAMP_ROOT, check=False
    )
    assert proc.returncode == 1
    assert "Error loading CSV file" in proc.stderr


def test_cli_negative_hours():
    cmd = [
        sys.executable,
        "-m",
        "members.luongnhatinh.w3.cli",
        str(BOOTCAMP_ROOT / "samples" / "tasks.csv"),
        "--hours",
        "-1",
    ]
    proc = subprocess.run(
        cmd, capture_output=True, text=True, cwd=BOOTCAMP_ROOT, check=False
    )
    assert proc.returncode == 1
    assert "--hours must be greater than zero" in proc.stderr


def test_cli_invalid_date():
    cmd = [
        sys.executable,
        "-m",
        "members.luongnhatinh.w3.cli",
        str(BOOTCAMP_ROOT / "samples" / "tasks.csv"),
        "--hours",
        "2",
        "--today",
        "not-a-date",
    ]
    proc = subprocess.run(
        cmd, capture_output=True, text=True, cwd=BOOTCAMP_ROOT, check=False
    )
    assert proc.returncode == 1
    assert "Invalid date format" in proc.stderr
