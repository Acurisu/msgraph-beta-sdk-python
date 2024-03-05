from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_grading_scheme_grade import EducationGradingSchemeGrade
    from .entity import Entity

from .entity import Entity

@dataclass
class EducationGradingScheme(Entity):
    # The displayName property
    display_name: Optional[str] = None
    # The grades property
    grades: Optional[List[EducationGradingSchemeGrade]] = None
    # The hidePointsDuringGrading property
    hide_points_during_grading: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationGradingScheme:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationGradingScheme
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EducationGradingScheme()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_grading_scheme_grade import EducationGradingSchemeGrade
        from .entity import Entity

        from .education_grading_scheme_grade import EducationGradingSchemeGrade
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "grades": lambda n : setattr(self, 'grades', n.get_collection_of_object_values(EducationGradingSchemeGrade)),
            "hidePointsDuringGrading": lambda n : setattr(self, 'hide_points_during_grading', n.get_bool_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("grades", self.grades)
        writer.write_bool_value("hidePointsDuringGrading", self.hide_points_during_grading)
    

