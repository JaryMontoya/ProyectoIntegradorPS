"""Generated with stubgen from mypy, then manually edited, do not regen."""

from __future__ import annotations

import datetime
from dataclasses import dataclass
from types import FunctionType
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Set,
    Tuple,
    Type,
    Union,
    _GenericAlias,  # type: ignore
    overload,
)

from _typeshed import Incomplete

from reflex import constants as constants
from reflex.base import Base as Base
from reflex.state import BaseState as BaseState
from reflex.state import State as State
from reflex.utils import console as console
from reflex.utils import format as format
from reflex.utils import types as types
from reflex.utils.imports import ImmutableParsedImportDict, ImportDict, ParsedImportDict

USED_VARIABLES: Incomplete

def get_unique_variable_name() -> str: ...
def _encode_var(value: Var) -> str: ...

_global_vars: Dict[int, Var]

def _decode_var(value: str) -> tuple[VarData, str]: ...
def _extract_var_data(value: Iterable) -> list[VarData | None]: ...

class VarData(Base):
    state: str = ""
    imports: Union[ImportDict, ParsedImportDict] = {}
    hooks: Dict[str, None] = {}
    interpolations: List[Tuple[int, int]] = []
    @classmethod
    def merge(cls, *others: ImmutableVarData | VarData | None) -> VarData | None: ...

class ImmutableVarData:
    state: str = ""
    imports: ImmutableParsedImportDict = tuple()
    hooks: Tuple[str, ...] = tuple()
    def __init__(
        self,
        state: str = "",
        imports: ImportDict | ParsedImportDict | None = None,
        hooks: dict[str, None] | None = None,
    ) -> None: ...
    @classmethod
    def merge(
        cls, *others: ImmutableVarData | VarData | None
    ) -> ImmutableVarData | None: ...
    @classmethod
    def from_state(cls, state: Type[BaseState] | str) -> ImmutableVarData: ...

def _decode_var_immutable(value: str) -> tuple[ImmutableVarData, str]: ...

class Var:
    _var_name: str
    _var_type: Type
    _var_is_local: bool = False
    _var_is_string: bool = False
    _var_full_name_needs_state_prefix: bool = False
    _var_data: VarData | None = None
    @classmethod
    def create(
        cls,
        value: Any,
        _var_is_local: bool = True,
        _var_is_string: bool | None = None,
        _var_data: VarData | None = None,
    ) -> Optional[Var]: ...
    @classmethod
    def create_safe(
        cls,
        value: Any,
        _var_is_local: bool = True,
        _var_is_string: bool | None = None,
        _var_data: VarData | None = None,
    ) -> Var: ...
    @classmethod
    def __class_getitem__(cls, type_: Type) -> _GenericAlias: ...
    def _replace(self, merge_var_data=None, **kwargs: Any) -> BaseVar: ...
    def equals(self, other: Var) -> bool: ...
    def to_string(self) -> Var: ...
    def __hash__(self) -> int: ...
    def __format__(self, format_spec: str) -> str: ...
    def __getitem__(self, i: Any) -> Var: ...
    def __getattribute__(self, name: str) -> Var: ...
    def operation(
        self,
        op: str = ...,
        other: Optional[Var] = ...,
        type_: Optional[Type] = ...,
        flip: bool = ...,
        fn: Optional[str] = ...,
    ) -> Var: ...
    def compare(self, op: str, other: Var) -> Var: ...
    def __invert__(self) -> Var: ...
    def __neg__(self) -> Var: ...
    def __abs__(self) -> Var: ...
    def length(self) -> Var: ...
    def __eq__(self, other: Var) -> Var: ...
    def __ne__(self, other: Var) -> Var: ...
    def __gt__(self, other: Var) -> Var: ...
    def __ge__(self, other: Var) -> Var: ...
    def __lt__(self, other: Var) -> Var: ...
    def __le__(self, other: Var) -> Var: ...
    def __add__(self, other: Var) -> Var: ...
    def __radd__(self, other: Var) -> Var: ...
    def __sub__(self, other: Var) -> Var: ...
    def __rsub__(self, other: Var) -> Var: ...
    def __mul__(self, other: Var) -> Var: ...
    def __rmul__(self, other: Var) -> Var: ...
    def __pow__(self, other: Var) -> Var: ...
    def __rpow__(self, other: Var) -> Var: ...
    def __truediv__(self, other: Var) -> Var: ...
    def __rtruediv__(self, other: Var) -> Var: ...
    def __floordiv__(self, other: Var) -> Var: ...
    def __mod__(self, other: Var) -> Var: ...
    def __rmod__(self, other: Var) -> Var: ...
    def __and__(self, other: Var) -> Var: ...
    def __rand__(self, other: Var) -> Var: ...
    def __or__(self, other: Var) -> Var: ...
    def __ror__(self, other: Var) -> Var: ...
    def __contains__(self, _: Any) -> Var: ...
    def contains(self, other: Any, field: Union[Var, None] = None) -> Var: ...
    def reverse(self) -> Var: ...
    def foreach(self, fn: Callable) -> Var: ...
    @classmethod
    def range(
        cls,
        v1: Var | int = 0,
        v2: Var | int | None = None,
        step: Var | int | None = None,
    ) -> Var: ...
    def to(self, type_: Type) -> Var: ...
    def as_ref(self) -> Var: ...
    @property
    def _var_full_name(self) -> str: ...
    def _var_set_state(self, state: Type[BaseState] | str) -> Any: ...
    def _get_all_var_data(self) -> VarData | ImmutableVarData: ...
    def json(self) -> str: ...
    def _type(self) -> Var: ...

@dataclass(eq=False)
class BaseVar(Var):
    _var_name: str
    _var_type: Any
    _var_is_local: bool = False
    _var_is_string: bool = False
    _var_full_name_needs_state_prefix: bool = False
    _var_data: VarData | None = None
    def __hash__(self) -> int: ...
    def get_default_value(self) -> Any: ...
    def get_setter_name(self, include_state: bool = ...) -> str: ...
    def get_setter(self) -> Callable[[BaseState, Any], None]: ...

@dataclass(init=False)
class ComputedVar(Var):
    _var_cache: bool
    fget: FunctionType
    @property
    def _cache_attr(self) -> str: ...
    def __get__(self, instance, owner): ...
    def _deps(self, objclass: Type, obj: Optional[FunctionType] = ...) -> Set[str]: ...
    def _replace(self, merge_var_data=None, **kwargs: Any) -> ComputedVar: ...
    def mark_dirty(self, instance) -> None: ...
    def needs_update(self, instance) -> bool: ...
    def _determine_var_type(self) -> Type: ...
    @overload
    def __init__(
        self,
        fget: Callable[[BaseState], Any],
        **kwargs,
    ) -> None: ...
    @overload
    def __init__(self, func) -> None: ...

@overload
def computed_var(
    fget: Callable[[BaseState], Any] | None = None,
    initial_value: Any | types.Unset = types.Unset(),
    cache: bool = False,
    deps: Optional[List[Union[str, Var]]] = None,
    auto_deps: bool = True,
    interval: Optional[Union[datetime.timedelta, int]] = None,
    **kwargs,
) -> Callable[[Callable[[Any], Any]], ComputedVar]: ...
@overload
def computed_var(fget: Callable[[Any], Any]) -> ComputedVar: ...
@overload
def cached_var(
    fget: Callable[[BaseState], Any] | None = None,
    initial_value: Any | types.Unset = types.Unset(),
    deps: Optional[List[Union[str, Var]]] = None,
    auto_deps: bool = True,
    interval: Optional[Union[datetime.timedelta, int]] = None,
    **kwargs,
) -> Callable[[Callable[[Any], Any]], ComputedVar]: ...
@overload
def cached_var(fget: Callable[[Any], Any]) -> ComputedVar: ...

class CallableVar(BaseVar):
    def __init__(self, fn: Callable[..., BaseVar]): ...
    def __call__(self, *args, **kwargs) -> BaseVar: ...

def get_uuid_string_var() -> Var: ...
