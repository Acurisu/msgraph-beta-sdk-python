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
    from .....models.virtual_event_webinar import VirtualEventWebinar
    from .presenters.presenters_request_builder import PresentersRequestBuilder
    from .registrations.registrations_request_builder import RegistrationsRequestBuilder
    from .registrations_with_email.registrations_with_email_request_builder import RegistrationsWithEmailRequestBuilder
    from .registrations_with_user_id.registrations_with_user_id_request_builder import RegistrationsWithUserIdRequestBuilder
    from .registration_configuration.registration_configuration_request_builder import RegistrationConfigurationRequestBuilder
    from .sessions.sessions_request_builder import SessionsRequestBuilder
    from .sessions_with_join_web_url.sessions_with_join_web_url_request_builder import SessionsWithJoinWebUrlRequestBuilder

class VirtualEventWebinarItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the webinars property of the microsoft.graph.virtualEventsRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new VirtualEventWebinarItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/solutions/virtualEvents/webinars/{virtualEventWebinar%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete navigation property webinars for solutions
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[VirtualEventWebinar]:
        """
        Read the properties and relationships of a virtualEventWebinar object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VirtualEventWebinar]
        Find more info here: https://learn.microsoft.com/graph/api/virtualeventwebinar-get?view=graph-rest-1.0
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
        from .....models.virtual_event_webinar import VirtualEventWebinar

        return await self.request_adapter.send_async(request_info, VirtualEventWebinar, error_mapping)
    
    async def patch(self,body: Optional[VirtualEventWebinar] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[VirtualEventWebinar]:
        """
        Update the navigation property webinars in solutions
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[VirtualEventWebinar]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.virtual_event_webinar import VirtualEventWebinar

        return await self.request_adapter.send_async(request_info, VirtualEventWebinar, error_mapping)
    
    def registrations_with_email(self,email: Optional[str] = None) -> RegistrationsWithEmailRequestBuilder:
        """
        Provides operations to manage the registrations property of the microsoft.graph.virtualEventWebinar entity.
        param email: Alternate key of virtualEventRegistration
        Returns: RegistrationsWithEmailRequestBuilder
        """
        if not email:
            raise TypeError("email cannot be null.")
        from .registrations_with_email.registrations_with_email_request_builder import RegistrationsWithEmailRequestBuilder

        return RegistrationsWithEmailRequestBuilder(self.request_adapter, self.path_parameters, email)
    
    def registrations_with_user_id(self,user_id: Optional[str] = None) -> RegistrationsWithUserIdRequestBuilder:
        """
        Provides operations to manage the registrations property of the microsoft.graph.virtualEventWebinar entity.
        param user_id: Alternate key of virtualEventRegistration
        Returns: RegistrationsWithUserIdRequestBuilder
        """
        if not user_id:
            raise TypeError("user_id cannot be null.")
        from .registrations_with_user_id.registrations_with_user_id_request_builder import RegistrationsWithUserIdRequestBuilder

        return RegistrationsWithUserIdRequestBuilder(self.request_adapter, self.path_parameters, user_id)
    
    def sessions_with_join_web_url(self,join_web_url: Optional[str] = None) -> SessionsWithJoinWebUrlRequestBuilder:
        """
        Provides operations to manage the sessions property of the microsoft.graph.virtualEvent entity.
        param join_web_url: Alternate key of virtualEventSession
        Returns: SessionsWithJoinWebUrlRequestBuilder
        """
        if not join_web_url:
            raise TypeError("join_web_url cannot be null.")
        from .sessions_with_join_web_url.sessions_with_join_web_url_request_builder import SessionsWithJoinWebUrlRequestBuilder

        return SessionsWithJoinWebUrlRequestBuilder(self.request_adapter, self.path_parameters, join_web_url)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property webinars for solutions
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/solutions/virtualEvents/webinars/{virtualEventWebinar%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties and relationships of a virtualEventWebinar object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[VirtualEventWebinar] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property webinars in solutions
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, '{+baseurl}/solutions/virtualEvents/webinars/{virtualEventWebinar%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> VirtualEventWebinarItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: VirtualEventWebinarItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return VirtualEventWebinarItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def presenters(self) -> PresentersRequestBuilder:
        """
        Provides operations to manage the presenters property of the microsoft.graph.virtualEvent entity.
        """
        from .presenters.presenters_request_builder import PresentersRequestBuilder

        return PresentersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def registration_configuration(self) -> RegistrationConfigurationRequestBuilder:
        """
        Provides operations to manage the registrationConfiguration property of the microsoft.graph.virtualEventWebinar entity.
        """
        from .registration_configuration.registration_configuration_request_builder import RegistrationConfigurationRequestBuilder

        return RegistrationConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def registrations(self) -> RegistrationsRequestBuilder:
        """
        Provides operations to manage the registrations property of the microsoft.graph.virtualEventWebinar entity.
        """
        from .registrations.registrations_request_builder import RegistrationsRequestBuilder

        return RegistrationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sessions(self) -> SessionsRequestBuilder:
        """
        Provides operations to manage the sessions property of the microsoft.graph.virtualEvent entity.
        """
        from .sessions.sessions_request_builder import SessionsRequestBuilder

        return SessionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class VirtualEventWebinarItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of a virtualEventWebinar object.
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

    

