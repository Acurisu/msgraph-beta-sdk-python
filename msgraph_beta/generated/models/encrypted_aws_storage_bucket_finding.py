from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_resource import AuthorizationSystemResource
    from .aws_access_type import AwsAccessType
    from .finding import Finding

from .finding import Finding

@dataclass
class EncryptedAwsStorageBucketFinding(Finding):
    # The accessibility property
    accessibility: Optional[AwsAccessType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The storageBucket property
    storage_bucket: Optional[AuthorizationSystemResource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EncryptedAwsStorageBucketFinding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EncryptedAwsStorageBucketFinding
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EncryptedAwsStorageBucketFinding()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_resource import AuthorizationSystemResource
        from .aws_access_type import AwsAccessType
        from .finding import Finding

        from .authorization_system_resource import AuthorizationSystemResource
        from .aws_access_type import AwsAccessType
        from .finding import Finding

        fields: Dict[str, Callable[[Any], None]] = {
            "accessibility": lambda n : setattr(self, 'accessibility', n.get_enum_value(AwsAccessType)),
            "storageBucket": lambda n : setattr(self, 'storage_bucket', n.get_object_value(AuthorizationSystemResource)),
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
        writer.write_enum_value("accessibility", self.accessibility)
        writer.write_object_value("storageBucket", self.storage_bucket)
    

