from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.operation_approval_source import OperationApprovalSource

@dataclass
class CancelApprovalPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The approvalSource property
    approval_source: Optional[OperationApprovalSource] = None
    # The justification property
    justification: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CancelApprovalPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CancelApprovalPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CancelApprovalPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.operation_approval_source import OperationApprovalSource

        from .....models.operation_approval_source import OperationApprovalSource

        fields: Dict[str, Callable[[Any], None]] = {
            "approvalSource": lambda n : setattr(self, 'approval_source', n.get_enum_value(OperationApprovalSource)),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
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
        writer.write_enum_value("approvalSource", self.approval_source)
        writer.write_str_value("justification", self.justification)
        writer.write_additional_data_value(self.additional_data)
    

