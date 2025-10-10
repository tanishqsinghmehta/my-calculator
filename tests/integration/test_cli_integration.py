"""
Integration Tests - CLI + Calculator Working Together
"""

import subprocess
import sys
import pytest


class TestCLIIntegration:
    """Integration tests for CLI interacting with calculator module."""

    def run_cli(self, *args):
        """Helper method to run CLI and capture output."""
        cmd = [sys.executable, "src/cli.py"] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        return result

    def test_cli_multiply_integration(self):
        """Test CLI can perform multiplication"""
        result = self.run_cli("multiply", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "15"

    def test_cli_divide_integration(self):
        """Test CLI can perform division"""
        result = self.run_cli("divide", "5", "3")
        assert result.returncode == 0
        # The CLI prints rounded float (2 decimals)
        assert result.stdout.strip() == "1.67"
