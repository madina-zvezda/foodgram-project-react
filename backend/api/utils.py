from typing import Dict

from rest_framework import exceptions, status
from rest_framework.response import Response


FIVE_NUM = 5
TWO_NUM = 2
ZERO_NUM = 0
TEN_NUM = 10
def get_end_letter(value):
    end_lib: Dict[int, str] = {FIVE_NUM: '', TWO_NUM: 'а', ZERO_NUM: ''}

    for my_key in end_lib:

        if value % TEN_NUM >= my_key:
            return end_lib[my_key]

    return ''


def create_or_delete_record(request, record, serializer_data, params):
    if request.method == 'POST':

        if record.exists():
            raise exceptions.ValidationError('records already exists.')

        record.create(user=request.user, **params)
        return Response(serializer_data, status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        if not record.exists():
            raise exceptions.ValidationError('records does not exists.')
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
