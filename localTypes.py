from typing import Dict, Union, List, Literal, TypedDict


class CommandBody(TypedDict):
    command: str
    stdin: Union[None, str]
    pipe_to_stdin: Union[None, bool]
    expected_return_code: int
    return_stderr_on_error: bool


class RouteBody(TypedDict):
    method: str
    params: Union[None, List[str]]
    return_stdout: bool
    commands: List[CommandBody]


Route = Dict[str, RouteBody]


class DefaultResponseBody(TypedDict):
    type: Literal["string", "file"]
    text: str
    location: str
    mime_type: str


Default_response = Dict[str, DefaultResponseBody]


class RouteError(Exception):
    pass


class DefaultResponseError(Exception):
    pass
