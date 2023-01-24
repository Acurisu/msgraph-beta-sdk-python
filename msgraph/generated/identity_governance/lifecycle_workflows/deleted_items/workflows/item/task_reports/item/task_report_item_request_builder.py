from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

task_request_builder = lazy_import('msgraph.generated.identity_governance.lifecycle_workflows.deleted_items.workflows.item.task_reports.item.task.task_request_builder')
task_definition_request_builder = lazy_import('msgraph.generated.identity_governance.lifecycle_workflows.deleted_items.workflows.item.task_reports.item.task_definition.task_definition_request_builder')
task_processing_results_request_builder = lazy_import('msgraph.generated.identity_governance.lifecycle_workflows.deleted_items.workflows.item.task_reports.item.task_processing_results.task_processing_results_request_builder')
task_processing_result_item_request_builder = lazy_import('msgraph.generated.identity_governance.lifecycle_workflows.deleted_items.workflows.item.task_reports.item.task_processing_results.item.task_processing_result_item_request_builder')
task_report = lazy_import('msgraph.generated.models.identity_governance.task_report')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class TaskReportItemRequestBuilder():
    """
    Provides operations to manage the taskReports property of the microsoft.graph.identityGovernance.workflow entity.
    """
    @property
    def task(self) -> task_request_builder.TaskRequestBuilder:
        """
        Provides operations to manage the task property of the microsoft.graph.identityGovernance.taskReport entity.
        """
        return task_request_builder.TaskRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task_definition(self) -> task_definition_request_builder.TaskDefinitionRequestBuilder:
        """
        Provides operations to manage the taskDefinition property of the microsoft.graph.identityGovernance.taskReport entity.
        """
        return task_definition_request_builder.TaskDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task_processing_results(self) -> task_processing_results_request_builder.TaskProcessingResultsRequestBuilder:
        """
        Provides operations to manage the taskProcessingResults property of the microsoft.graph.identityGovernance.taskReport entity.
        """
        return task_processing_results_request_builder.TaskProcessingResultsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TaskReportItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/lifecycleWorkflows/deletedItems/workflows/{workflow%2Did}/taskReports/{taskReport%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[TaskReportItemRequestBuilderGetRequestConfiguration] = None) -> Optional[task_report.TaskReport]:
        """
        Represents the aggregation of task execution data for tasks within a workflow object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[task_report.TaskReport]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, task_report.TaskReport, error_mapping)
    
    def task_processing_results_by_id(self,id: str) -> task_processing_result_item_request_builder.TaskProcessingResultItemRequestBuilder:
        """
        Provides operations to manage the taskProcessingResults property of the microsoft.graph.identityGovernance.taskReport entity.
        Args:
            id: Unique identifier of the item
        Returns: task_processing_result_item_request_builder.TaskProcessingResultItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["taskProcessingResult%2Did"] = id
        return task_processing_result_item_request_builder.TaskProcessingResultItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_get_request_information(self,request_configuration: Optional[TaskReportItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Represents the aggregation of task execution data for tasks within a workflow object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    @dataclass
    class TaskReportItemRequestBuilderGetQueryParameters():
        """
        Represents the aggregation of task execution data for tasks within a workflow object.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class TaskReportItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TaskReportItemRequestBuilder.TaskReportItemRequestBuilderGetQueryParameters] = None

    

