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
    from ....models.managed_device import ManagedDevice
    from ....models.managed_device_collection_response import ManagedDeviceCollectionResponse
    from ....models.o_data_errors.o_data_error import ODataError
    from .app_diagnostics_with_upn.app_diagnostics_with_upn_request_builder import AppDiagnosticsWithUpnRequestBuilder
    from .bulk_reprovision_cloud_pc.bulk_reprovision_cloud_pc_request_builder import BulkReprovisionCloudPcRequestBuilder
    from .bulk_restore_cloud_pc.bulk_restore_cloud_pc_request_builder import BulkRestoreCloudPcRequestBuilder
    from .bulk_set_cloud_pc_review_status.bulk_set_cloud_pc_review_status_request_builder import BulkSetCloudPcReviewStatusRequestBuilder
    from .count.count_request_builder import CountRequestBuilder
    from .download_app_diagnostics.download_app_diagnostics_request_builder import DownloadAppDiagnosticsRequestBuilder
    from .execute_action.execute_action_request_builder import ExecuteActionRequestBuilder
    from .item.managed_device_item_request_builder import ManagedDeviceItemRequestBuilder
    from .move_devices_to_o_u.move_devices_to_o_u_request_builder import MoveDevicesToOURequestBuilder

class ManagedDevicesRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the managedDevices property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ManagedDevicesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/managedDevices{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def app_diagnostics_with_upn(self,upn: str) -> AppDiagnosticsWithUpnRequestBuilder:
        """
        Provides operations to call the appDiagnostics method.
        param upn: Usage: upn='{upn}'
        Returns: AppDiagnosticsWithUpnRequestBuilder
        """
        if not upn:
            raise TypeError("upn cannot be null.")
        from .app_diagnostics_with_upn.app_diagnostics_with_upn_request_builder import AppDiagnosticsWithUpnRequestBuilder

        return AppDiagnosticsWithUpnRequestBuilder(self.request_adapter, self.path_parameters, upn)
    
    def by_managed_device_id(self,managed_device_id: str) -> ManagedDeviceItemRequestBuilder:
        """
        Provides operations to manage the managedDevices property of the microsoft.graph.user entity.
        param managed_device_id: The unique identifier of managedDevice
        Returns: ManagedDeviceItemRequestBuilder
        """
        if not managed_device_id:
            raise TypeError("managed_device_id cannot be null.")
        from .item.managed_device_item_request_builder import ManagedDeviceItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedDevice%2Did"] = managed_device_id
        return ManagedDeviceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ManagedDevicesRequestBuilderGetQueryParameters]] = None) -> Optional[ManagedDeviceCollectionResponse]:
        """
        The managed devices associated with the user.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManagedDeviceCollectionResponse]
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
        from ....models.managed_device_collection_response import ManagedDeviceCollectionResponse

        return await self.request_adapter.send_async(request_info, ManagedDeviceCollectionResponse, error_mapping)
    
    async def post(self,body: ManagedDevice, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ManagedDevice]:
        """
        Create new navigation property to managedDevices for users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManagedDevice]
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
        from ....models.managed_device import ManagedDevice

        return await self.request_adapter.send_async(request_info, ManagedDevice, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ManagedDevicesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The managed devices associated with the user.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: ManagedDevice, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create new navigation property to managedDevices for users
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
    
    def with_url(self,raw_url: str) -> ManagedDevicesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ManagedDevicesRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ManagedDevicesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bulk_reprovision_cloud_pc(self) -> BulkReprovisionCloudPcRequestBuilder:
        """
        Provides operations to call the bulkReprovisionCloudPc method.
        """
        from .bulk_reprovision_cloud_pc.bulk_reprovision_cloud_pc_request_builder import BulkReprovisionCloudPcRequestBuilder

        return BulkReprovisionCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bulk_restore_cloud_pc(self) -> BulkRestoreCloudPcRequestBuilder:
        """
        Provides operations to call the bulkRestoreCloudPc method.
        """
        from .bulk_restore_cloud_pc.bulk_restore_cloud_pc_request_builder import BulkRestoreCloudPcRequestBuilder

        return BulkRestoreCloudPcRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bulk_set_cloud_pc_review_status(self) -> BulkSetCloudPcReviewStatusRequestBuilder:
        """
        Provides operations to call the bulkSetCloudPcReviewStatus method.
        """
        from .bulk_set_cloud_pc_review_status.bulk_set_cloud_pc_review_status_request_builder import BulkSetCloudPcReviewStatusRequestBuilder

        return BulkSetCloudPcReviewStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def download_app_diagnostics(self) -> DownloadAppDiagnosticsRequestBuilder:
        """
        Provides operations to call the downloadAppDiagnostics method.
        """
        from .download_app_diagnostics.download_app_diagnostics_request_builder import DownloadAppDiagnosticsRequestBuilder

        return DownloadAppDiagnosticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def execute_action(self) -> ExecuteActionRequestBuilder:
        """
        Provides operations to call the executeAction method.
        """
        from .execute_action.execute_action_request_builder import ExecuteActionRequestBuilder

        return ExecuteActionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def move_devices_to_o_u(self) -> MoveDevicesToOURequestBuilder:
        """
        Provides operations to call the moveDevicesToOU method.
        """
        from .move_devices_to_o_u.move_devices_to_o_u_request_builder import MoveDevicesToOURequestBuilder

        return MoveDevicesToOURequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ManagedDevicesRequestBuilderGetQueryParameters():
        """
        The managed devices associated with the user.
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
    class ManagedDevicesRequestBuilderGetRequestConfiguration(RequestConfiguration[ManagedDevicesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ManagedDevicesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

