from rest_framework.routers import DefaultRouter
from maintenance.api.views import carrierApiViewSet, portApiViewSet, vendorApiViewSet, employeeApiViewSet, companyApiViewSet, addressApiViewSet, companyTypeApiViewSet, companyInfoApiViewSet, addressInfoApiViewSet, companyLogoApiViewSet, companyRegisCodeApiViewSet, systCurrenApiViewSet, importScheduleApiViewSet, packTypeApiViewSet, wareHouseProvidersApiViewSet, forWardingAgentsApiViewSet, containerTypeApiViewSet, customerApiViewSet, containerCodeApiViewSet, locationApiViewSet, containerEquipTypeApiViewSet, consigneeApiViewSet

router_maintenance = DefaultRouter()

router_maintenance.register(prefix='carrier', basename='carrier', viewset=carrierApiViewSet)
router_maintenance.register(prefix='port', basename='port', viewset=portApiViewSet)
router_maintenance.register(prefix='vendor', basename='vendor', viewset=vendorApiViewSet)
router_maintenance.register(prefix='employee', basename='employee', viewset=employeeApiViewSet)
router_maintenance.register(prefix='company', basename='company', viewset=companyApiViewSet)
router_maintenance.register(prefix='address', basename='address', viewset=addressApiViewSet)
router_maintenance.register(prefix='companyType', basename='companyType', viewset=companyTypeApiViewSet)
router_maintenance.register(prefix='addressInfo', basename='addressInfo', viewset=addressInfoApiViewSet)
router_maintenance.register(prefix='companyLogo', basename='companyLogo', viewset=companyLogoApiViewSet)
router_maintenance.register(prefix='companyRegisCode', basename='companyRegisCode', viewset=companyRegisCodeApiViewSet)
router_maintenance.register(prefix='systCurren', basename='systCurren', viewset=systCurrenApiViewSet)
router_maintenance.register(prefix='importSchedule', basename='importSchedule', viewset=importScheduleApiViewSet)
router_maintenance.register(prefix='companyInfo', basename='companyInfo', viewset=companyInfoApiViewSet)
router_maintenance.register(prefix='packType', basename='packType', viewset=packTypeApiViewSet)
router_maintenance.register(prefix='wareHouseProviders', basename='wareHouseProviders', viewset=wareHouseProvidersApiViewSet)
router_maintenance.register(prefix='forWardingAgents', basename='forWardingAgents', viewset=forWardingAgentsApiViewSet)
# ++++++++++++++++++++++++
router_maintenance.register(prefix='containerType', basename='containerType', viewset=containerTypeApiViewSet)
router_maintenance.register(prefix='customer', basename='customer', viewset=customerApiViewSet)
router_maintenance.register(prefix='location', basename='location', viewset=locationApiViewSet)
router_maintenance.register(prefix='containerCode', basename='containerCode', viewset=containerCodeApiViewSet)
router_maintenance.register(prefix='containerEquipType', basename='containerEquipType', viewset=containerEquipTypeApiViewSet)
#-------------------------
router_maintenance.register(prefix='consignee', basename='consignee', viewset=consigneeApiViewSet)
