from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .link_role_abilities import LinkRoleAbilities

@dataclass
class LinkScopeAbilities(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The blockDownload link abilities.
    block_download_link_abilities: Optional[LinkRoleAbilities] = None
    # The editLinkAbilities property
    edit_link_abilities: Optional[LinkRoleAbilities] = None
    # The manageList link abilities.
    manage_list_link_abilities: Optional[LinkRoleAbilities] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The readLinkAbilities property
    read_link_abilities: Optional[LinkRoleAbilities] = None
    # The review link abilities.
    review_link_abilities: Optional[LinkRoleAbilities] = None
    # The submitOnly link abilities.
    submit_only_link_abilities: Optional[LinkRoleAbilities] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LinkScopeAbilities:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LinkScopeAbilities
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LinkScopeAbilities()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .link_role_abilities import LinkRoleAbilities

        from .link_role_abilities import LinkRoleAbilities

        fields: Dict[str, Callable[[Any], None]] = {
            "blockDownloadLinkAbilities": lambda n : setattr(self, 'block_download_link_abilities', n.get_object_value(LinkRoleAbilities)),
            "editLinkAbilities": lambda n : setattr(self, 'edit_link_abilities', n.get_object_value(LinkRoleAbilities)),
            "manageListLinkAbilities": lambda n : setattr(self, 'manage_list_link_abilities', n.get_object_value(LinkRoleAbilities)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "readLinkAbilities": lambda n : setattr(self, 'read_link_abilities', n.get_object_value(LinkRoleAbilities)),
            "reviewLinkAbilities": lambda n : setattr(self, 'review_link_abilities', n.get_object_value(LinkRoleAbilities)),
            "submitOnlyLinkAbilities": lambda n : setattr(self, 'submit_only_link_abilities', n.get_object_value(LinkRoleAbilities)),
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
        writer.write_object_value("blockDownloadLinkAbilities", self.block_download_link_abilities)
        writer.write_object_value("editLinkAbilities", self.edit_link_abilities)
        writer.write_object_value("manageListLinkAbilities", self.manage_list_link_abilities)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("readLinkAbilities", self.read_link_abilities)
        writer.write_object_value("reviewLinkAbilities", self.review_link_abilities)
        writer.write_object_value("submitOnlyLinkAbilities", self.submit_only_link_abilities)
        writer.write_additional_data_value(self.additional_data)
    

