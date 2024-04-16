from __future__ import annotations
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
    from .start_post_response import StartPostResponse

class StartRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the start method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new StartRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/education/synchronizationProfiles/{educationSynchronizationProfile%2Did}/start", path_parameters)
    
    async def post(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[StartPostResponse]:
        """
        Verify the files uploaded to a specific school data synchronization profile in the tenant. If the verification is successful, synchronization starts on the profile. Otherwise, the response contains errors and warnings. If the response contains errors, the synchronization won't start. If the response contains only warnings, synchronization starts.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[StartPostResponse]
        Find more info here: https://learn.microsoft.com/graph/api/educationsynchronizationprofile-start?view=graph-rest-1.0
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .start_post_response import StartPostResponse

        return await self.request_adapter.send_async(request_info, StartPostResponse, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Verify the files uploaded to a specific school data synchronization profile in the tenant. If the verification is successful, synchronization starts on the profile. Otherwise, the response contains errors and warnings. If the response contains errors, the synchronization won't start. If the response contains only warnings, synchronization starts.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> StartRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: StartRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return StartRequestBuilder(self.request_adapter, raw_url)
    

