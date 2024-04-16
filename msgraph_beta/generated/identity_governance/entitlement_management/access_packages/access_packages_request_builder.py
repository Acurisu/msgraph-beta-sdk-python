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
    from ....models.access_package import AccessPackage
    from ....models.access_package_collection_response import AccessPackageCollectionResponse
    from ....models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .filter_by_current_user_with_on.filter_by_current_user_with_on_request_builder import FilterByCurrentUserWithOnRequestBuilder
    from .item.access_package_item_request_builder import AccessPackageItemRequestBuilder
    from .search.search_request_builder import SearchRequestBuilder

class AccessPackagesRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the accessPackages property of the microsoft.graph.entitlementManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new AccessPackagesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackages{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_access_package_id(self,access_package_id: str) -> AccessPackageItemRequestBuilder:
        """
        Provides operations to manage the accessPackages property of the microsoft.graph.entitlementManagement entity.
        param access_package_id: The unique identifier of accessPackage
        Returns: AccessPackageItemRequestBuilder
        """
        if not access_package_id:
            raise TypeError("access_package_id cannot be null.")
        from .item.access_package_item_request_builder import AccessPackageItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackage%2Did"] = access_package_id
        return AccessPackageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def filter_by_current_user_with_on(self,on: Optional[str] = None) -> FilterByCurrentUserWithOnRequestBuilder:
        """
        Provides operations to call the filterByCurrentUser method.
        param on: Usage: on='{on}'
        Returns: FilterByCurrentUserWithOnRequestBuilder
        """
        if not on:
            raise TypeError("on cannot be null.")
        from .filter_by_current_user_with_on.filter_by_current_user_with_on_request_builder import FilterByCurrentUserWithOnRequestBuilder

        return FilterByCurrentUserWithOnRequestBuilder(self.request_adapter, self.path_parameters, on)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[AccessPackageCollectionResponse]:
        """
        Retrieve a list of accessPackage objects.  The resulting list includes all the access packages that the caller has access to read, across all catalogs.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackageCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/entitlementmanagement-list-accesspackages?view=graph-rest-1.0
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
        from ....models.access_package_collection_response import AccessPackageCollectionResponse

        return await self.request_adapter.send_async(request_info, AccessPackageCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[AccessPackage] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[AccessPackage]:
        """
        Create a new accessPackage object. The access package will be added to an existing accessPackageCatalog. After the access package is created, you can then create accessPackageAssignmentPolicies which specify how users are assigned to the access package.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessPackage]
        Find more info here: https://learn.microsoft.com/graph/api/entitlementmanagement-post-accesspackages?view=graph-rest-1.0
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
        from ....models.access_package import AccessPackage

        return await self.request_adapter.send_async(request_info, AccessPackage, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve a list of accessPackage objects.  The resulting list includes all the access packages that the caller has access to read, across all catalogs.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Optional[AccessPackage] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Create a new accessPackage object. The access package will be added to an existing accessPackageCatalog. After the access package is created, you can then create accessPackageAssignmentPolicies which specify how users are assigned to the access package.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> AccessPackagesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AccessPackagesRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AccessPackagesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def search(self) -> SearchRequestBuilder:
        """
        Provides operations to call the Search method.
        """
        from .search.search_request_builder import SearchRequestBuilder

        return SearchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AccessPackagesRequestBuilderGetQueryParameters():
        """
        Retrieve a list of accessPackage objects.  The resulting list includes all the access packages that the caller has access to read, across all catalogs.
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

    

