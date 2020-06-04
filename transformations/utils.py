"""
Helper class and functions for transformations
"""


class LazyInit:
    """
    Class LazyInt generalizes initialization of data structures
    """
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set all remaining keyword arguments
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError(f'Invalid argument(s): {",".join(kwargs)}')


def transform_filter_names(es_input):
    """
    Iterates over ElasticSearch source input
    and creates seriazable objects
    :param es_input: result of ElasticSearch query
    :return: list of objects
    """
    from transformations.models import Employee
    result = []
    for emp in es_input:
        result.append(Employee(**emp['_source'].to_dict()))
    return result


def transform_only(es_input):
    result = []
    for emp in es_input:
        emp = emp['_source'].to_dict()
        result.append(emp)
    return result


def add_to_kwargs(attrs):
    output = dict()
    for key in attrs.keys():
        if '_' in key:
            first, last = key.split('_')
            output[f'{first.title()}{last.title()}'] = attrs.get(key)
        else:
            output[key.title()] = attrs.get(key)
    return output
