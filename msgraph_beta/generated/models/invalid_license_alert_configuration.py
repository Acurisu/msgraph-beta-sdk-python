from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

@dataclass
class InvalidLicenseAlertConfiguration(UnifiedRoleManagementAlertConfiguration):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.invalidLicenseAlertConfiguration"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InvalidLicenseAlertConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvalidLicenseAlertConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InvalidLicenseAlertConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

        from .unified_role_management_alert_configuration import UnifiedRoleManagementAlertConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
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
    

