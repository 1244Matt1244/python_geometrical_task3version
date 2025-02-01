# core/logging.py
import logging
import structlog

def configure_logging():
    structlog.configure(
        processors=[
            structlog.processors.JSONRenderer()
        ],
        logger_factory=structlog.PrintLoggerFactory()
    )
    return structlog.get_logger()
