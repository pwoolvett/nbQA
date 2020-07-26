"""Comment-out magic IPython lines from converted notebook."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: nocover
    from pathlib import Path


def main(temp_python_file: "Path") -> None:
    """
    Temporarily comment-out "magic" IPython lines (e.g. :code:`%%timeit`).

    Parameters
    ----------
    temp_python_file
        Temporary Python file notebook was converted to.
    """
    with open(str(temp_python_file), "r") as handle:
        file = handle.readlines()

    file = [
        i if not (i.startswith("!") or i.startswith("%")) else f"# {i}" for i in file
    ]

    with open(str(temp_python_file), "w") as handle:
        handle.writelines(file)
