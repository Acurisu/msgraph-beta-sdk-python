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
    from .....models.o_data_errors.o_data_error import ODataError
    from .get_provisioned_cloud_p_cs_with_group_id_with_service_plan_id_get_response import GetProvisionedCloudPCsWithGroupIdWithServicePlanIdGetResponse

class GetProvisionedCloudPCsWithGroupIdWithServicePlanIdRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the getProvisionedCloudPCs method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]], group_id: Optional[str] = None, service_plan_id: Optional[str] = None) -> None:
        """
        Instantiates a new GetProvisionedCloudPCsWithGroupIdWithServicePlanIdRequestBuilder and sets the default values.
        param group_id: Usage: groupId='{groupId}'
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        param service_plan_id: Usage: servicePlanId='{servicePlanId}'
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['groupId'] = str(group_id)
            path_parameters['servicePlanId'] = str(service_plan_id)
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/cloudPCs/getProvisionedCloudPCs(groupId='{groupId}',servicePlanId='{servicePlanId}'){?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[GetProvisionedCloudPCsWithGroupIdWithServicePlanIdGetResponse]:
        """
        Invoke function getProvisionedCloudPCs
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GetProvisionedCloudPCsWithGroupIdWithServicePlanIdGetResponse]
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
        from .get_provisioned_cloud_p_cs_with_group_id_with_service_plan_id_get_response import GetProvisionedCloudPCsWithGroupIdWithServicePlanIdGetResponse

        return await self.request_adapter.send_async(request_info, GetProvisionedCloudPCsWithGroupIdWithServicePlanIdGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Invoke function getProvisionedCloudPCs
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> GetProvisionedCloudPCsWithGroupIdWithServicePlanIdRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GetProvisionedCloudPCsWithGroupIdWithServicePlanIdRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return GetProvisionedCloudPCsWithGroupIdWithServicePlanIdRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class GetProvisionedCloudPCsWithGroupIdWithServicePlanIdRequestBuilderGetQueryParameters():
        """
        Invoke function getProvisionedCloudPCs
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

    

