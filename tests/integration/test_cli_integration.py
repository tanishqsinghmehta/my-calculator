from click.testing import CliRunner


class TestCLIIntegration:
    """Integration tests for CLI and calculator module"""

    def run_cli(self, *args):
        from src.cli import calculate

        runner = CliRunner()
        return runner.invoke(calculate, list(args))

    def test_cli_add_integration(self):
        res = self.run_cli("add", "5", "3")
        assert res.exit_code == 0
        assert res.output.strip() == "8"

    def test_cli_subtract_integration(self):
        res = self.run_cli("subtract", "5", "3")
        assert res.exit_code == 0
        assert res.output.strip() == "2"

    def test_cli_multiply_integration(self):
        res = self.run_cli("multiply", "4", "7")
        assert res.exit_code == 0
        assert res.output.strip() == "28"

    def test_cli_divide_integration(self):
        res = self.run_cli("divide", "15", "3")
        assert res.exit_code == 0
        assert res.output.strip() == "5"

    def test_cli_sqrt_integration(self):
        res = self.run_cli("sqrt", "16")
        assert res.exit_code == 0
        assert res.output.strip() == "4"

    def test_cli_error_handling_integration(self):
        res = self.run_cli("divide", "10", "0")
        assert res.exit_code == 1
        assert "Cannot divide by zero" in res.output
