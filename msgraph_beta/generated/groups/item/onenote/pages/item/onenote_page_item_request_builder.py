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
    from ......models.onenote_page import OnenotePage
    from ......models.o_data_errors.o_data_error import ODataError
    from .content.content_request_builder import ContentRequestBuilder
    from .copy_to_section.copy_to_section_request_builder import CopyToSectionRequestBuilder
    from .onenote_patch_content.onenote_patch_content_request_builder import OnenotePatchContentRequestBuilder
    from .parent_notebook.parent_notebook_request_builder import ParentNotebookRequestBuilder
    from .parent_section.parent_section_request_builder import ParentSectionRequestBuilder
    from .preview.preview_request_builder import PreviewRequestBuilder

class OnenotePageItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the pages property of the microsoft.graph.onenote entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new OnenotePageItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/onenote/pages/{onenotePage%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete a OneNote page.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/page-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[OnenotePage]:
        """
        The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnenotePage]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.onenote_page import OnenotePage

        return await self.request_adapter.send_async(request_info, OnenotePage, error_mapping)
    
    async def patch(self,body: Optional[OnenotePage] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[OnenotePage]:
        """
        Update the navigation property pages in groups
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnenotePage]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.onenote_page import OnenotePage

        return await self.request_adapter.send_async(request_info, OnenotePage, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete a OneNote page.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[OnenotePage] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property pages in groups
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
    
    def with_url(self,raw_url: Optional[str] = None) -> OnenotePageItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OnenotePageItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return OnenotePageItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def content(self) -> ContentRequestBuilder:
        """
        Provides operations to manage the media for the group entity.
        """
        from .content.content_request_builder import ContentRequestBuilder

        return ContentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def copy_to_section(self) -> CopyToSectionRequestBuilder:
        """
        Provides operations to call the copyToSection method.
        """
        from .copy_to_section.copy_to_section_request_builder import CopyToSectionRequestBuilder

        return CopyToSectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def onenote_patch_content(self) -> OnenotePatchContentRequestBuilder:
        """
        Provides operations to call the onenotePatchContent method.
        """
        from .onenote_patch_content.onenote_patch_content_request_builder import OnenotePatchContentRequestBuilder

        return OnenotePatchContentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def parent_notebook(self) -> ParentNotebookRequestBuilder:
        """
        Provides operations to manage the parentNotebook property of the microsoft.graph.onenotePage entity.
        """
        from .parent_notebook.parent_notebook_request_builder import ParentNotebookRequestBuilder

        return ParentNotebookRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def parent_section(self) -> ParentSectionRequestBuilder:
        """
        Provides operations to manage the parentSection property of the microsoft.graph.onenotePage entity.
        """
        from .parent_section.parent_section_request_builder import ParentSectionRequestBuilder

        return ParentSectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def preview(self) -> PreviewRequestBuilder:
        """
        Provides operations to call the preview method.
        """
        from .preview.preview_request_builder import PreviewRequestBuilder

        return PreviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OnenotePageItemRequestBuilderGetQueryParameters():
        """
        The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
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

    

