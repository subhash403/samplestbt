import requests
import json
import configparser
import os
from pathlib import Path

class MakeApiCall:


    def __init__(self):
        self.mac_address    =   self.get_config_values('sst_demo','macAddress')
        self.spec_endpoint  = self.get_config_values('sst_demo','spec_endpoint')
        self.pin_value       = self.get_config_values('pin','pin_value')

    def get_config_values(self,ParentKey,ChildKey):
        absFilePath = Path(__file__).parent
        while(os.path.basename(absFilePath)!='stb-tester-test-pack-charter'):
            absFilePath = Path(absFilePath).parent
        project_root_dir = absFilePath._str
        config = configparser.ConfigParser()
        config.read(project_root_dir+"\config\stbt.conf")
        return config[ParentKey][ChildKey]

    def login_edge_payload_builder(self,mac_address):
        return "macAddress="+self.mac_address

    def login_edge_header_builder(self):
        return {'Content-Type': "application/x-www-form-urlencoded",
                'Authorization': "Basic Y2hhcnRlcm5ldDpDaGFydDNybjN0",
                'Accept': 'application/json'
        }

    def network_edge_header_builder(self, token):
        return {'Content-Type': "application/json",
                'Authorization': "Basic Y2hhcnRlcm5ldDpDaGFydDNybjN0",
                'X-CHARTER-SESSION': token
                }

    def post_request_builder(self,url,payload,header):
        response = requests.post(url,data=payload, headers=header)
        return response

    def get_login_edge_response(self,url):
        payload  = self.login_edge_payload_builder(self.mac_address)
        header   = self.login_edge_header_builder()
        response = self.post_request_builder(url,payload,header)
        return response

    def get_network_edge_response(self,url,payload,login_edge_response):
        j = login_edge_response.json()
        token = j['AuthResponse']['Token']
        header =  self.network_edge_header_builder(token)
        response = self.post_request_builder(url, payload, header)
        return response

    def execute_spec_endpoint(self):
        if (self.spec_endpoint == "spectrumint.engprod-charter.net" or self.spec_endpoint == "spectrum.engprod-charter.net"):
            try:
                url = "http://" + self.spec_endpoint + "/api/pub/loginedge/login/v1/auth/login"
                response = self.get_login_edge_response(url)
                if (response.status_code != 200):
                    raise Exception
                else:
                    return response
            except Exception:
                print("Exception Occured in Login Call")
                if self.spec_endpoint == "spectrumint.engprod-charter.net":
                    try:
                        self.spec_endpoint = "spectrum.engprod-charter.net"
                        url = "http://" + self.spec_endpoint + "/api/pub/loginedge/login/v1/auth/login"
                        response = self.get_login_edge_response(url)
                        if response.status_code != 200:
                            raise Exception
                        else:
                            return response
                    except Exception:
                        print("Both Endpoints for SpecA received a failure when trying to use loginEdge")

                elif self.spec_endpoint == "spectrum.engprod-charter.net":
                    try:
                        self.spec_endpoint = "spectrumint.engprod-charter.net"
                        url = "http://" + self.spec_endpoint + "/api/pub/loginedge/login/v1/auth/login"
                        response = self.get_login_edge_response(url)
                        if response.status_code != 200:
                            raise Exception
                        else:
                            print("Login Edge Call Successful")
                            return response
                    except Exception:
                        print("Both Endpoints for SpecA received a failure when trying to use loginEdge")
        else:
            self.spec_endpoint = "spectrum.engprod-charter.net"
            try:
                url = "http://" + self.spec_endpoint + "/api/pub/loginedge/login/v1/auth/login"
                response = self.get_login_edge_response(url)
                if response.status_code != 200:
                    raise Exception
                else:
                    return response
            except Exception:
                if self.spec_endpoint == "spectrumint.engprod-charter.net":
                    try:
                        self.spec_endpoint = "spectrum.engprod-charter.net"
                        url = url = "http://" + self.spec_endpoint + "/api/pub/loginedge/login/v1/auth/login"
                        response = self.get_login_edge_response(url)
                        if response.status_code != 200:
                            raise Exception
                        else:
                            print("Login Edge Call Successful")
                            return response
                    except Exception:
                        print("Both Endpoints for SpecA received a failure when trying to use loginEdge")

                elif self.spec_endpoint == "spectrum.engprod-charter.net":
                    try:
                        self.spec_endpoint = "spectrumint.engprod-charter.net"
                        url = url = "http://" + self.spec_endpoint + "/api/pub/loginedge/login/v1/auth/login"
                        response = self.get_login_edge_response(url)
                        if response.status_code != 200:
                            raise Exception
                        else:
                            return response
                    except Exception:
                        print("Both Endpoints for SpecA received a failure when trying to use loginEdge")

    def set_pin(self,value,login_edge_response):
        print("*********Triggering Set PIN API*********")
        if(value == "Parental"):
            payload = '{"settings":{"groups":[{"id":"STB' + self.mac_address + '","type":"device-stb","options":[{"name":"Parental Control PIN","value":["2222"]}]}]}}'
        elif(value == "Purchase"):
            payload = '{"settings":{"groups":[{"id":"STB' + self.mac_address + '","type":"device-stb","options":[{"name":"Purchase PIN","value":["0000"]},{"name":"Purchase PIN Active","value":[true]}]}]}}'
        elif(value == "Demand"):
            payload = '{"settings":{"groups":[{"id":"STB' + self.mac_address + '","type":"device-stb","options":[{"name":"VOD PIN","value":["0000"]},{"name":"On Demand Lock","value":[true]}]}]}}'
        try:
            url = "http://" + self.spec_endpoint + "/api/pub/networksettingsedge/v1/settings"
            network_edge_response = self.get_network_edge_response(url, payload, login_edge_response)
            if (network_edge_response.status_code != 200):
                raise Exception
        except Exception:
            print("Exception Occured in Network Edge Call")
            retry_count = 3
            while (network_edge_response.status_code != 200):
                if (retry_count > 0):
                    network_edge_response = self.get_network_edge_response(url, payload, login_edge_response)
                else:
                    print("NetworkSettingsEdge call failed to update SET pin for the mac: " + self.mac_address + " even after 3 attempts")
                    #Code to fail the test case
                    break
                retry_count = retry_count - 1
        else:
            print("*********SET PIN API Call successful*********")

    def parental_pin(self,toggle):
        print("*********Triggering Parental PIN API*********")
        login_edge_response = self.execute_spec_endpoint()
        self.set_pin("Parental",login_edge_response)
        if(toggle == "On"):
            payload = '{"settings":{"groups":[{"id":"STB' + self.mac_address + '","type":"device-stb","options":[{"name":"Enable/Disable Parental Controls","value":["On"]}]}]}}'
        elif(toggle == "Off"):
            payload = '{"settings":{"groups":[{"id":"STB' + self.mac_address + '","type":"device-stb","options":[{"name":"Enable/Disable Parental Controls","value":["Off"]}]}]}}'
        try:
            url = "http://" + self.spec_endpoint + "/api/pub/networksettingsedge/v1/settings"
            network_edge_response = self.get_network_edge_response(url,payload,login_edge_response)
            if network_edge_response.status_code != 200:
                raise Exception
        except Exception:
            print("Exception Occured in Network Edge Call")
            retry_count = 3
            while(network_edge_response.status_code != 200):
                if(retry_count>0):
                    network_edge_response = self.get_network_edge_response(url, payload, login_edge_response)
                else:
                    print("NetworkSettingsEdge call failed to update parental pin to ON/OFF setting for the mac:" + self.mac_address +"even after 3 attempts")
                    # Code to fail the test case
                    break
                retry_count = retry_count - 1
        else:
            print("*********Parental PIN API Call successful*********")

    def HDAT(self, toggle):
                print("*********Triggering HD Auto Tune PIN API*********")
                login_edge_response = self.execute_spec_endpoint()
                if (toggle == "On"):
                    payload = '{"settings":{"groups":[{"id":"STB' + self.mac_address + '","type":"device-stb","options":[{"name":"HD Auto Tune","value":["On"]}]}]}}'
                elif (toggle == "Off"):
                    payload = '{"settings":{"groups":[{"id":"STB' + self.mac_address + '","type":"device-stb","options":[{"name":"HD Auto Tune","value":["Off"]}]}]}}'
                try:
                    url = "http://" + self.spec_endpoint + "/api/pub/networksettingsedge/v1/settings"
                    network_edge_response = self.get_network_edge_response(url, payload, login_edge_response)
                    if network_edge_response.status_code != 200:
                        raise Exception
                except Exception:
                    print("Exception Occured in Network Edge Call")
                    retry_count = 3
                    while (network_edge_response.status_code != 200):
                        if (retry_count > 0):
                            network_edge_response = self.get_network_edge_response(url, payload, login_edge_response)
                        else:
                            print(
                                "NetworkSettingsEdge call failed to update Hdat to ON/OFF setting for the mac:" + self.mac_address + "even after 3 attempts")
                            # Code to fail the test case
                            break
                        retry_count = retry_count - 1
                else:
                    print("*********HD Auto Tune API Call successful*********")

    def ResetBox(self, toggle):
                print("*********Triggering Reset Box API*********")
                login_edge_response = self.execute_spec_endpoint()
                if (toggle == "No"):
                    payload = '{"settings":{"groups":[{"id":"STB' + self.mac_address + '","type":"device-stb","options":[{"name":"SetupCompleted","value":["1.0"]},{"name":"NavPanelVisitsRemaining","value":["4"]}]}]}}'
                elif (toggle == "Yes"):
                    payload = '{"settings":{"groups":[{"id":"STB' + self.mac_address + '","type":"device-stb","options":[{"name": "SetupCompleted","value": []},{"name": "Guide Presentation","value": ["High Definition (16:9)"]},{"name": "InitResolutionSetup","value": ["0"]}]}]}}'
                try:
                    url = "http://" + self.spec_endpoint + "/api/pub/networksettingsedge/v1/settings"
                    network_edge_response = self.get_network_edge_response(url, payload, login_edge_response)
                    if network_edge_response.status_code != 200:
                        raise Exception
                except Exception:
                    print("Exception Occured in Network Edge Call")
                    retry_count = 3
                    while (network_edge_response.status_code != 200):
                        if (retry_count > 0):
                            network_edge_response = self.get_network_edge_response(url, payload, login_edge_response)
                        else:
                            print(
                                "NetworkSettingsEdge call failed to reset the box setting for the mac:" + self.mac_address + "even after 3 attempts")
                            # Code to fail the test case
                            break
                        retry_count = retry_count - 1
                else:
                    print("*********reset the box API Call successful*********")
    def Info(self, toggle):
                print("*********Triggering Info Banner Duration API*********")
                login_edge_response = self.execute_spec_endpoint()
                if (toggle == "5"):
                    payload = '{"settings":{"groups":[{"id":"STB' + self.mac_address + '","type":"device-stb","options":[{"name":"Info Banner Duration","value":["5"]}]}]}}'
                elif (toggle == "10"):
                    payload = '{"settings":{"groups":[{"id":"STB' + self.mac_address + '","type":"device-stb","options":[{"name":"Info Banner Duration","value":["10"]}]}]}}'
                elif (toggle == "15"):
                    payload = '{"settings":{"groups":[{"id":"STB' + self.mac_address + '","type":"device-stb","options":[{"name":"Info Banner Duration","value":["15"]}]}]}}'
                elif (toggle == "20"):
                    payload = '{"settings":{"groups":[{"id":"STB' + self.mac_address + '","type":"device-stb","options":[{"name":"Info Banner Duration","value":["20"]}]}]}}'
                elif (toggle == "25"):
                    payload = '{"settings":{"groups":[{"id":"STB' + self.mac_address + '","type":"device-stb","options":[{"name":"Info Banner Duration","value":["25"]}]}]}}'
                elif (toggle == "30"):
                    payload = '{"settings":{"groups":[{"id":"STB' + self.mac_address + '","type":"device-stb","options":[{"name":"Info Banner Duration","value":["30"]}]}]}}'
                try:
                    url = "http://" + self.spec_endpoint + "/api/pub/networksettingsedge/v1/settings"
                    network_edge_response = self.get_network_edge_response(url, payload, login_edge_response)
                    if network_edge_response.status_code != 200:
                        raise Exception
                except Exception:
                    print("Exception Occured in Network Edge Call")
                    retry_count = 3
                    while (network_edge_response.status_code != 200):
                        if (retry_count > 0):
                            network_edge_response = self.get_network_edge_response(url, payload, login_edge_response)
                        else:
                            print(
                                "NetworkSettingsEdge call failed to set Info Banner Duration for the mac:" + self.mac_address + "even after 3 attempts")
                            # Code to fail the test case
                            break
                        retry_count = retry_count - 1
                else:
                    print("*********Info Banner Duration setting API Call successful*********")

abc = MakeApiCall()
#login_edge_response = abc.execute_spec_endpoint()
#abc.set_pin("Parental",login_edge_response)
#abc.HDAT("On")
#abc.ResetBox("Yes")
abc.Info("15")