from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .security_alert_status import SecurityAlertStatus

@dataclass
class ActivityLog(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The statusFrom property
    status_from: Optional[SecurityAlertStatus] = None
    # The statusTo property
    status_to: Optional[SecurityAlertStatus] = None
    # The updatedBy property
    updated_by: Optional[str] = None
    # The updatedDateTime property
    updated_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ActivityLog:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActivityLog
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ActivityLog()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .security_alert_status import SecurityAlertStatus

        from .security_alert_status import SecurityAlertStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "statusFrom": lambda n : setattr(self, 'status_from', n.get_enum_value(SecurityAlertStatus)),
            "statusTo": lambda n : setattr(self, 'status_to', n.get_enum_value(SecurityAlertStatus)),
            "updatedBy": lambda n : setattr(self, 'updated_by', n.get_str_value()),
            "updatedDateTime": lambda n : setattr(self, 'updated_date_time', n.get_datetime_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("statusFrom", self.status_from)
        writer.write_enum_value("statusTo", self.status_to)
        writer.write_str_value("updatedBy", self.updated_by)
        writer.write_datetime_value("updatedDateTime", self.updated_date_time)
        writer.write_additional_data_value(self.additional_data)
    

