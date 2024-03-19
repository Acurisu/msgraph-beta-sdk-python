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
    from .......models.custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension
    from .......models.o_data_errors.o_data_error import ODataError

class CustomAccessPackageWorkflowExtensionItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the customAccessPackageWorkflowExtensions property of the microsoft.graph.accessPackageCatalog entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new CustomAccessPackageWorkflowExtensionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackageCatalogs/{accessPackageCatalog%2Did}/customAccessPackageWorkflowExtensions/{customAccessPackageWorkflowExtension%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete an accessPackageAssignmentWorkflowExtension object. The custom workflow extension must first be removed from any associated policies before it can be deleted. Follow these steps to remove the custom workflow extension from any associated policies:1. First retrieve the accessPackageCatalogId by calling the Get accessPackageAssignmentPolicies operation and appending ?$expand=accessPackage($expand=accessPackageCatalog) to the query. For example, https://graph.microsoft.com/beta/identityGovernance/entitlementManagement/accessPackageAssignmentPolicies?$expand=accessPackage($expand=accessPackageCatalog).2. Use the access package catalog ID and retrieve the ID of the accessPackageCustomWorkflowExtension object that you want to delete by running the List accessPackageCustomWorkflowExtensions operation.3. Call the Update accessPackageAssignmentPolicy operation to remove the custom workflow extension object from the policy. For an example, see Example 3: Remove the customExtensionStageSettings from a policy.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/accesspackageassignmentworkflowextension-delete?view=graph-rest-1.0
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[CustomAccessPackageWorkflowExtension]:
        """
        Read the properties and relationships of a customAccessPackageWorkflowExtension object for an accessPackageCatalog object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomAccessPackageWorkflowExtension]
        Find more info here: https://learn.microsoft.com/graph/api/customaccesspackageworkflowextension-get?view=graph-rest-1.0
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
        from .......models.custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension

        return await self.request_adapter.send_async(request_info, CustomAccessPackageWorkflowExtension, error_mapping)
    
    async def patch(self,body: Optional[CustomAccessPackageWorkflowExtension] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[CustomAccessPackageWorkflowExtension]:
        """
        Update the properties of an existing customAccessPackageWorkflowExtension object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomAccessPackageWorkflowExtension]
        Find more info here: https://learn.microsoft.com/graph/api/customaccesspackageworkflowextension-update?view=graph-rest-1.0
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
        from .......models.custom_access_package_workflow_extension import CustomAccessPackageWorkflowExtension

        return await self.request_adapter.send_async(request_info, CustomAccessPackageWorkflowExtension, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete an accessPackageAssignmentWorkflowExtension object. The custom workflow extension must first be removed from any associated policies before it can be deleted. Follow these steps to remove the custom workflow extension from any associated policies:1. First retrieve the accessPackageCatalogId by calling the Get accessPackageAssignmentPolicies operation and appending ?$expand=accessPackage($expand=accessPackageCatalog) to the query. For example, https://graph.microsoft.com/beta/identityGovernance/entitlementManagement/accessPackageAssignmentPolicies?$expand=accessPackage($expand=accessPackageCatalog).2. Use the access package catalog ID and retrieve the ID of the accessPackageCustomWorkflowExtension object that you want to delete by running the List accessPackageCustomWorkflowExtensions operation.3. Call the Update accessPackageAssignmentPolicy operation to remove the custom workflow extension object from the policy. For an example, see Example 3: Remove the customExtensionStageSettings from a policy.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions", DeprecationWarning)
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/identityGovernance/entitlementManagement/accessPackageCatalogs/{accessPackageCatalog%2Did}/customAccessPackageWorkflowExtensions/{customAccessPackageWorkflowExtension%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties and relationships of a customAccessPackageWorkflowExtension object for an accessPackageCatalog object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions", DeprecationWarning)
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[CustomAccessPackageWorkflowExtension] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of an existing customAccessPackageWorkflowExtension object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions", DeprecationWarning)
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, '{+baseurl}/identityGovernance/entitlementManagement/accessPackageCatalogs/{accessPackageCatalog%2Did}/customAccessPackageWorkflowExtensions/{customAccessPackageWorkflowExtension%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CustomAccessPackageWorkflowExtensionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CustomAccessPackageWorkflowExtensionItemRequestBuilder
        """
        warn(" as of 2022-10/PrivatePreview:MicrosofEntitlementManagementCustomextensions", DeprecationWarning)
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CustomAccessPackageWorkflowExtensionItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CustomAccessPackageWorkflowExtensionItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of a customAccessPackageWorkflowExtension object for an accessPackageCatalog object.
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

    

