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
    from ....models.group_policy_definition import GroupPolicyDefinition
    from ....models.o_data_errors.o_data_error import ODataError
    from .category.category_request_builder import CategoryRequestBuilder
    from .definition_file.definition_file_request_builder import DefinitionFileRequestBuilder
    from .next_version_definition.next_version_definition_request_builder import NextVersionDefinitionRequestBuilder
    from .presentations.presentations_request_builder import PresentationsRequestBuilder
    from .previous_version_definition.previous_version_definition_request_builder import PreviousVersionDefinitionRequestBuilder

class GroupPolicyDefinitionItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the groupPolicyDefinitions property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new GroupPolicyDefinitionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/groupPolicyDefinitions/{groupPolicyDefinition%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete navigation property groupPolicyDefinitions for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[GroupPolicyDefinition]:
        """
        The available group policy definitions for this account.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GroupPolicyDefinition]
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
        from ....models.group_policy_definition import GroupPolicyDefinition

        return await self.request_adapter.send_async(request_info, GroupPolicyDefinition, error_mapping)
    
    async def patch(self,body: Optional[GroupPolicyDefinition] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[GroupPolicyDefinition]:
        """
        Update the navigation property groupPolicyDefinitions in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GroupPolicyDefinition]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.group_policy_definition import GroupPolicyDefinition

        return await self.request_adapter.send_async(request_info, GroupPolicyDefinition, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property groupPolicyDefinitions for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        The available group policy definitions for this account.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[GroupPolicyDefinition] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property groupPolicyDefinitions in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> GroupPolicyDefinitionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GroupPolicyDefinitionItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return GroupPolicyDefinitionItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def category(self) -> CategoryRequestBuilder:
        """
        Provides operations to manage the category property of the microsoft.graph.groupPolicyDefinition entity.
        """
        from .category.category_request_builder import CategoryRequestBuilder

        return CategoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def definition_file(self) -> DefinitionFileRequestBuilder:
        """
        Provides operations to manage the definitionFile property of the microsoft.graph.groupPolicyDefinition entity.
        """
        from .definition_file.definition_file_request_builder import DefinitionFileRequestBuilder

        return DefinitionFileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def next_version_definition(self) -> NextVersionDefinitionRequestBuilder:
        """
        Provides operations to manage the nextVersionDefinition property of the microsoft.graph.groupPolicyDefinition entity.
        """
        from .next_version_definition.next_version_definition_request_builder import NextVersionDefinitionRequestBuilder

        return NextVersionDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def presentations(self) -> PresentationsRequestBuilder:
        """
        Provides operations to manage the presentations property of the microsoft.graph.groupPolicyDefinition entity.
        """
        from .presentations.presentations_request_builder import PresentationsRequestBuilder

        return PresentationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def previous_version_definition(self) -> PreviousVersionDefinitionRequestBuilder:
        """
        Provides operations to manage the previousVersionDefinition property of the microsoft.graph.groupPolicyDefinition entity.
        """
        from .previous_version_definition.previous_version_definition_request_builder import PreviousVersionDefinitionRequestBuilder

        return PreviousVersionDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class GroupPolicyDefinitionItemRequestBuilderGetQueryParameters():
        """
        The available group policy definitions for this account.
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

    

