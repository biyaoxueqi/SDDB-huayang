from xml.sax.handler import ContentHandler
from xml.sax import parse
import json
import os
import pandas as pd
sourceFolder ="C:\\Users\\xujunjie2\\PycharmProjects\\SDDB 处理"
logName = "DC1E_2046_E2u_20200824.sddb"
targetFile = os.path.join(sourceFolder, logName)

class TestHandler(ContentHandler):
    # in_headline = False

    def __init__(self, ecuList):
        super().__init__()
        self.ecuList = ecuList
        self.ecu = {}
        self.ecuAttribute = {}
        self.currentEcuName = None
        self.currentSwName = None
        self.Sws = []
        self.currentServiceName = None
        self.currentServiceId = None
        self.Services = []
        self.currentDidName = None
        self.currentDidId = None
        self.Dids = []       

    def startElement(self, name, attrs):
        # print(name, attrs.keys())
        if name == 'ECU':
            print("ECU level attributes: ", name,attrs.get('Name'), attrs.get('address'))
            if attrs.get('Name'):
                # self.ecuList.append({attrs.get('Name'): None})
                self.currentEcuName = attrs.get('Name')
            # self.ecuAttribute.setdefault('DIDs', [])
            # self.ecuAttribute.setdefault('Address', attrs.get('address'))
            # self.ecuAttribute.setdefault('Name', attrs.get('Name'))
        # elif name == 'SWs':
        #     self.Sws = []
        elif name == 'SW':
            print("Software level attributes: ", attrs.get('Name'), attrs.get('Type'))
            if attrs.get('Name'):
                self.currentSwName = attrs.get('Name')
        # elif name == 'Services':
        #     self.Services = []
        elif name == 'Service':
            # print("Service Information: ", attrs.get('Name'), attrs.get('ID'))
            if attrs.get('Name'):
                self.currentServiceName = attrs.get('Name')
                self.currentServiceId = attrs.get('ID')
            if self.currentServiceId == "22":
                pass
                # print("22 service is found!")
                # print(self.currentEcuName, self.currentServiceName)
        elif name == 'DataIdentifier':
            if attrs.get('Name'):
                self.currentDidName = attrs.get('Name')
                self.currentDidId = attrs.get('ID')
            # print("请打印出当前的DID信息： ", self.currentDidName, self.currentServiceId)
            if self.currentServiceId == "22" and self.currentDidName.endswith("Geely"):
                # print("找到Geely的DID号码！")
                print(self.currentEcuName, self.currentSwName, self.currentServiceName, 
                self.currentDidName, self.currentDidId)
                self.Dids.append({"Name": self.currentDidName, "ID": self.currentDidId})
                self.ecu.setdefault("ECU", self.currentEcuName)
                self.ecu.setdefault('SW', self.currentSwName)
                self.ecu.setdefault('Service', self.currentServiceName)
                self.ecu.setdefault('DidName',self.currentDidName)
                self.ecu.setdefault('Did',self.currentDidId)

        return super().startElement(name, attrs)

    def endElement(self, name):
        if name == 'ECU':
            # self.ecu.setdefault(self.currentEcuName, self.ecuAttribute)
            # print("Current ECU: ", self.ecu)
            # print("Current ECU Attribute: ", self.ecuAttribute)
            self.ecuList.append(self.ecu)
            self.ecuAttribute = {}
            self.ecu = {}
            self.currentEcuName = None
        elif name == 'SWs':
            self.Sws = []
        elif name == 'SW':
            # print("Current SW: ", self.currentSwName)
            self.currentSwName = None
        elif name == 'Services':
            self.Services = []
        elif name == 'Service':
            # print("Current Service: ", self.currentServiceName)
            self.currentServiceName = None
            self.currentServiceId = None

        elif name == 'DataIdentifiers':
            # print("DIDs: ", self.Dids)
            self.Dids = []

        elif name == 'DataIdentifier':
            self.currentDidName = None
            self.currentDidId = None


        return super().endElement(name)

    def characters(self, content):
        # print(len(content))
        return super().characters(content)

    # def generateEcuAddressMap(self):
    #     with open('EcuAddressMap.py', 'w') as f:
    #         pass

def test():
    print(targetFile)
    # ecuConfig = {}
    ecuList = []
    parse(targetFile, TestHandler(ecuList))
    # print(ecuConfig)
    print(ecuList)
    print(len(ecuList))

    # with open('ecuPool.json', 'w') as f:
    #     json.dump(ecuConfig, f, indent=4)

if __name__ == '__main__':
    test()
