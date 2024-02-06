from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filtering_policy_action import FilteringPolicyAction
    from .web_category import WebCategory

@dataclass
class WebCategoriesSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The action property
    action: Optional[FilteringPolicyAction] = None
    # The number of unique devices that were seen.
    device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of transactions that were seen.
    transaction_count: Optional[int] = None
    # The number of unique Microsoft Entra ID users that were seen.
    user_count: Optional[int] = None
    # The webCategory property
    web_category: Optional[WebCategory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WebCategoriesSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebCategoriesSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WebCategoriesSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .filtering_policy_action import FilteringPolicyAction
        from .web_category import WebCategory

        from .filtering_policy_action import FilteringPolicyAction
        from .web_category import WebCategory

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(FilteringPolicyAction)),
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "transactionCount": lambda n : setattr(self, 'transaction_count', n.get_int_value()),
            "userCount": lambda n : setattr(self, 'user_count', n.get_int_value()),
            "webCategory": lambda n : setattr(self, 'web_category', n.get_object_value(WebCategory)),
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
        writer.write_enum_value("action", self.action)
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("transactionCount", self.transaction_count)
        writer.write_int_value("userCount", self.user_count)
        writer.write_object_value("webCategory", self.web_category)
        writer.write_additional_data_value(self.additional_data)
    

