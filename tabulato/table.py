from typing import Literal


class DataMalformedException(Exception):
    pass


class CONFIG:
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"


COLOR_LITERAL = Literal[
    "BLACK", "RED", "GREEN", "YELLOW", "BLUE", "PURPLE", "CYAN", "WHITE"
]


def get_color(color: COLOR_LITERAL) -> str:
    if color == "BLACK":
        return CONFIG.BLACK
    if color == "RED":
        return CONFIG.RED
    if color == "BLUE":
        return CONFIG.BLUE
    if color == "WHITE":
        return CONFIG.WHITE
    if color == "GREEN":
        return CONFIG.GREEN
    if color == "CYAN":
        return CONFIG.CYAN
    if color == "PURPLE":
        return CONFIG.PURPLE
    if color == "YELLOW":
        return CONFIG.YELLOW


def colorful_tabulate(
    headers: list[str],
    data: list[list],
    colorful: bool = True,
    bold_header: bool = True,
    header_color: COLOR_LITERAL = "BLUE",
    even_row_color: COLOR_LITERAL = "GREEN",
    odd_row_color: COLOR_LITERAL = "YELLOW",
) -> None:
    lens = [len(row) for row in data]
    _max = lens[0]

    if not all([_max == length for length in lens]):
        raise DataMalformedException("The row values must have the same length.")

    num_columns = len(data[0])
    if len(headers) != num_columns:
        raise DataMalformedException(
            f"The headers and rows must have the same shape but received ({len(headers), len(data[0])})."
        )

    # Calculate the maximum width for each column
    column_widths = [max(len(str(row[i])) for row in data) for i in range(num_columns)]

    # Adjust column widths if headers are longer
    for i, header in enumerate(headers):
        column_widths[i] = max(column_widths[i], len(header))

    # Print the headers
    print("+", end="")
    for width in column_widths:
        print("-" * (width + 2) + "+", end="")
    print()
    for i, header in enumerate(headers):
        if colorful:
            print("| ", end="")
            print(
                get_color(header_color)
                + (CONFIG.BOLD if bold_header else "")
                + f"{str(header):<{column_widths[i]}} "
                + CONFIG.RESET,
                end="",
            )
        else:
            print("| ", end="")
            print(
                (CONFIG.BOLD if bold_header else "")
                + f"{str(header):<{column_widths[i]}} "
                + CONFIG.RESET,
                end="",
            )
    print("|")

    # Print the separator
    print("+", end="")
    for width in column_widths:
        print("-" * (width + 2) + "+", end="")
    print()

    # Print the data rows
    for index, row in enumerate(data):
        for i, cell in enumerate(row):
            if colorful:
                print("| ", end="")
                if index % 2 == 0:
                    print(
                        get_color(even_row_color)
                        + f"{str(cell):<{column_widths[i]}} "
                        + CONFIG.RESET,
                        end="",
                    )
                else:
                    print(
                        get_color(odd_row_color)
                        + f"{str(cell):<{column_widths[i]}} "
                        + CONFIG.RESET,
                        end="",
                    )
            else:
                print("| ", end="")
                print(
                    f"{str(cell):<{column_widths[i]}} ",
                    end="",
                )
        print("|")

    # Print the bottom line
    print("+", end="")
    for width in column_widths:
        print("-" * (width + 2) + "+", end="")
    print()
