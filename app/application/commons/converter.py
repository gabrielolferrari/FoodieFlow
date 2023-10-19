from datetime import datetime
from typing import Any
from uuid import UUID


def custom_json_converter(value: Any) -> Any:
    if isinstance(value, UUID):
        return str(value)

    if isinstance(value, datetime):
        return value.isoformat()

    return str(value)
