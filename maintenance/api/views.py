from rest_framework.viewsets import ModelViewSet
from maintenance.models import carrier, port, vendor, employee, forwarAgent, company, address, agent, companyType, addressInfo, companyLogo, companyRegisCode, systCurren, importSchedule, companyInfo, packType, wareHouseProviders, forWardingAgents, containerType, customer, location, containerCode, containerEquipType, consignee
from maintenance.api.serializers import carrierSerializer, portSerializer, vendorSerializer, employeeSerializer, forwarAgentSerializer, companySerializer, addresSerializer, agentSerializer, companyTypeSerializer, companyInfoSerializer, addressInfoSerializer, companyLogoSerializer, companyRegisCodeSerializer, systCurrenSerializer, importScheduleSerializer, packTypeSerializer, wareHouseProvidersSerializer, forWardingAgentsSerializer, containerTypeSerializer, customerSerializer, locationSerializer, containerCodeSerializer, containerEquipTypeSerializer, consigneeSerializer


class carrierApiViewSet(ModelViewSet):
    serializer_class = carrierSerializer
    queryset = carrier.objects.all()

class portApiViewSet(ModelViewSet):
    serializer_class = portSerializer
    queryset = port.objects.all()

class vendorApiViewSet(ModelViewSet):
    serializer_class = vendorSerializer
    queryset = vendor.objects.all()

class employeeApiViewSet(ModelViewSet):
    serializer_class = employeeSerializer
    queryset = employee.objects.all()

class forwarAgentApiViewSet(ModelViewSet):
    serializer_class = forwarAgentSerializer
    queryset = forwarAgent.objects.all()

class companyApiViewSet(ModelViewSet):
    serializer_class = companySerializer
    queryset = company.objects.all()

class addressApiViewSet(ModelViewSet):
    serializer_class = addresSerializer
    queryset = address.objects.all()

class agentApiViewSet(ModelViewSet):
    serializer_class = agentSerializer
    queryset = agent.objects.all()

class companyTypeApiViewSet(ModelViewSet):
    serializer_class = companyTypeSerializer
    queryset = companyType.objects.all()

class companyInfoApiViewSet(ModelViewSet):
    serializer_class = companyInfoSerializer
    queryset = companyInfo.objects.all()

class addressInfoApiViewSet(ModelViewSet):
    serializer_class = addressInfoSerializer
    queryset = addressInfo.objects.all()

class companyLogoApiViewSet(ModelViewSet):
    serializer_class = companyLogoSerializer
    queryset = companyLogo.objects.all()

class companyRegisCodeApiViewSet(ModelViewSet):
    serializer_class = companyRegisCodeSerializer
    queryset = companyRegisCode.objects.all()

class systCurrenApiViewSet(ModelViewSet):
    serializer_class = systCurrenSerializer
    queryset = systCurren.objects.all()

class importScheduleApiViewSet(ModelViewSet):
    serializer_class = importScheduleSerializer
    queryset = importSchedule.objects.all()

class packTypeApiViewSet(ModelViewSet):
    serializer_class = packTypeSerializer
    queryset = packType.objects.all()

class wareHouseProvidersApiViewSet(ModelViewSet):
    serializer_class = wareHouseProvidersSerializer
    queryset = wareHouseProviders.objects.all()

class forWardingAgentsApiViewSet(ModelViewSet):
    serializer_class = forWardingAgentsSerializer
    queryset = forWardingAgents.objects.all()

class containerTypeApiViewSet(ModelViewSet):
    serializer_class = containerTypeSerializer
    queryset = containerType.objects.all()
    
class customerApiViewSet(ModelViewSet):
    serializer_class = customerSerializer
    queryset = customer.objects.all()

class locationApiViewSet(ModelViewSet):
    serializer_class = locationSerializer
    queryset = location.objects.all()

class containerCodeApiViewSet(ModelViewSet):
    serializer_class = containerCodeSerializer
    queryset = containerCode.objects.all()

class containerEquipTypeApiViewSet(ModelViewSet):
    serializer_class = containerEquipTypeSerializer
    queryset = containerEquipType.objects.all()
    
class consigneeApiViewSet(ModelViewSet):
    serializer_class = consigneeSerializer
    queryset = consignee.objects.all()