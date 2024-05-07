from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .engagement_async_operation_type import EngagementAsyncOperationType
    from .long_running_operation import LongRunningOperation

from .long_running_operation import LongRunningOperation

@dataclass
class EngagementAsyncOperation(LongRunningOperation):
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of the long-running operation. The possible values are: createCommunity, unknownFutureValue.
    operation_type: Optional[EngagementAsyncOperationType] = None
    # The ID of the object created or modified as a result of this async operation.
    resource_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EngagementAsyncOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EngagementAsyncOperation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EngagementAsyncOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .engagement_async_operation_type import EngagementAsyncOperationType
        from .long_running_operation import LongRunningOperation

        from .engagement_async_operation_type import EngagementAsyncOperationType
        from .long_running_operation import LongRunningOperation

        fields: Dict[str, Callable[[Any], None]] = {
            "operationType": lambda n : setattr(self, 'operation_type', n.get_enum_value(EngagementAsyncOperationType)),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
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
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_str_value("resourceId", self.resource_id)
    

