# cli.py
import click
from rich.console import Console
from geoshapes.shapes import Circle, Sphere

console = Console()

@click.group()
def cli():
    """Geometry toolkit for calculating shape properties."""

@cli.command()
@click.option("--radius", type=float, required=True)
@click.option("--unit", default="m")
def circle(radius, unit):
    try:
        circle = Circle(radius, unit)
        area = circle.area()
        console.print(f"[bold green]Area:[/bold green] {area[0]:.2f} {area[1]}")
    except InvalidDimensionError as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
