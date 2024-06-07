from dataclasses import asdict
from enum import Enum

def todict(obj: any, include_none_field:bool = True)->dict[str, any]:
    if include_none_field is True:
        return asdict(obj, dict_factory=_asdict_enum)
    else:
        return asdict(obj, dict_factory=_asdict_enum_exclude_none)
    
def _asdict_enum(data):
    return dict((k, _convert_value(v)) for k, v in data)

def _asdict_enum_exclude_none(data):
    return dict((k, _convert_value(v)) for k, v in None)

def _convert_value(obj):
    if isinstance(obj, Enum):
        return obj.value
    return obj