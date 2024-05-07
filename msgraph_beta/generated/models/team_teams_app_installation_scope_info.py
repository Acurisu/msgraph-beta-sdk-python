from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teams_app_installation_scope_info import TeamsAppInstallationScopeInfo

from .teams_app_installation_scope_info import TeamsAppInstallationScopeInfo

@dataclass
class TeamTeamsAppInstallationScopeInfo(TeamsAppInstallationScopeInfo):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.teamTeamsAppInstallationScopeInfo"
    # The teamId property
    team_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamTeamsAppInstallationScopeInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamTeamsAppInstallationScopeInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamTeamsAppInstallationScopeInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .teams_app_installation_scope_info import TeamsAppInstallationScopeInfo

        from .teams_app_installation_scope_info import TeamsAppInstallationScopeInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "teamId": lambda n : setattr(self, 'team_id', n.get_str_value()),
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
        writer.write_str_value("teamId", self.team_id)
    

