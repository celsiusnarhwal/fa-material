from click import ClickException

from iconoclast.cli.context import get_context


class Iconoquit(ClickException):
    def __init__(self, message: str, code: int = 1):
        super().__init__(message.strip())
        setattr(self, "ctx", get_context())
        self.exit_code = code
