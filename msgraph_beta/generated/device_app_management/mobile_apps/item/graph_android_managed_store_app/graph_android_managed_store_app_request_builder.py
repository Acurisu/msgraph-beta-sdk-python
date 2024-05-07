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
    from .....models.android_managed_store_app import AndroidManagedStoreApp
    from .....models.o_data_errors.o_data_error import ODataError
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .categories.categories_request_builder import CategoriesRequestBuilder
    from .relationships.relationships_request_builder import RelationshipsRequestBuilder

class GraphAndroidManagedStoreAppRequestBuilder(BaseRequestBuilder):
    """
    Casts the previous resource to androidManagedStoreApp.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new GraphAndroidManagedStoreAppRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/mobileApps/{mobileApp%2Did}/graph.androidManagedStoreApp{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[GraphAndroidManagedStoreAppRequestBuilderGetQueryParameters]] = None) -> Optional[AndroidManagedStoreApp]:
        """
        Get the item of type microsoft.graph.mobileApp as microsoft.graph.androidManagedStoreApp
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AndroidManagedStoreApp]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.android_managed_store_app import AndroidManagedStoreApp

        return await self.request_adapter.send_async(request_info, AndroidManagedStoreApp, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[GraphAndroidManagedStoreAppRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get the item of type microsoft.graph.mobileApp as microsoft.graph.androidManagedStoreApp
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> GraphAndroidManagedStoreAppRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GraphAndroidManagedStoreAppRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return GraphAndroidManagedStoreAppRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def assignments(self) -> AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.mobileApp entity.
        """
        from .assignments.assignments_request_builder import AssignmentsRequestBuilder

        return AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def categories(self) -> CategoriesRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.mobileApp entity.
        """
        from .categories.categories_request_builder import CategoriesRequestBuilder

        return CategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def relationships(self) -> RelationshipsRequestBuilder:
        """
        Provides operations to manage the relationships property of the microsoft.graph.mobileApp entity.
        """
        from .relationships.relationships_request_builder import RelationshipsRequestBuilder

        return RelationshipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class GraphAndroidManagedStoreAppRequestBuilderGetQueryParameters():
        """
        Get the item of type microsoft.graph.mobileApp as microsoft.graph.androidManagedStoreApp
        """
        def get_query_parameter(self,original_name: str) -> str:
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

    
    @dataclass
    class GraphAndroidManagedStoreAppRequestBuilderGetRequestConfiguration(RequestConfiguration[GraphAndroidManagedStoreAppRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

