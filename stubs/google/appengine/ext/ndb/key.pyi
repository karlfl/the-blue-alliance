from typing import Optional, Union

class Key:
    def __new__(cls, *_args, **kwargs): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __cmp__(self, other): ...
    def __getnewargs__(self): ...
    def parent(self) -> Optional["Key"]: ...
    def root(self) -> "Key": ...
    def namespace(self) -> Optional[str]: ...
    def app(self) -> str: ...
    def id(self) -> Optional[Union[int, str]]: ...
    def string_id(self) -> Optional[str]: ...
    def integer_id(self) -> Optional[int]: ...
    def pairs(self): ...
    def flat(self): ...
    def kind(self) -> str: ...
    def reference(self): ...
    def serialized(self): ...
    def urlsafe(self): ...
    def get(self, **ctx_options): ...
    def get_async(self, **ctx_options): ...
    def delete(self, **ctx_options): ...
    def delete_async(self, **ctx_options): ...
    @classmethod
    def from_old_key(cls, old_key): ...
    def to_old_key(self): ...