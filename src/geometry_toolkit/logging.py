# src/geometry_toolkit/logging.py
import structlog

def configure_logging():
    structlog.configure(
        processors=[
            structlog.processors.JSONRenderer()
        ],
        wrapper_class=structlog.BoundLogger,
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory()
    )
    return structlog.get_logger()
