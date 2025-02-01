# src/geometry_toolkit/config/settings.py
from dependency_injector import containers, providers
from ..engines import NumericEngine, SymbolicEngine
from ..core.units import UnitConverter

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    
    unit_converter = providers.Singleton(
        UnitConverter,
        config.base_unit
    )

    calculation_engine = providers.Selector(
        config.engine_type,
        numeric=providers.Factory(NumericEngine),
        symbolic=providers.Factory(SymbolicEngine)
    )
