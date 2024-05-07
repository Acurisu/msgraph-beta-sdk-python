from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate
    from .device_management_configuration_simple_setting_value_template import DeviceManagementConfigurationSimpleSettingValueTemplate

from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

@dataclass
class DeviceManagementConfigurationSimpleSettingInstanceTemplate(DeviceManagementConfigurationSettingInstanceTemplate):
    """
    Simple Setting Instance Template
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementConfigurationSimpleSettingInstanceTemplate"
    # Simple Setting Value Template
    simple_setting_value_template: Optional[DeviceManagementConfigurationSimpleSettingValueTemplate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationSimpleSettingInstanceTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSimpleSettingInstanceTemplate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationSimpleSettingInstanceTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate
        from .device_management_configuration_simple_setting_value_template import DeviceManagementConfigurationSimpleSettingValueTemplate

        from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate
        from .device_management_configuration_simple_setting_value_template import DeviceManagementConfigurationSimpleSettingValueTemplate

        fields: Dict[str, Callable[[Any], None]] = {
            "simpleSettingValueTemplate": lambda n : setattr(self, 'simple_setting_value_template', n.get_object_value(DeviceManagementConfigurationSimpleSettingValueTemplate)),
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
        writer.write_object_value("simpleSettingValueTemplate", self.simple_setting_value_template)
    

