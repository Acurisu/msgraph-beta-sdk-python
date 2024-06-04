from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .restore_artifact_base import RestoreArtifactBase

from .restore_artifact_base import RestoreArtifactBase

@dataclass
class MailboxRestoreArtifact(RestoreArtifactBase):
    # The OdataType property
    odata_type: Optional[str] = None
    # The new restored folder identifier for the user.
    restored_folder_id: Optional[str] = None
    # The new restored folder name.
    restored_folder_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MailboxRestoreArtifact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailboxRestoreArtifact
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MailboxRestoreArtifact()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .restore_artifact_base import RestoreArtifactBase

        from .restore_artifact_base import RestoreArtifactBase

        fields: Dict[str, Callable[[Any], None]] = {
            "restoredFolderId": lambda n : setattr(self, 'restored_folder_id', n.get_str_value()),
            "restoredFolderName": lambda n : setattr(self, 'restored_folder_name', n.get_str_value()),
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
        writer.write_str_value("restoredFolderId", self.restored_folder_id)
    

