from typing import Union


class EmailBaseTemplate:
    def __init__(self):
        self.subject: Union[str, None] = None
        self.body: Union[str, None] = None
