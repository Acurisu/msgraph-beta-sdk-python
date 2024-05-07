from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
    from .entity import Entity

from .entity import Entity

@dataclass
class WindowsQualityUpdateProfileAssignment(Entity):
    """
    This entity contains the properties used to assign a windows quality update profile to a group.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # The assignment target that the quality update profile is assigned to.
    target: Optional[DeviceAndAppManagementAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsQualityUpdateProfileAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsQualityUpdateProfileAssignment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WindowsQualityUpdateProfileAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
        from .entity import Entity

        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "target": lambda n : setattr(self, 'target', n.get_object_value(DeviceAndAppManagementAssignmentTarget)),
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
        writer.write_object_value("target", self.target)
    

