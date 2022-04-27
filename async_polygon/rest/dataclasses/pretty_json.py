from async_polygon.rest import dataclasses


def to_pretty_json(_responseName: str, resp_json: dict) -> dict:
    """_summary_

    Args:
        _responseName (str): Api name method
        resp_json (json): results from get request

    Returns:
        json: pretty json obj
    """

    result = dataclasses.name_to_method[_responseName]()
    result = result.make_pretty_json(resp_json)
    return result