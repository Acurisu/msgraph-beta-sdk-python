from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.o_data_errors.o_data_error import ODataError
    from ..models.term_store.store import Store
    from .groups.groups_request_builder import GroupsRequestBuilder
    from .sets.sets_request_builder import SetsRequestBuilder

class TermStoreRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the store singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new TermStoreRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/termStore{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[TermStoreRequestBuilderGetRequestConfiguration] = None) -> Optional[Store]:
        """
        Read the properties and relationships of a store object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Store]
        Find more info here: https://learn.microsoft.com/graph/api/termstore-store-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.term_store.store import Store

        return await self.request_adapter.send_async(request_info, Store, error_mapping)
    
    async def patch(self,body: Optional[Store] = None, request_configuration: Optional[TermStoreRequestBuilderPatchRequestConfiguration] = None) -> Optional[Store]:
        """
        Update the properties of a store object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Store]
        Find more info here: https://learn.microsoft.com/graph/api/termstore-store-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.term_store.store import Store

        return await self.request_adapter.send_async(request_info, Store, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[TermStoreRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties and relationships of a store object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[Store] = None, request_configuration: Optional[TermStoreRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a store object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> TermStoreRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TermStoreRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return TermStoreRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def groups(self) -> GroupsRequestBuilder:
        """
        Provides operations to manage the groups property of the microsoft.graph.termStore.store entity.
        """
        from .groups.groups_request_builder import GroupsRequestBuilder

        return GroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sets(self) -> SetsRequestBuilder:
        """
        Provides operations to manage the sets property of the microsoft.graph.termStore.store entity.
        """
        from .sets.sets_request_builder import SetsRequestBuilder

        return SetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TermStoreRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of a store object.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TermStoreRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[TermStoreRequestBuilder.TermStoreRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TermStoreRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

