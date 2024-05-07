from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.managed_tenants.management_template_collection_tenant_summary import ManagementTemplateCollectionTenantSummary
    from ....models.managed_tenants.management_template_collection_tenant_summary_collection_response import ManagementTemplateCollectionTenantSummaryCollectionResponse
    from ....models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .item.management_template_collection_tenant_summary_item_request_builder import ManagementTemplateCollectionTenantSummaryItemRequestBuilder

class ManagementTemplateCollectionTenantSummariesRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the managementTemplateCollectionTenantSummaries property of the microsoft.graph.managedTenants.managedTenant entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ManagementTemplateCollectionTenantSummariesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/tenantRelationships/managedTenants/managementTemplateCollectionTenantSummaries{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_management_template_collection_tenant_summary_id(self,management_template_collection_tenant_summary_id: str) -> ManagementTemplateCollectionTenantSummaryItemRequestBuilder:
        """
        Provides operations to manage the managementTemplateCollectionTenantSummaries property of the microsoft.graph.managedTenants.managedTenant entity.
        param management_template_collection_tenant_summary_id: The unique identifier of managementTemplateCollectionTenantSummary
        Returns: ManagementTemplateCollectionTenantSummaryItemRequestBuilder
        """
        if not management_template_collection_tenant_summary_id:
            raise TypeError("management_template_collection_tenant_summary_id cannot be null.")
        from .item.management_template_collection_tenant_summary_item_request_builder import ManagementTemplateCollectionTenantSummaryItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managementTemplateCollectionTenantSummary%2Did"] = management_template_collection_tenant_summary_id
        return ManagementTemplateCollectionTenantSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ManagementTemplateCollectionTenantSummariesRequestBuilderGetQueryParameters]] = None) -> Optional[ManagementTemplateCollectionTenantSummaryCollectionResponse]:
        """
        Get managementTemplateCollectionTenantSummaries from tenantRelationships
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManagementTemplateCollectionTenantSummaryCollectionResponse]
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
        from ....models.managed_tenants.management_template_collection_tenant_summary_collection_response import ManagementTemplateCollectionTenantSummaryCollectionResponse

        return await self.request_adapter.send_async(request_info, ManagementTemplateCollectionTenantSummaryCollectionResponse, error_mapping)
    
    async def post(self,body: ManagementTemplateCollectionTenantSummary, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ManagementTemplateCollectionTenantSummary]:
        """
        Create new navigation property to managementTemplateCollectionTenantSummaries for tenantRelationships
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManagementTemplateCollectionTenantSummary]
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
        from ....models.managed_tenants.management_template_collection_tenant_summary import ManagementTemplateCollectionTenantSummary

        return await self.request_adapter.send_async(request_info, ManagementTemplateCollectionTenantSummary, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ManagementTemplateCollectionTenantSummariesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get managementTemplateCollectionTenantSummaries from tenantRelationships
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: ManagementTemplateCollectionTenantSummary, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create new navigation property to managementTemplateCollectionTenantSummaries for tenantRelationships
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
    
    def with_url(self,raw_url: str) -> ManagementTemplateCollectionTenantSummariesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ManagementTemplateCollectionTenantSummariesRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ManagementTemplateCollectionTenantSummariesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ManagementTemplateCollectionTenantSummariesRequestBuilderGetQueryParameters():
        """
        Get managementTemplateCollectionTenantSummaries from tenantRelationships
        """
        def get_query_parameter(self,original_name: str) -> str:
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

    
    @dataclass
    class ManagementTemplateCollectionTenantSummariesRequestBuilderGetRequestConfiguration(RequestConfiguration[ManagementTemplateCollectionTenantSummariesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ManagementTemplateCollectionTenantSummariesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

