#!/usr/bin/env python
import os

from prompt_toolkit import prompt
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.sql import SqlLexer


def repl():
    history_file = f"{os.path.splitext(os.path.basename(__file__))[0]}_history.txt"
    while True:
        user_input = prompt(
            "> ",
            history=FileHistory(history_file),
            auto_suggest=AutoSuggestFromHistory(),
            completer=WordCompleter(['SELECT', 'SHOW', 'FROM', 'LIKE'], ignore_case=True),
            lexer=PygmentsLexer(SqlLexer)
        )
        print(user_input)


if __name__ == "__main__":
    repl()
