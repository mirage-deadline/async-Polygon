from .templates import LastTrade
from .templates import AggregateBars
from .templates import PreviousClose
from .templates import LastTradeCryptoPair
from .templates import Template

import typing


AnyTemplate = typing.TypeVar("AnyTemplate", bound=Template)


name_to_method: typing.Dict[str, typing.Callable[[], typing.Type[AnyTemplate]]] = {
    'AggregateBars': AggregateBars,
    'LastTrade': LastTrade,
    'PreviousClose': PreviousClose,
}