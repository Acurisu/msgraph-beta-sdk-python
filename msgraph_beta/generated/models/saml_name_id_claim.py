from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_claim_base import CustomClaimBase
    from .saml_name_i_d_format import SamlNameIDFormat

from .custom_claim_base import CustomClaimBase

@dataclass
class SamlNameIdClaim(CustomClaimBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.samlNameIdClaim"
    # The nameIdFormat property
    name_id_format: Optional[SamlNameIDFormat] = None
    # The serviceProviderNameQualifier property
    service_provider_name_qualifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SamlNameIdClaim:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SamlNameIdClaim
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SamlNameIdClaim()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .custom_claim_base import CustomClaimBase
        from .saml_name_i_d_format import SamlNameIDFormat

        from .custom_claim_base import CustomClaimBase
        from .saml_name_i_d_format import SamlNameIDFormat

        fields: Dict[str, Callable[[Any], None]] = {
            "nameIdFormat": lambda n : setattr(self, 'name_id_format', n.get_enum_value(SamlNameIDFormat)),
            "serviceProviderNameQualifier": lambda n : setattr(self, 'service_provider_name_qualifier', n.get_str_value()),
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
        writer.write_enum_value("nameIdFormat", self.name_id_format)
        writer.write_str_value("serviceProviderNameQualifier", self.service_provider_name_qualifier)
    

