from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_and_app_management_assignment_source import DeviceAndAppManagementAssignmentSource
    from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
    from .entity import Entity
    from .install_intent import InstallIntent
    from .mobile_app_assignment_settings import MobileAppAssignmentSettings

from .entity import Entity

@dataclass
class MobileAppAssignment(Entity):
    """
    A class containing the properties used for Group Assignment of a Mobile App.
    """
    # Possible values for the install intent chosen by the admin.
    intent: Optional[InstallIntent] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The settings for target assignment defined by the admin.
    settings: Optional[MobileAppAssignmentSettings] = None
    # Represents source of assignment.
    source: Optional[DeviceAndAppManagementAssignmentSource] = None
    # The identifier of the source of the assignment. This property is read-only.
    source_id: Optional[str] = None
    # The target group assignment defined by the admin.
    target: Optional[DeviceAndAppManagementAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppAssignment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MobileAppAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_and_app_management_assignment_source import DeviceAndAppManagementAssignmentSource
        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
        from .entity import Entity
        from .install_intent import InstallIntent
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings

        from .device_and_app_management_assignment_source import DeviceAndAppManagementAssignmentSource
        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
        from .entity import Entity
        from .install_intent import InstallIntent
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings

        fields: Dict[str, Callable[[Any], None]] = {
            "intent": lambda n : setattr(self, 'intent', n.get_enum_value(InstallIntent)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(MobileAppAssignmentSettings)),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(DeviceAndAppManagementAssignmentSource)),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
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
        writer.write_enum_value("intent", self.intent)
        writer.write_object_value("settings", self.settings)
        writer.write_enum_value("source", self.source)
        writer.write_object_value("target", self.target)
    

