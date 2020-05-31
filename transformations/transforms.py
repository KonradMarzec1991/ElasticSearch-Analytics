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
