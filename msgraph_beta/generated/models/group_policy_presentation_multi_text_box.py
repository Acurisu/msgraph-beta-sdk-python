from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

@dataclass
class GroupPolicyPresentationMultiTextBox(GroupPolicyUploadedPresentation):
    """
    Represents an ADMX multiTextBox element and an ADMX multiText element.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.groupPolicyPresentationMultiTextBox"
    # An unsigned integer that specifies the maximum number of text characters. Default value is 1023.
    max_length: Optional[int] = None
    # An unsigned integer that specifies the maximum number of strings. Default value is 0.
    max_strings: Optional[int] = None
    # Requirement to enter a value in the text box. Default value is false.
    required: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupPolicyPresentationMultiTextBox:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationMultiTextBox
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyPresentationMultiTextBox()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

        from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

        fields: Dict[str, Callable[[Any], None]] = {
            "maxLength": lambda n : setattr(self, 'max_length', n.get_int_value()),
            "maxStrings": lambda n : setattr(self, 'max_strings', n.get_int_value()),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
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
        writer.write_int_value("maxLength", self.max_length)
        writer.write_int_value("maxStrings", self.max_strings)
        writer.write_bool_value("required", self.required)
    

