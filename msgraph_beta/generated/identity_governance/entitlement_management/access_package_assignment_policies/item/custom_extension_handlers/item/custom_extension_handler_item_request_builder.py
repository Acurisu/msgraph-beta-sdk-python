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
from warnings import warn

if TYPE_CHECKING:
    from .......models.custom_extension_handler import CustomExtensionHandler
    from .......models.o_data_errors.o_data_error import ODataError
    from .custom_extension.custom_extension_request_builder import CustomExtensionRequestBuilder

class CustomExtensionHandlerItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the customExtensionHandlers property of the microsoft.graph.accessPackageAssignmentPolicy entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new CustomExtensionHandlerItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackageAssignmentPolicies/{accessPackageAssignmentPolicy%2Did}/customExtensionHandlers/{customExtensionHandler%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete navigation property customExtensionHandlers for identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions", DeprecationWarning)
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[CustomExtensionHandler]:
        """
        The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomExtensionHandler]
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions", DeprecationWarning)
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.custom_extension_handler import CustomExtensionHandler

        return await self.request_adapter.send_async(request_info, CustomExtensionHandler, error_mapping)
    
    async def patch(self,body: Optional[CustomExtensionHandler] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[CustomExtensionHandler]:
        """
        Update the navigation property customExtensionHandlers in identityGovernance
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomExtensionHandler]
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions", DeprecationWarning)
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.custom_extension_handler import CustomExtensionHandler

        return await self.request_adapter.send_async(request_info, CustomExtensionHandler, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property customExtensionHandlers for identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions", DeprecationWarning)
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions", DeprecationWarning)
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[CustomExtensionHandler] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property customExtensionHandlers in identityGovernance
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions", DeprecationWarning)
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CustomExtensionHandlerItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CustomExtensionHandlerItemRequestBuilder
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions", DeprecationWarning)
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CustomExtensionHandlerItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def custom_extension(self) -> CustomExtensionRequestBuilder:
        """
        Provides operations to manage the customExtension property of the microsoft.graph.customExtensionHandler entity.
        """
        from .custom_extension.custom_extension_request_builder import CustomExtensionRequestBuilder

        return CustomExtensionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CustomExtensionHandlerItemRequestBuilderGetQueryParameters():
        """
        The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.
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

    

