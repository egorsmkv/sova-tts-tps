from typing import Union

from tps.modules.emphasizer.rule_based.independent import Emphasizer
from tps.utils import prob2bool
from tps.symbols import accent


class UkEmphasizer(Emphasizer):
    def __init__(self, dict_source: Union[str, tuple, list, dict]=None, prefer_user: bool=True):
        super().__init__(dict_source, prefer_user)


    def _process_token(self, token, mask):
        if prob2bool(mask):
            return token.replace(accent, "")

        stress_exists = token.find(accent) != -1
        if stress_exists and self.prefer_user:
            return token

        return self.entries.get(token, token)
