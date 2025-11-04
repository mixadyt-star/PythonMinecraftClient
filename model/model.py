from .validator import Validator
from ..datatypes import *
from .context import *
from .path import *

from typing import *


class Model:
    def __init__(self,
                 craft_data = None,
                 /,
                 parent_context: Optional[Context] = None,
                 local_context_path: Optional[Path] = None,
                 **kwargs):
        
        context = DictContext() if (parent_context is None) else parent_context
        local_context_path = ContextPath() if (local_context_path is None) else local_context_path
        local_context = local_context_path.apply(context)

        annotations = cast(Dict[str, Validator | DataType | Model], self.__annotations__)

        for name, annotation in annotations.items():
            if (type(annotation) == Validator):
                if (not annotation._condition(context, craft_data)):
                    continue

                annotation = annotation.datatype

            if (craft_data is None):
                if (type(annotation) == DataType):
                    self.__setattr__(name, annotation.encode(kwargs[name]))
                
                elif (type(annotation) == Model):
                    self.__setattr__(name, kwargs[name])
            
            else:
                if (type(annotation) == DataType):
                    value = annotation.decode(craft_data)

                    self.__setattr__(name, value)
                    local_context.append(name, value)
                
                elif (type(annotation) == Model):
                    local_context.append(name, DictContext())

                    self.__setattr__(name, annotation(
                        craft_data,
                        parent_context=context,
                        local_context_path=local_context_path.join(name),
                    ))