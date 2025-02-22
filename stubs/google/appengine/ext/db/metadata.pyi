from google.appengine.api import datastore_types as datastore_types
from google.appengine.ext import db as db
from typing import Any

class BaseMetadata(db.Model):
    KIND_NAME: str
    @classmethod
    def kind(cls): ...

class Namespace(BaseMetadata):
    KIND_NAME: str
    EMPTY_NAMESPACE_ID: Any
    @property
    def namespace_name(self): ...
    @classmethod
    def key_for_namespace(cls, namespace): ...
    @classmethod
    def key_to_namespace(cls, key): ...

class Kind(BaseMetadata):
    KIND_NAME: str
    @property
    def kind_name(self): ...
    @classmethod
    def key_for_kind(cls, kind): ...
    @classmethod
    def key_to_kind(cls, key): ...

class Property(BaseMetadata):
    KIND_NAME: str
    @property
    def property_name(self): ...
    @property
    def kind_name(self): ...
    property_representation: Any
    @classmethod
    def key_for_kind(cls, kind): ...
    @classmethod
    def key_for_property(cls, kind, property_): ...
    @classmethod
    def key_to_kind(cls, key): ...
    @classmethod
    def key_to_property(cls, key): ...

class EntityGroup(BaseMetadata):
    KIND_NAME: str
    ID: int
    version: Any
    @classmethod
    def key_for_entity(cls, entity_or_key): ...

def get_namespaces(start: Any | None = ..., end: Any | None = ...): ...
def get_kinds(start: Any | None = ..., end: Any | None = ...): ...
def get_properties_of_kind(kind, start: Any | None = ..., end: Any | None = ...): ...
def get_representations_of_kind(kind, start: Any | None = ..., end: Any | None = ...): ...
def get_entity_group_version(entity_or_key): ...
