class TestTableColorful:
    def testing_table_creation(self):
        import pytest
        from tabulato import colorful_tabulate
        from tabulato.table import DataMalformedException

        with pytest.raises(DataMalformedException) as exc_info:
            headers = ["Name", "Student Number", "DOB", "Email Address"]
            values = [[]]
            colorful_tabulate(
                headers=headers, data=values, colorful=True, bold_header=True
            )
        assert (
            str(exc_info.value)
            == "The headers and rows must have the same shape but received ((4, 0))."
        )
        with pytest.raises(DataMalformedException) as exc_info:
            headers = ["Name", "Student Number", "DOB", "Email Address"]
            values = [["Bob", "126178", None, "bob@bob.com"] for i in range(10)] + [
                "Jin",
                "66691",
            ]
            colorful_tabulate(
                headers=headers, data=values, colorful=True, bold_header=True
            )
        assert str(exc_info.value) == "The row values must have the same length."
