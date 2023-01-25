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

currency_request_builder = lazy_import('msgraph.generated.financials.companies.item.sales_quotes.item.currency.currency_request_builder')
customer_request_builder = lazy_import('msgraph.generated.financials.companies.item.sales_quotes.item.customer.customer_request_builder')
make_invoice_request_builder = lazy_import('msgraph.generated.financials.companies.item.sales_quotes.item.make_invoice.make_invoice_request_builder')
payment_term_request_builder = lazy_import('msgraph.generated.financials.companies.item.sales_quotes.item.payment_term.payment_term_request_builder')
sales_quote_lines_request_builder = lazy_import('msgraph.generated.financials.companies.item.sales_quotes.item.sales_quote_lines.sales_quote_lines_request_builder')
sales_quote_line_item_request_builder = lazy_import('msgraph.generated.financials.companies.item.sales_quotes.item.sales_quote_lines.item.sales_quote_line_item_request_builder')
send_request_builder = lazy_import('msgraph.generated.financials.companies.item.sales_quotes.item.send.send_request_builder')
shipment_method_request_builder = lazy_import('msgraph.generated.financials.companies.item.sales_quotes.item.shipment_method.shipment_method_request_builder')
sales_quote = lazy_import('msgraph.generated.models.sales_quote')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class SalesQuoteItemRequestBuilder():
    """
    Provides operations to manage the salesQuotes property of the microsoft.graph.company entity.
    """
    @property
    def currency(self) -> currency_request_builder.CurrencyRequestBuilder:
        """
        Provides operations to manage the currency property of the microsoft.graph.salesQuote entity.
        """
        return currency_request_builder.CurrencyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customer(self) -> customer_request_builder.CustomerRequestBuilder:
        """
        Provides operations to manage the customer property of the microsoft.graph.salesQuote entity.
        """
        return customer_request_builder.CustomerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def make_invoice(self) -> make_invoice_request_builder.MakeInvoiceRequestBuilder:
        """
        Provides operations to call the makeInvoice method.
        """
        return make_invoice_request_builder.MakeInvoiceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def payment_term(self) -> payment_term_request_builder.PaymentTermRequestBuilder:
        """
        Provides operations to manage the paymentTerm property of the microsoft.graph.salesQuote entity.
        """
        return payment_term_request_builder.PaymentTermRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sales_quote_lines(self) -> sales_quote_lines_request_builder.SalesQuoteLinesRequestBuilder:
        """
        Provides operations to manage the salesQuoteLines property of the microsoft.graph.salesQuote entity.
        """
        return sales_quote_lines_request_builder.SalesQuoteLinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send(self) -> send_request_builder.SendRequestBuilder:
        """
        Provides operations to call the send method.
        """
        return send_request_builder.SendRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shipment_method(self) -> shipment_method_request_builder.ShipmentMethodRequestBuilder:
        """
        Provides operations to manage the shipmentMethod property of the microsoft.graph.salesQuote entity.
        """
        return shipment_method_request_builder.ShipmentMethodRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SalesQuoteItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/financials/companies/{company%2Did}/salesQuotes/{salesQuote%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[SalesQuoteItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[sales_quote.SalesQuote]:
        """
        Get salesQuotes from financials
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[sales_quote.SalesQuote]
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
        return await self.request_adapter.send_async(request_info, sales_quote.SalesQuote, response_handler, error_mapping)
    
    async def patch(self,body: Optional[sales_quote.SalesQuote] = None, request_configuration: Optional[SalesQuoteItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[sales_quote.SalesQuote]:
        """
        Update the navigation property salesQuotes in financials
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[sales_quote.SalesQuote]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, sales_quote.SalesQuote, response_handler, error_mapping)
    
    def sales_quote_lines_by_id(self,id: str) -> sales_quote_line_item_request_builder.SalesQuoteLineItemRequestBuilder:
        """
        Provides operations to manage the salesQuoteLines property of the microsoft.graph.salesQuote entity.
        Args:
            id: Unique identifier of the item
        Returns: sales_quote_line_item_request_builder.SalesQuoteLineItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["salesQuoteLine%2Did"] = id
        return sales_quote_line_item_request_builder.SalesQuoteLineItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_get_request_information(self,request_configuration: Optional[SalesQuoteItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get salesQuotes from financials
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
    
    def to_patch_request_information(self,body: Optional[sales_quote.SalesQuote] = None, request_configuration: Optional[SalesQuoteItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property salesQuotes in financials
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class SalesQuoteItemRequestBuilderGetQueryParameters():
        """
        Get salesQuotes from financials
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
    class SalesQuoteItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SalesQuoteItemRequestBuilder.SalesQuoteItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SalesQuoteItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

