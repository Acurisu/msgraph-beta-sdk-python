from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .association import Association

from .association import Association

@dataclass
class AssociatedBranch(Association):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.associatedBranch"
    # Identifier for the branch.
    branch_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AssociatedBranch:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssociatedBranch
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AssociatedBranch()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .association import Association

        from .association import Association

        fields: Dict[str, Callable[[Any], None]] = {
            "branchId": lambda n : setattr(self, 'branch_id', n.get_str_value()),
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
        writer.write_str_value("branchId", self.branch_id)
    

