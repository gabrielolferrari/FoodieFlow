import logging
import sys

import daiquiri
from daiquiri import formatter
from decouple import config
from uvicorn.config import LOGGING_CONFIG


def configure():
    env = str(config('ENV', 'dev')).upper()
    if env in ['HML', 'PRD']:
        from ddtrace import patch

        patch(logging=True, asyncio=True, starlette=True, fastapi=True, aiohttp=False)

        daiquiri.setup(
            outputs=[daiquiri.output.Stream(stream=sys.stdout, formatter=formatter.DATADOG_FORMATTER)],
            level=logging.INFO,
        )
    else:
        daiquiri.setup(outputs=[daiquiri.output.Stream(stream=sys.stdout)], level=logging.INFO)

    LOGGING_CONFIG['loggers'] = {}
    daiquiri.set_default_log_levels([('uvicorn', 'INFO'), ('uvicorn.error', 'INFO'), ('uvicorn.access', 'INFO')])
