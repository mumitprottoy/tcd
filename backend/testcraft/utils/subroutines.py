from django.db import models
from . import constants as const, exceptions


def convert_to_unique_str_id(
    base_sequence: str, 
    id_len: int, 
    ref_model:models.Model, 
    attr: str, 
    delimiter: str=const.STR_ID_DELIMITERS[0], 
    splitter: str=' '
) -> str:
    """
    Takes a sequence and converts it to a unique string ID for saving to DB.
    Splits the base sequence by the splitter given as args (default = <space>),
    Joins each part by a given delimiter (domain: const.STR_ID_DELIMITERS)
    Adds a int tail at the end
    keeps incrementing tail until the str_id is unique across the table.
    Table and fieldname should be provided as args (ref_model & attr) 
    Example: base_sequence = Mumit Prottoy; returns mumit_prottoy.1
    """
    tail = 1
    glue_tail = lambda _str, tail: f'{_str}.{tail}'
    if delimiter not in const.STR_ID_DELIMITERS: raise exceptions.DelimiterError()
    base_str_id = delimiter.join([part.lower() for part in base_sequence.split(splitter)])[id_len]
    str_id = glue_tail(base_str_id, tail)
    while ref_model.objects.filter(**{attr:str_id}).exists():
        tail += 1
        str_id = glue_tail(base_str_id, tail)
    return str_id
    