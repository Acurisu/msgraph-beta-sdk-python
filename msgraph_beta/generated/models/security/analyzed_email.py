from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .analyzed_email_attachment import AnalyzedEmailAttachment
    from .analyzed_email_authentication_detail import AnalyzedEmailAuthenticationDetail
    from .analyzed_email_delivery_detail import AnalyzedEmailDeliveryDetail
    from .analyzed_email_exchange_transport_rule_info import AnalyzedEmailExchangeTransportRuleInfo
    from .analyzed_email_sender_detail import AnalyzedEmailSenderDetail
    from .analyzed_email_url import AnalyzedEmailUrl
    from .antispam_directionality import AntispamDirectionality
    from .threat_type import ThreatType

from ..entity import Entity

@dataclass
class AnalyzedEmail(Entity):
    # The alertIds property
    alert_ids: Optional[List[str]] = None
    # The attachments property
    attachments: Optional[List[AnalyzedEmailAttachment]] = None
    # The attachmentsCount property
    attachments_count: Optional[int] = None
    # The authenticationDetails property
    authentication_details: Optional[AnalyzedEmailAuthenticationDetail] = None
    # The bulkComplaintLevel property
    bulk_complaint_level: Optional[str] = None
    # The contexts property
    contexts: Optional[List[str]] = None
    # The detectionMethods property
    detection_methods: Optional[List[str]] = None
    # The directionality property
    directionality: Optional[AntispamDirectionality] = None
    # The distributionList property
    distribution_list: Optional[str] = None
    # The emailClusterId property
    email_cluster_id: Optional[str] = None
    # The exchangeTransportRules property
    exchange_transport_rules: Optional[List[AnalyzedEmailExchangeTransportRuleInfo]] = None
    # The internetMessageId property
    internet_message_id: Optional[str] = None
    # The language property
    language: Optional[str] = None
    # The latestDelivery property
    latest_delivery: Optional[AnalyzedEmailDeliveryDetail] = None
    # The loggedDateTime property
    logged_date_time: Optional[datetime.datetime] = None
    # The networkMessageId property
    network_message_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The originalDelivery property
    original_delivery: Optional[AnalyzedEmailDeliveryDetail] = None
    # The overrideSources property
    override_sources: Optional[List[str]] = None
    # The phishConfidenceLevel property
    phish_confidence_level: Optional[str] = None
    # The policy property
    policy: Optional[str] = None
    # The policyAction property
    policy_action: Optional[str] = None
    # The recipientEmailAddresses property
    recipient_email_addresses: Optional[List[str]] = None
    # The returnPath property
    return_path: Optional[str] = None
    # The senderDetail property
    sender_detail: Optional[AnalyzedEmailSenderDetail] = None
    # The sizeInBytes property
    size_in_bytes: Optional[int] = None
    # The spamConfidenceLevel property
    spam_confidence_level: Optional[str] = None
    # The subject property
    subject: Optional[str] = None
    # The threatType property
    threat_type: Optional[ThreatType] = None
    # The urls property
    urls: Optional[List[AnalyzedEmailUrl]] = None
    # The urlsCount property
    urls_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AnalyzedEmail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalyzedEmail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AnalyzedEmail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .analyzed_email_attachment import AnalyzedEmailAttachment
        from .analyzed_email_authentication_detail import AnalyzedEmailAuthenticationDetail
        from .analyzed_email_delivery_detail import AnalyzedEmailDeliveryDetail
        from .analyzed_email_exchange_transport_rule_info import AnalyzedEmailExchangeTransportRuleInfo
        from .analyzed_email_sender_detail import AnalyzedEmailSenderDetail
        from .analyzed_email_url import AnalyzedEmailUrl
        from .antispam_directionality import AntispamDirectionality
        from .threat_type import ThreatType

        from ..entity import Entity
        from .analyzed_email_attachment import AnalyzedEmailAttachment
        from .analyzed_email_authentication_detail import AnalyzedEmailAuthenticationDetail
        from .analyzed_email_delivery_detail import AnalyzedEmailDeliveryDetail
        from .analyzed_email_exchange_transport_rule_info import AnalyzedEmailExchangeTransportRuleInfo
        from .analyzed_email_sender_detail import AnalyzedEmailSenderDetail
        from .analyzed_email_url import AnalyzedEmailUrl
        from .antispam_directionality import AntispamDirectionality
        from .threat_type import ThreatType

        fields: Dict[str, Callable[[Any], None]] = {
            "alertIds": lambda n : setattr(self, 'alert_ids', n.get_collection_of_primitive_values(str)),
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(AnalyzedEmailAttachment)),
            "attachmentsCount": lambda n : setattr(self, 'attachments_count', n.get_int_value()),
            "authenticationDetails": lambda n : setattr(self, 'authentication_details', n.get_object_value(AnalyzedEmailAuthenticationDetail)),
            "bulkComplaintLevel": lambda n : setattr(self, 'bulk_complaint_level', n.get_str_value()),
            "contexts": lambda n : setattr(self, 'contexts', n.get_collection_of_primitive_values(str)),
            "detectionMethods": lambda n : setattr(self, 'detection_methods', n.get_collection_of_primitive_values(str)),
            "directionality": lambda n : setattr(self, 'directionality', n.get_enum_value(AntispamDirectionality)),
            "distributionList": lambda n : setattr(self, 'distribution_list', n.get_str_value()),
            "emailClusterId": lambda n : setattr(self, 'email_cluster_id', n.get_str_value()),
            "exchangeTransportRules": lambda n : setattr(self, 'exchange_transport_rules', n.get_collection_of_object_values(AnalyzedEmailExchangeTransportRuleInfo)),
            "internetMessageId": lambda n : setattr(self, 'internet_message_id', n.get_str_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "latestDelivery": lambda n : setattr(self, 'latest_delivery', n.get_object_value(AnalyzedEmailDeliveryDetail)),
            "loggedDateTime": lambda n : setattr(self, 'logged_date_time', n.get_datetime_value()),
            "networkMessageId": lambda n : setattr(self, 'network_message_id', n.get_str_value()),
            "originalDelivery": lambda n : setattr(self, 'original_delivery', n.get_object_value(AnalyzedEmailDeliveryDetail)),
            "overrideSources": lambda n : setattr(self, 'override_sources', n.get_collection_of_primitive_values(str)),
            "phishConfidenceLevel": lambda n : setattr(self, 'phish_confidence_level', n.get_str_value()),
            "policy": lambda n : setattr(self, 'policy', n.get_str_value()),
            "policyAction": lambda n : setattr(self, 'policy_action', n.get_str_value()),
            "recipientEmailAddresses": lambda n : setattr(self, 'recipient_email_addresses', n.get_collection_of_primitive_values(str)),
            "returnPath": lambda n : setattr(self, 'return_path', n.get_str_value()),
            "senderDetail": lambda n : setattr(self, 'sender_detail', n.get_object_value(AnalyzedEmailSenderDetail)),
            "sizeInBytes": lambda n : setattr(self, 'size_in_bytes', n.get_int_value()),
            "spamConfidenceLevel": lambda n : setattr(self, 'spam_confidence_level', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "threatType": lambda n : setattr(self, 'threat_type', n.get_enum_value(ThreatType)),
            "urls": lambda n : setattr(self, 'urls', n.get_collection_of_object_values(AnalyzedEmailUrl)),
            "urlsCount": lambda n : setattr(self, 'urls_count', n.get_int_value()),
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
        writer.write_collection_of_primitive_values("alertIds", self.alert_ids)
        writer.write_collection_of_object_values("attachments", self.attachments)
        writer.write_int_value("attachmentsCount", self.attachments_count)
        writer.write_object_value("authenticationDetails", self.authentication_details)
        writer.write_str_value("bulkComplaintLevel", self.bulk_complaint_level)
        writer.write_collection_of_primitive_values("contexts", self.contexts)
        writer.write_collection_of_primitive_values("detectionMethods", self.detection_methods)
        writer.write_enum_value("directionality", self.directionality)
        writer.write_str_value("distributionList", self.distribution_list)
        writer.write_str_value("emailClusterId", self.email_cluster_id)
        writer.write_collection_of_object_values("exchangeTransportRules", self.exchange_transport_rules)
        writer.write_str_value("internetMessageId", self.internet_message_id)
        writer.write_str_value("language", self.language)
        writer.write_object_value("latestDelivery", self.latest_delivery)
        writer.write_datetime_value("loggedDateTime", self.logged_date_time)
        writer.write_str_value("networkMessageId", self.network_message_id)
        writer.write_object_value("originalDelivery", self.original_delivery)
        writer.write_collection_of_primitive_values("overrideSources", self.override_sources)
        writer.write_str_value("phishConfidenceLevel", self.phish_confidence_level)
        writer.write_str_value("policy", self.policy)
        writer.write_str_value("policyAction", self.policy_action)
        writer.write_collection_of_primitive_values("recipientEmailAddresses", self.recipient_email_addresses)
        writer.write_str_value("returnPath", self.return_path)
        writer.write_object_value("senderDetail", self.sender_detail)
        writer.write_int_value("sizeInBytes", self.size_in_bytes)
        writer.write_str_value("spamConfidenceLevel", self.spam_confidence_level)
        writer.write_str_value("subject", self.subject)
        writer.write_enum_value("threatType", self.threat_type)
        writer.write_collection_of_object_values("urls", self.urls)
        writer.write_int_value("urlsCount", self.urls_count)
    

