from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .trust_framework_key_set import TrustFrameworkKeySet
    from .trust_framework_policy import TrustFrameworkPolicy

@dataclass
class TrustFramework(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The keySets property
    key_sets: Optional[List[TrustFrameworkKeySet]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policies property
    policies: Optional[List[TrustFrameworkPolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TrustFramework:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrustFramework
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TrustFramework()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .trust_framework_key_set import TrustFrameworkKeySet
        from .trust_framework_policy import TrustFrameworkPolicy

        from .trust_framework_key_set import TrustFrameworkKeySet
        from .trust_framework_policy import TrustFrameworkPolicy

        fields: Dict[str, Callable[[Any], None]] = {
            "keySets": lambda n : setattr(self, 'key_sets', n.get_collection_of_object_values(TrustFrameworkKeySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policies": lambda n : setattr(self, 'policies', n.get_collection_of_object_values(TrustFrameworkPolicy)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("keySets", self.key_sets)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("policies", self.policies)
        writer.write_additional_data_value(self.additional_data)
    

