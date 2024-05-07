from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .password_settings import PasswordSettings

from .password_settings import PasswordSettings

@dataclass
class SimplePasswordSettings(PasswordSettings):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.industryData.simplePasswordSettings"
    # The password for the user.
    password: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SimplePasswordSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SimplePasswordSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SimplePasswordSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .password_settings import PasswordSettings

        from .password_settings import PasswordSettings

        fields: Dict[str, Callable[[Any], None]] = {
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
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
        writer.write_str_value("password", self.password)
    

