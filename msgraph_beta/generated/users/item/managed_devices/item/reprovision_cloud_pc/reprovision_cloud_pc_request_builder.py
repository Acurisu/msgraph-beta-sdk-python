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
from warnings import warn

if TYPE_CHECKING:
    from ......models.o_data_errors.o_data_error import ODataError

class ReprovisionCloudPcRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the reprovisionCloudPc method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ReprovisionCloudPcRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/managedDevices/{managedDevice%2Did}/reprovisionCloudPc", path_parameters)
    
    async def post(self,request_configuration: Optional[ReprovisionCloudPcRequestBuilderPostRequestConfiguration] = None) -> None:
        """
        Reprovision a Cloud PC with an Intune managed device ID.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/manageddevice-reprovisioncloudpc?view=graph-rest-1.0
        """
        warn("The reprovisionCloudPc API is deprecated and will stop returning on Sep 30, 2023. Please use reprovision instead as of 2023-07/reprovisionCloudPc", DeprecationWarning)
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[ReprovisionCloudPcRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Reprovision a Cloud PC with an Intune managed device ID.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("The reprovisionCloudPc API is deprecated and will stop returning on Sep 30, 2023. Please use reprovision instead as of 2023-07/reprovisionCloudPc", DeprecationWarning)
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ReprovisionCloudPcRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ReprovisionCloudPcRequestBuilder
        """
        warn("The reprovisionCloudPc API is deprecated and will stop returning on Sep 30, 2023. Please use reprovision instead as of 2023-07/reprovisionCloudPc", DeprecationWarning)
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ReprovisionCloudPcRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ReprovisionCloudPcRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

