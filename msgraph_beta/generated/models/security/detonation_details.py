from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .detonation_chain import DetonationChain
    from .detonation_observables import DetonationObservables

@dataclass
class DetonationDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The analysisDateTime property
    analysis_date_time: Optional[datetime.datetime] = None
    # The detonationChain property
    detonation_chain: Optional[DetonationChain] = None
    # The detonationObservables property
    detonation_observables: Optional[DetonationObservables] = None
    # The detonationVerdict property
    detonation_verdict: Optional[str] = None
    # The detonationVerdictReason property
    detonation_verdict_reason: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DetonationDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DetonationDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DetonationDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .detonation_chain import DetonationChain
        from .detonation_observables import DetonationObservables

        from .detonation_chain import DetonationChain
        from .detonation_observables import DetonationObservables

        fields: Dict[str, Callable[[Any], None]] = {
            "analysisDateTime": lambda n : setattr(self, 'analysis_date_time', n.get_datetime_value()),
            "detonationChain": lambda n : setattr(self, 'detonation_chain', n.get_object_value(DetonationChain)),
            "detonationObservables": lambda n : setattr(self, 'detonation_observables', n.get_object_value(DetonationObservables)),
            "detonationVerdict": lambda n : setattr(self, 'detonation_verdict', n.get_str_value()),
            "detonationVerdictReason": lambda n : setattr(self, 'detonation_verdict_reason', n.get_str_value()),
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
        writer.write_datetime_value("analysisDateTime", self.analysis_date_time)
        writer.write_object_value("detonationChain", self.detonation_chain)
        writer.write_object_value("detonationObservables", self.detonation_observables)
        writer.write_str_value("detonationVerdict", self.detonation_verdict)
        writer.write_str_value("detonationVerdictReason", self.detonation_verdict_reason)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

