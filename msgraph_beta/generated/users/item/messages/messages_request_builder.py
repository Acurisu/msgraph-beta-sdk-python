from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.message import Message
    from ....models.message_collection_response import MessageCollectionResponse
    from ....models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .delta.delta_request_builder import DeltaRequestBuilder
    from .item.message_item_request_builder import MessageItemRequestBuilder

class MessagesRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the messages property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new MessagesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/messages{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top,includeHiddenMessages*}", path_parameters)
    
    def by_message_id(self,message_id: str) -> MessageItemRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.user entity.
        param message_id: The unique identifier of message
        Returns: MessageItemRequestBuilder
        """
        if not message_id:
            raise TypeError("message_id cannot be null.")
        from .item.message_item_request_builder import MessageItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["message%2Did"] = message_id
        return MessageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[MessageCollectionResponse]:
        """
        The messages in a mailbox or folder. Read-only. Nullable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MessageCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/opentypeextension-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.message_collection_response import MessageCollectionResponse

        return await self.request_adapter.send_async(request_info, MessageCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[Message] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[Message]:
        """
        Create an open extension (openTypeExtension object) and add custom properties in a new or existing instance of a resource. You can create an open extension in a resource instance and store custom data to it all in the same operation, except for specific resources. The table in the Permissions section lists the resources that support open extensions.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Message]
        Find more info here: https://learn.microsoft.com/graph/api/opentypeextension-post-opentypeextension?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.message import Message

        return await self.request_adapter.send_async(request_info, Message, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        The messages in a mailbox or folder. Read-only. Nullable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Optional[Message] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Create an open extension (openTypeExtension object) and add custom properties in a new or existing instance of a resource. You can create an open extension in a resource instance and store custom data to it all in the same operation, except for specific resources. The table in the Permissions section lists the resources that support open extensions.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> MessagesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MessagesRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return MessagesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delta(self) -> DeltaRequestBuilder:
        """
        Provides operations to call the delta method.
        """
        from .delta.delta_request_builder import DeltaRequestBuilder

        return DeltaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MessagesRequestBuilderGetQueryParameters():
        """
        The messages in a mailbox or folder. Read-only. Nullable.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "include_hidden_messages":
                return "includeHiddenMessages"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Include Hidden Messages
        include_hidden_messages: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    

