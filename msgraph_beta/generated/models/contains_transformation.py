from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_claim_transformation import CustomClaimTransformation
    from .transformation_attribute import TransformationAttribute

from .custom_claim_transformation import CustomClaimTransformation

@dataclass
class ContainsTransformation(CustomClaimTransformation):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.containsTransformation"
    # The output property
    output: Optional[TransformationAttribute] = None
    # The value property
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContainsTransformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContainsTransformation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ContainsTransformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .custom_claim_transformation import CustomClaimTransformation
        from .transformation_attribute import TransformationAttribute

        from .custom_claim_transformation import CustomClaimTransformation
        from .transformation_attribute import TransformationAttribute

        fields: Dict[str, Callable[[Any], None]] = {
            "output": lambda n : setattr(self, 'output', n.get_object_value(TransformationAttribute)),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("output", self.output)
        writer.write_str_value("value", self.value)
    

