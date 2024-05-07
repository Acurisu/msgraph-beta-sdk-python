from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delivery_optimization_bandwidth_absolute import DeliveryOptimizationBandwidthAbsolute
    from .delivery_optimization_bandwidth_hours_with_percentage import DeliveryOptimizationBandwidthHoursWithPercentage
    from .delivery_optimization_bandwidth_percentage import DeliveryOptimizationBandwidthPercentage

@dataclass
class DeliveryOptimizationBandwidth(AdditionalDataHolder, BackedModel, Parsable):
    """
    Bandwidth restriction types
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeliveryOptimizationBandwidth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationBandwidth
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deliveryOptimizationBandwidthAbsolute".casefold():
            from .delivery_optimization_bandwidth_absolute import DeliveryOptimizationBandwidthAbsolute

            return DeliveryOptimizationBandwidthAbsolute()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deliveryOptimizationBandwidthHoursWithPercentage".casefold():
            from .delivery_optimization_bandwidth_hours_with_percentage import DeliveryOptimizationBandwidthHoursWithPercentage

            return DeliveryOptimizationBandwidthHoursWithPercentage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deliveryOptimizationBandwidthPercentage".casefold():
            from .delivery_optimization_bandwidth_percentage import DeliveryOptimizationBandwidthPercentage

            return DeliveryOptimizationBandwidthPercentage()
        return DeliveryOptimizationBandwidth()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .delivery_optimization_bandwidth_absolute import DeliveryOptimizationBandwidthAbsolute
        from .delivery_optimization_bandwidth_hours_with_percentage import DeliveryOptimizationBandwidthHoursWithPercentage
        from .delivery_optimization_bandwidth_percentage import DeliveryOptimizationBandwidthPercentage

        from .delivery_optimization_bandwidth_absolute import DeliveryOptimizationBandwidthAbsolute
        from .delivery_optimization_bandwidth_hours_with_percentage import DeliveryOptimizationBandwidthHoursWithPercentage
        from .delivery_optimization_bandwidth_percentage import DeliveryOptimizationBandwidthPercentage

        fields: Dict[str, Callable[[Any], None]] = {
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

