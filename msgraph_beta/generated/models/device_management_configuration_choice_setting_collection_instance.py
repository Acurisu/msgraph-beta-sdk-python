from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_choice_setting_value import DeviceManagementConfigurationChoiceSettingValue
    from .device_management_configuration_setting_instance import DeviceManagementConfigurationSettingInstance

from .device_management_configuration_setting_instance import DeviceManagementConfigurationSettingInstance

@dataclass
class DeviceManagementConfigurationChoiceSettingCollectionInstance(DeviceManagementConfigurationSettingInstance):
    """
    Setting instance within policy
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionInstance"
    # Choice setting collection value
    choice_setting_collection_value: Optional[List[DeviceManagementConfigurationChoiceSettingValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationChoiceSettingCollectionInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationChoiceSettingCollectionInstance
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationChoiceSettingCollectionInstance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_choice_setting_value import DeviceManagementConfigurationChoiceSettingValue
        from .device_management_configuration_setting_instance import DeviceManagementConfigurationSettingInstance

        from .device_management_configuration_choice_setting_value import DeviceManagementConfigurationChoiceSettingValue
        from .device_management_configuration_setting_instance import DeviceManagementConfigurationSettingInstance

        fields: Dict[str, Callable[[Any], None]] = {
            "choiceSettingCollectionValue": lambda n : setattr(self, 'choice_setting_collection_value', n.get_collection_of_object_values(DeviceManagementConfigurationChoiceSettingValue)),
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
        writer.write_collection_of_object_values("choiceSettingCollectionValue", self.choice_setting_collection_value)
    

