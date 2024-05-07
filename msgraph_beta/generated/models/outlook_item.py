from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .calendar_sharing_message import CalendarSharingMessage
    from .contact import Contact
    from .entity import Entity
    from .event import Event
    from .event_message import EventMessage
    from .event_message_request import EventMessageRequest
    from .event_message_response import EventMessageResponse
    from .message import Message
    from .note import Note
    from .outlook_task import OutlookTask
    from .post import Post

from .entity import Entity

@dataclass
class OutlookItem(Entity):
    # The categories property
    categories: Optional[List[str]] = None
    # The changeKey property
    change_key: Optional[str] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime.datetime] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OutlookItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OutlookItem
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.calendarSharingMessage".casefold():
            from .calendar_sharing_message import CalendarSharingMessage

            return CalendarSharingMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contact".casefold():
            from .contact import Contact

            return Contact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.event".casefold():
            from .event import Event

            return Event()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessage".casefold():
            from .event_message import EventMessage

            return EventMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessageRequest".casefold():
            from .event_message_request import EventMessageRequest

            return EventMessageRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessageResponse".casefold():
            from .event_message_response import EventMessageResponse

            return EventMessageResponse()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.message".casefold():
            from .message import Message

            return Message()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.note".casefold():
            from .note import Note

            return Note()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.outlookTask".casefold():
            from .outlook_task import OutlookTask

            return OutlookTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.post".casefold():
            from .post import Post

            return Post()
        return OutlookItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .calendar_sharing_message import CalendarSharingMessage
        from .contact import Contact
        from .entity import Entity
        from .event import Event
        from .event_message import EventMessage
        from .event_message_request import EventMessageRequest
        from .event_message_response import EventMessageResponse
        from .message import Message
        from .note import Note
        from .outlook_task import OutlookTask
        from .post import Post

        from .calendar_sharing_message import CalendarSharingMessage
        from .contact import Contact
        from .entity import Entity
        from .event import Event
        from .event_message import EventMessage
        from .event_message_request import EventMessageRequest
        from .event_message_response import EventMessageResponse
        from .message import Message
        from .note import Note
        from .outlook_task import OutlookTask
        from .post import Post

        fields: Dict[str, Callable[[Any], None]] = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "changeKey": lambda n : setattr(self, 'change_key', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_str_value("changeKey", self.change_key)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

