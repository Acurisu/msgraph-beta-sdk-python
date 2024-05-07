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
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.security.sensor import Sensor
    from ....models.security.sensor_collection_response import SensorCollectionResponse
    from .count.count_request_builder import CountRequestBuilder
    from .item.sensor_item_request_builder import SensorItemRequestBuilder
    from .microsoft_graph_security_get_deployment_access_key.microsoft_graph_security_get_deployment_access_key_request_builder import MicrosoftGraphSecurityGetDeploymentAccessKeyRequestBuilder
    from .microsoft_graph_security_get_deployment_package_uri.microsoft_graph_security_get_deployment_package_uri_request_builder import MicrosoftGraphSecurityGetDeploymentPackageUriRequestBuilder
    from .microsoft_graph_security_regenerate_deployment_access_key.microsoft_graph_security_regenerate_deployment_access_key_request_builder import MicrosoftGraphSecurityRegenerateDeploymentAccessKeyRequestBuilder

class SensorsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the sensors property of the microsoft.graph.security.identityContainer entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new SensorsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/identities/sensors{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_sensor_id(self,sensor_id: str) -> SensorItemRequestBuilder:
        """
        Provides operations to manage the sensors property of the microsoft.graph.security.identityContainer entity.
        param sensor_id: The unique identifier of sensor
        Returns: SensorItemRequestBuilder
        """
        if not sensor_id:
            raise TypeError("sensor_id cannot be null.")
        from .item.sensor_item_request_builder import SensorItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["sensor%2Did"] = sensor_id
        return SensorItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SensorsRequestBuilderGetQueryParameters]] = None) -> Optional[SensorCollectionResponse]:
        """
        Get sensors from security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SensorCollectionResponse]
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
        from ....models.security.sensor_collection_response import SensorCollectionResponse

        return await self.request_adapter.send_async(request_info, SensorCollectionResponse, error_mapping)
    
    async def post(self,body: Sensor, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Sensor]:
        """
        Create new navigation property to sensors for security
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Sensor]
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
        from ....models.security.sensor import Sensor

        return await self.request_adapter.send_async(request_info, Sensor, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SensorsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get sensors from security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Sensor, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create new navigation property to sensors for security
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
    
    def with_url(self,raw_url: str) -> SensorsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SensorsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return SensorsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_security_get_deployment_access_key(self) -> MicrosoftGraphSecurityGetDeploymentAccessKeyRequestBuilder:
        """
        Provides operations to call the getDeploymentAccessKey method.
        """
        from .microsoft_graph_security_get_deployment_access_key.microsoft_graph_security_get_deployment_access_key_request_builder import MicrosoftGraphSecurityGetDeploymentAccessKeyRequestBuilder

        return MicrosoftGraphSecurityGetDeploymentAccessKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_security_get_deployment_package_uri(self) -> MicrosoftGraphSecurityGetDeploymentPackageUriRequestBuilder:
        """
        Provides operations to call the getDeploymentPackageUri method.
        """
        from .microsoft_graph_security_get_deployment_package_uri.microsoft_graph_security_get_deployment_package_uri_request_builder import MicrosoftGraphSecurityGetDeploymentPackageUriRequestBuilder

        return MicrosoftGraphSecurityGetDeploymentPackageUriRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_security_regenerate_deployment_access_key(self) -> MicrosoftGraphSecurityRegenerateDeploymentAccessKeyRequestBuilder:
        """
        Provides operations to call the regenerateDeploymentAccessKey method.
        """
        from .microsoft_graph_security_regenerate_deployment_access_key.microsoft_graph_security_regenerate_deployment_access_key_request_builder import MicrosoftGraphSecurityRegenerateDeploymentAccessKeyRequestBuilder

        return MicrosoftGraphSecurityRegenerateDeploymentAccessKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SensorsRequestBuilderGetQueryParameters():
        """
        Get sensors from security
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
    class SensorsRequestBuilderGetRequestConfiguration(RequestConfiguration[SensorsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SensorsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

