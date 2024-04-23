from rest_framework.routers import DefaultRouter
from maintenance.api.views import (
    CarrierApiViewSet, AgentApiViewSet, VendorApiViewSet, CustomerApiViewSet,
    EmployeeApiViewSet, PortApiViewSet, PackageTypeApiViewSet, LocationApiViewSet,
    CompanyApiViewSet, ShipperApiViewSet, PickUpLocationApiViewSet, ConsigneeApiViewSet,
    DeliveryLocationApiViewSet, ClientToBillApiViewSet, ReleasedToApiViewSet
)
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CustomRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_with_pagination('carrier', CarrierApiViewSet)
        self.register_with_pagination('agent', AgentApiViewSet)
        self.register_with_pagination('vendor', VendorApiViewSet)
        self.register_with_pagination('customer', CustomerApiViewSet)
        self.register_with_pagination('employee', EmployeeApiViewSet)
        self.register_with_pagination('port', PortApiViewSet)
        self.register_with_pagination('packageType', PackageTypeApiViewSet)
        self.register_with_pagination('location', LocationApiViewSet)
        self.register_with_pagination('company', CompanyApiViewSet)
        self.register_with_pagination('shipper', ShipperApiViewSet)
        self.register_with_pagination('pickUpLocation', PickUpLocationApiViewSet)
        self.register_with_pagination('consignee', ConsigneeApiViewSet)
        self.register_with_pagination('deliveryLocation', DeliveryLocationApiViewSet)
        self.register_with_pagination('clientToBill', ClientToBillApiViewSet)
        self.register_with_pagination('releasedTo', ReleasedToApiViewSet)

    def register_with_pagination(self, prefix, viewset):
        print(f"Registering {prefix} with viewset {viewset}...")
        route = self.register(prefix=prefix, basename=prefix, viewset=viewset)
        if route is None:
            print(f"Failed to register {prefix}")
            return
        route_kwargs = {'suffix': 'List', 'name': f'{prefix}-list'}
        self.routes.append(self.get_dynamic_route(route, **route_kwargs))
        route_kwargs['suffix'] = 'Detail'
        route_kwargs['name'] = f'{prefix}-detail'
        self.routes.append(self.get_dynamic_route(route, **route_kwargs))

    def get_dynamic_route(self, route, **kwargs):
        dynamic_route = route.clone()
        for key, value in kwargs.items():
            setattr(dynamic_route, key, value)
        return dynamic_route

router_maintenance = CustomRouter()
router_maintenance.get_api_root_view().cls.pagination_class = CustomPageNumberPagination
