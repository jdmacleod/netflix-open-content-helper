import typer
from typing_extensions import Annotated


def greet(
    name: Annotated[str, typer.Option(help="The name to greet.")],
    count: Annotated[int, typer.Option(help="Number of times to greet.")],
) -> None:
    """
    Greet a person with the given name.

    Args:
        name (str): The name of the person to greet.
        count (int): The number of times to greet the person.
    """
    for _ in range(count):
        print(f"Hello {name}!")
