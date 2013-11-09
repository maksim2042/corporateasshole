"""The D&B Direct API returns information in data_layers.
Each data_layer may have multiple levels.
The term "PRODUCT" is used to represent a given level for a data layer."""

"""Services are API technical documentation pages which describe what operations
a given API web-service provides. """

"""D&B partners that will be part of the hackathon:

FlipTop:
        Products:
        Social Media Data - per Company
        Social Media Data - per Person

HDS: HealthCare Data Solutions: HealthCare Industry Solutions:
        Products:
        Health Care - Hospital
        Health Care - Pharmacy
        Health Care - Provider

PROFOUND Networks: Provides Information Technology Data.
        Products:
        Digital Business Intelligence
         """


"""This class is one for the DataExchange Service.
It should be extended by the following PRODUCTS:
   
   1> Digital Business Intelligence
   2> Social Media -Company
   3> Social Media - Person
   4> Health Care - Provider
   5> Health Care - Hospital
   6> Health Care - Pharmacy

   These products will be classes of their own."""

import requests
import json
import dataCollection

class DataExchange:
    def __init__(self):
        self.auth_token = dataCollection.auth()
        self.auth_dict = {'Authorization':self.auth_token}
        self.version = 1.0
        self.api_version =2.0
        self.baseURL =''
        self.errors_dict= {200:'OK. Email(s) were processed successfully, and results were found. (Emails with no results are excluded from the response.)',202 :'Data not available. At least one email from the request is still being processed.',400:'Bad request The request is invalid or has incorrect syntax.',404:'Page not found Email(s) were processed successfully, and no results were found.',500:'Internal Server error (rare) There was an unexpected server error.'}

    """PRODUCT: Digital Business Intelligence
       OPERATION: OrderBusinessIntelligence .
    The OrderBusinessIntelligence operation provides business intelligence data for 
    a specific company, and requires a Profound domain or DUNS number"""
    #OrderBusinessIntelligenceByDuns
    """ @param: duns -- The duns number of the organization to retrieve BusinessIntelligence Product for.
        @return: dict() business_intelligence."""
    #doesn't work correctly
    def OrderBusinessIntelligenceByDuns(self,duns): 
        response= requests.get('https:// maxcvservices.dnb.com/dataexchange/profound/domain?duns='+str(duns)+'&view=enterprise',headers={'Authorization':self.auth_token})
        assert response.status_code==200,"please check duns and retry."
        resp_dict = json.loads(response.content)
        return resp_dict


    """ @param: domain -- The domain (URI) of the organization to retrieve BusinessIntelligence Product for.
        @return: resp_dict: info  of business_intelligence for the business with the specified domain."""
    
    def OrderBusinessIntelligenceByProfoundDomain(self,domain):
        response = requests.get('https://maxcvservices.dnb.com/dataexchange/profound/domain/'+domain+'?view=enterprise',headers={'Authorization':self.auth_token})
        assert response.status_code==200,"please check input domain Status Code:  "+str(response.status_code)
        resp_dict = json.loads(response.content)
        return resp_dict

    """ @param: duns -- The duns number of the organization to retrieve the Profound Domain for.
        @return: the domain of the input DUNS number. (URI)"""
    
    #No working examples provided in test-set. As it gives an invalid product code error.
    def FindProfoundDomainByDuns(self,duns):
        response = requests.get('https://maxcvservices.dnb.com/dataexchange/profound/duns='+str(duns),headers={'Authorization':self.auth_token})
        assert response.status_code==200,"please check input DUNS number.\n   Status Code: "+str(response.status_code)
        return response
        resp_dict= json.loads(response.content)
        return resp_dict

    """ This D&B Direct product includes 40 fields of crucial data on over 1.5 million healthcare providers, from Doctors and Dentists to Nurse Practitioners and Physician Assistants.
        This product is part of the D&B Data Exchange solution."""

    """@param: duns--valid duns number of a healthcare provider
       @return: resp_dict: the response dictionary with details of the specific healthcare provider."""
    
    #works!
    def OrderHealthProvider(self,duns):
        response = requests.get('https://maxcvservices.dnb.com/dataexchange/hds/duns2phy/'+str(duns),headers={'Authorization':self.auth_token})
        assert response.status_code==200,"please check input DUNS number.\n  Status Code:"+str(response.status_code)
        resp_dict = json.loads(response.content)
        return resp_dict

    #NO VALUES IN TEST SET TO TEST!
    def FindHealthProvider(self,first_name,last_name):
        response = requests.get('https://maxcvservices.dnb.com/dataexchange/hds/phys2duns?first='+first_name+'&last='+last_name,headers={'Authorization':self.auth_token})
        assert response.status_code==200,"please check input first and last name.\n  Status Code:"+str(response.status_code)
        resp_dict = json.loads(response.content)
        return resp_dict

    #works!
    def OrderHospital(self,duns):
        response = requests.get('https://maxcvservices.dnb.com/dataexchange/hds/hospitalinfo2/'+str(duns),headers={'Authorization':self.auth_token})
        assert response.status_code==200,"please check input DUNS number.\n  Status Code:"+str(response.status_code)
        resp_dict = json.loads(response.content)
        return resp_dict
    #works!
    def OrderPharmacy(self,duns):
        response = requests.get('https://maxcvservices.dnb.com/dataexchange/hds/prescriberinfo2/'+str(duns),headers={'Authorization':self.auth_token})
        assert response.status_code==200,"please check input DUNS number.\n  Status Code:"+str(response.status_code)
        resp_dict = json.loads(response.content)
        return resp_dict
    #works!
    def OrderCompanySocial(self,duns):
        response = requests.get('https://maxcvservices.dnb.com/dataexchange/fliptop/beta/company?duns='+str(duns),headers={'Authorization':self.auth_token})
        assert response.status_code==200,"please check input DUNS number.\n  Status Code:"+str(response.status_code)
        resp_dict = json.loads(response.content)
        return resp_dict

    

    """This D&B Direct product provides a complete digital identity for each of your contacts deriving
     a vast array of information from email addresses. Using information available on the public web, 
     this product provides social data from over 100 social networks such as Twitter, Facebook and LinkedIn; 
    creating one united digital personality for each of your leads and contacts. """

    """When requesting this D&B Direct product, a valid email or profile URL 
    (from Twitter, Facebook or LinkedIn) must be provided.
    An option to designate the response format is available. """
    """For now the social_url only takes the email service but later it should be expanded to accept other service. """
    
    #works!
    def OrderPersonSocial(self,social_url):
        response = requests.get('https://maxcvservices.dnb.com/dataexchange/fliptop/beta/person?email='+social_url+'&format=JSON',headers={'Authorization':self.auth_token})
        assert response.status_code==200,"please check input email address.\n  Status Code:"+str(response.status_code)
        resp_dict = json.loads(response.content)
        return resp_dict





