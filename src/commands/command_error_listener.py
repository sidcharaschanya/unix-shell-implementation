from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException


class CommandErrorListener(ErrorListener):
    INSTANCE = None

    # noinspection PyPep8Naming
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        message = f"syntax error: line {line}:{column} {msg}"
        raise ParseCancellationException(message)


CommandErrorListener.INSTANCE = CommandErrorListener()
