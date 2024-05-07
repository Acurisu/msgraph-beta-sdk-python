from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AnalyzedEmailSenderDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The sender email address in the mail From header, also known as the envelope sender or the P1 sender.
    from_address: Optional[str] = None
    # The IPv4 address of the last detected mail server that relayed the message.
    ipv4: Optional[str] = None
    # The sender email address in the From header, which is visible to email recipients on their email clients. Also known as P2 sender.
    mail_from_address: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalyzedEmailSenderDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalyzedEmailSenderDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AnalyzedEmailSenderDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "fromAddress": lambda n : setattr(self, 'from_address', n.get_str_value()),
            "ipv4": lambda n : setattr(self, 'ipv4', n.get_str_value()),
            "mailFromAddress": lambda n : setattr(self, 'mail_from_address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("fromAddress", self.from_address)
        writer.write_str_value("ipv4", self.ipv4)
        writer.write_str_value("mailFromAddress", self.mail_from_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

