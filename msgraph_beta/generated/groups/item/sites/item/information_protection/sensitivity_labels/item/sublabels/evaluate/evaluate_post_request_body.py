from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..........models.current_label import CurrentLabel
    from ..........models.discovered_sensitive_type import DiscoveredSensitiveType

@dataclass
class EvaluatePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The currentLabel property
    current_label: Optional[CurrentLabel] = None
    # The discoveredSensitiveTypes property
    discovered_sensitive_types: Optional[List[DiscoveredSensitiveType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EvaluatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EvaluatePostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EvaluatePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..........models.current_label import CurrentLabel
        from ..........models.discovered_sensitive_type import DiscoveredSensitiveType

        from ..........models.current_label import CurrentLabel
        from ..........models.discovered_sensitive_type import DiscoveredSensitiveType

        fields: Dict[str, Callable[[Any], None]] = {
            "currentLabel": lambda n : setattr(self, 'current_label', n.get_object_value(CurrentLabel)),
            "discoveredSensitiveTypes": lambda n : setattr(self, 'discovered_sensitive_types', n.get_collection_of_object_values(DiscoveredSensitiveType)),
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
        writer.write_object_value("currentLabel", self.current_label)
        writer.write_collection_of_object_values("discoveredSensitiveTypes", self.discovered_sensitive_types)
        writer.write_additional_data_value(self.additional_data)
    

