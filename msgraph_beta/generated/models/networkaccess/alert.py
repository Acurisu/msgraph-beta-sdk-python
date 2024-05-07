from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .alert_action import AlertAction
    from .alert_type import AlertType
    from .related_resource import RelatedResource

from ..entity import Entity

@dataclass
class Alert(Entity):
    # The actions property
    actions: Optional[List[AlertAction]] = None
    # The alertType property
    alert_type: Optional[AlertType] = None
    # The creationDateTime property
    creation_date_time: Optional[datetime.datetime] = None
    # The description property
    description: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The relatedResources property
    related_resources: Optional[List[RelatedResource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Alert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Alert
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Alert()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .alert_action import AlertAction
        from .alert_type import AlertType
        from .related_resource import RelatedResource

        from ..entity import Entity
        from .alert_action import AlertAction
        from .alert_type import AlertType
        from .related_resource import RelatedResource

        fields: Dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(AlertAction)),
            "alertType": lambda n : setattr(self, 'alert_type', n.get_enum_value(AlertType)),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "relatedResources": lambda n : setattr(self, 'related_resources', n.get_collection_of_object_values(RelatedResource)),
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
        writer.write_collection_of_object_values("actions", self.actions)
        writer.write_enum_value("alertType", self.alert_type)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("relatedResources", self.related_resources)
    

