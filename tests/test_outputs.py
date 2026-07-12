import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), "missing /app/report.json"
    with REPORT_PATH.open() as report_file:
        return json.load(report_file)


def test_report_json_shape():
    """Verifies instruction.md success criterion 1: report.json is a JSON object with exactly the required keys."""
    report = load_report()
    assert isinstance(report, dict), "report.json must contain a JSON object"
    assert set(report) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    """Verifies instruction.md success criterion 2: total_requests is integer 6."""
    report = load_report()
    assert report["total_requests"] == 6
    assert isinstance(report["total_requests"], int)


def test_unique_ips():
    """Verifies instruction.md success criterion 3: unique_ips is integer 3."""
    report = load_report()
    assert report["unique_ips"] == 3
    assert isinstance(report["unique_ips"], int)


def test_top_path():
    """Verifies instruction.md success criterion 4: top_path is /index.html."""
    report = load_report()
    assert report["top_path"] == "/index.html"
