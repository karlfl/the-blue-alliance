from google.appengine.api import datastore_types as datastore_types
from google.appengine.datastore import datastore_pbs as datastore_pbs
from google.appengine.datastore.datastore_pbs import googledatastore as googledatastore
from typing import Any

class ValidationError(Exception): ...

class _ValidationConstraint:
    def __init__(self, absent_key_allowed: bool = ..., incomplete_key_path_allowed: bool = ..., complete_key_path_allowed: bool = ..., reserved_key_allowed: bool = ..., reserved_property_name_allowed: bool = ..., meaning_index_only_allowed: bool = ...) -> None: ...
    @property
    def absent_key_allowed(self): ...
    @property
    def incomplete_key_path_allowed(self): ...
    @property
    def complete_key_path_allowed(self): ...
    @property
    def reserved_key_allowed(self): ...
    @property
    def reserved_property_name_allowed(self): ...
    @property
    def meaning_index_only_allowed(self): ...
    def __hash__(self): ...
    def __eq__(self, other): ...

READ: Any
READ_ENTITY_IN_VALUE: Any
UPSERT: Any
UPSERT_ENTITY_IN_VALUE: Any
UPDATE: Any
DELETE: Any
WRITE_ENTITY_IN_VALUE: Any
ALLOCATE_KEY_ID: Any
KEY_IN_VALUE: Any

class _EntityValidator:
    def validate_keys(self, constraint, keys) -> None: ...
    def validate_key(self, constraint, key) -> None: ...
    def validate_partition_id(self, constraint, partition_id) -> None: ...
    def validate_project_id(self, constraint, project_id) -> None: ...
    def validate_partition_id_dimension(self, constraint, partition_dimension, desc) -> None: ...
    def validate_kind(self, constraint, kind) -> None: ...
    def validate_entities(self, constraint, entities) -> None: ...
    def validate_entity(self, constraint, entity) -> None: ...
    def validate_property(self, constraint, prop) -> None: ...
    def validate_value(self, constraint, value) -> None: ...
    def validate_property_name(self, constraint, property_name) -> None: ...
    def validate_timestamp(self, timestamp) -> None: ...

def get_entity_validator(): ...

class _QueryValidator:
    def __init__(self, entity_validator) -> None: ...
    def validate_query(self, query, is_strong_read_consistency) -> None: ...
    def validate_filter(self, filt) -> None: ...

def get_query_validator(): ...

class _ServiceValidator:
    def __init__(self, entity_validator, query_validator, id_resolver) -> None: ...
    def validate_begin_transaction_req(self, req) -> None: ...
    def validate_rollback_req(self, req) -> None: ...
    def validate_commit_req(self, req) -> None: ...
    def validate_run_query_req(self, req) -> None: ...
    def validate_lookup_req(self, req) -> None: ...
    def validate_allocate_ids_req(self, req) -> None: ...

def get_service_validator(id_resolver): ...
