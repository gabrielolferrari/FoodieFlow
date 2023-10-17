from typing import Dict, Any

import simplejson
from decouple import config
from fastapi import Request, Response

from commons.converter import custom_json_converter


def make_response(
    request: Request, body: Any, status_code: int = 200, headers: Dict[str, str] = {}, error_code=None
) -> Response:
    cors_origin = config('CORS_ORIGIN', default='')
    origin = request.headers.get('Origin', default=None)
    if not origin or origin not in cors_origin:
        origin = config('ORIGIN_DEFAULT', default='*')

    default_headers = {
        'Access-Control-Allow-Origin': origin,
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Allow-Headers': 'authorization,content-type',
        'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS',
    }

    message_template = {
        'success': True,
        'status_code': status_code,
        'error_message': None,
        'error_code': str(error_code),
        'message': None,
    }

    if body is not None:
        body_type = type(body)
        join_headers = {**default_headers, **headers}

        if body_type in (list, dict):
            join_headers.update({'Content-Type': 'application/json; charset=utf-8'})
            message_template['data'] = body
        elif body_type is str:
            join_headers.update({'Content-Type': 'application/json; charset=utf-8'})
            message_template['message'] = body
        elif body_type is bytes:
            join_headers.update({'Content-Type': 'application/csv'})
            message_template['message'] = body
        else:
            raise Exception(f'Invalid response type: {body}')

        return Response(
            content=simplejson.dumps(
                message_template, use_decimal=True, ensure_ascii=False, default=custom_json_converter
            ),
            status_code=status_code,
            headers=join_headers,
        )

    raise Exception('Response body cannot be null')


class ResponseBuilder:
    def __init__(self, message: str = ''):
        self._errors: Dict[str, Any] = {}
        self._message: str = message

    def add_field(self, field, error_message) -> 'ResponseBuilder':
        if not (field in self._errors):
            self._errors[field] = []

        self._errors[field].append(error_message)
        return self

    def build(self) -> Dict[str, Any]:
        if self._message == '' and self._errors == {}:
            self._message = 'Success'

        return {'message': self._message, 'errors': self._errors}
