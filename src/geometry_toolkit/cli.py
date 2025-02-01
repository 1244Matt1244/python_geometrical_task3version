# src/geometry_toolkit/cli.py
import click
from typing import Optional
from .config.settings import Container
from .exceptions import handle_errors

@click.group()
@click.option("--engine", default="numeric", help="Calculation engine type")
@click.pass_context
@handle_errors
def cli(ctx, engine: str):
    container = Container()
    container.config.set("engine_type", engine)
    ctx.obj = container

@cli.command()
@click.option("--radius", type=float, required=True)
@click.option("--unit", default="m")
@click.pass_obj
def sphere(container, radius: float, unit: str):
    engine = container.calculation_engine()
    unit_converter = container.unit_converter()
    
    sphere = Sphere(Dimension(radius, unit), unit_converter)
    result = engine.calculate(sphere)
    
    click.echo(f"Surface Area: {result['area'][0]:.2f} {result['area'][1]}")
    click.echo(f"Volume: {result['volume'][0]:.2f} {result['volume'][1]}")
