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
    from .....models.o_data_errors.o_data_error import ODataError
    from .bulk_resize_post_request_body import BulkResizePostRequestBody
    from .bulk_resize_post_response import BulkResizePostResponse

class BulkResizeRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the bulkResize method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new BulkResizeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/cloudPCs/bulkResize", path_parameters)
    
    async def post(self,body: Optional[BulkResizePostRequestBody] = None, request_configuration: Optional[BulkResizeRequestBuilderPostRequestConfiguration] = None) -> Optional[BulkResizePostResponse]:
        """
        Perform a bulk resize action to resize a group of cloudPCs that have successfully passed validation. If any devices can't be resized, those devices indicate 'resize failed'. The remaining devices are provisioned for the resize process.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BulkResizePostResponse]
        Find more info here: https://learn.microsoft.com/graph/api/cloudpc-bulkresize?view=graph-rest-1.0
        """
        warn("The bulkResize action is deprecated and will stop supporting on September 24, 2023. Please use bulk action entity api. as of 2023-05/bulkResize", DeprecationWarning)
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .bulk_resize_post_response import BulkResizePostResponse

        return await self.request_adapter.send_async(request_info, BulkResizePostResponse, error_mapping)
    
    def to_post_request_information(self,body: Optional[BulkResizePostRequestBody] = None, request_configuration: Optional[BulkResizeRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Perform a bulk resize action to resize a group of cloudPCs that have successfully passed validation. If any devices can't be resized, those devices indicate 'resize failed'. The remaining devices are provisioned for the resize process.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("The bulkResize action is deprecated and will stop supporting on September 24, 2023. Please use bulk action entity api. as of 2023-05/bulkResize", DeprecationWarning)
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> BulkResizeRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: BulkResizeRequestBuilder
        """
        warn("The bulkResize action is deprecated and will stop supporting on September 24, 2023. Please use bulk action entity api. as of 2023-05/bulkResize", DeprecationWarning)
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return BulkResizeRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class BulkResizeRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

