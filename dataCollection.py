import requests 
import json
"""
Steps:  Run auth first, store return value of auth method in a token.
        Pass this token as the auth token into all the methods.
        Auth must be passed in the header of the GET request with 'Authorization' key.
"""



"""def main():
    product_codes_per_service = {'News and Media Service':{'@version':'News and Social Media':'NEWS_MDA'},
                    'Assessment Product Service':{'@version':3.0,'Small Business company & Owner Risk Profile':'SBCRP','Predictive Bankruptcy Risk - D&B Financial Stress Score (FSS)':'PBR_FSS_V7.1','Predictive Payment Risk - D&B Commercial Credit Score (CCS)':'PPR_CCS_V9','D&B Rating & Trend':'RTNG_TRND','Predictive Bankruptcy & Payment Risk - Standard':'PBPR_STD','Predictive Bankruptcy & Payment Risk - Enhanced':'PBPR_ENH','Predictive Global Payment Risk -  D&B Emergine Market Mediation Alert Score (EMMA)':'PGPR_EMMA','D&B Supplier Evaluation Risk Rating':'SER','D&B Total Loss Predictor':'TLP','D&B Viability Rating':'VIAB_RAT'},
                    ''}
    token = auth()"""

#this mehtod makes a post_request with the user_id and password.
def auth():
    header_params = {'x-dnb-user':'Hackathon2@dnb.com','x-dnb-pwd':'Hackathon123'}
    url = 'https://maxcvservices.dnb.com/rest/Authentication'
    r = requests.post(url,headers=header_params)
    auth_token=''
    assert r.status_code==200,"Invalid user_id/password please try again"    
    auth_token = r.headers['authorization']
    return auth_token

#this method returns all available product IDs per duns number and country code combination.
#@param: trade_up, this parameter 

#works!
def getAllAvailableProductsPerDUNS(duns,country_code,auth_token,trade_up=True):
    url = 'https://maxcvservices.dnb.com/V2/organizations/'+str(duns)+'/products?CountryISOAlpha2Code='+country_code
    r  = requests.get(url,headers={'Authorization':auth_token})
    product_ids=list()
    products_dict = dict()
    if(r.status_code==200):
        products_dict = json.loads(r.content)
        #product ids of various products in that company represented by @param:duns in country represented by @param:country_code.
        product_ids = [item['DNBProductID']for item in products_dict['ListAvailableProductResponse']['ListAvailableProductResponseDetail']['AvailableProductDetail']]
       
    #if response code was not 200 and something else,
    assert len(product_ids)>0,"No product Ids to return please check input params and whether response code was successful."
    return product_ids    


product_codes={'Small Business Company & Owner Risk Profile':'SBCRP',
              'Predictive Bankruptcy Risk - D&B Financial Stress Score (FSS)':'PBR_FSS_V7.1',  
              'Predictive Payment Risk - D&B Commercial Credit Score (CCS)':'PPR_CCS_V9',
              'D&B Rating & Trend':'RTNG_TRND',
              'Predictive Bankruptcy & Payment Risk - Standard':'PBPR_STD',
              'Predictive Bankruptcy & Payment Risk - Enhanced':'PBPR_ENH',
              'Predictive Global Payment Risk - D&B Emerging Market Mediation Alert Score (EMMA)':'PGPR_EMMA'}
#works!              
def assessmentProductService(duns,product_id,auth_token,version=3.0):
    url = 'https://maxcvservices.dnb.com/V'+str(version)+'/organizations/'+str(duns)+'/products/'+product_id
    r = requests.get(url,headers={'Authorization':auth_token})
    assert r.status_code==200,"Invalid duns or product_id"
    #if successful it returns a string which we convert into a dict which we return.
    return json.loads(r.content)

#doesn't work for the given test_ids.
#The given example works but don't know how to obtain PrincipalIdentificaitonNumber.
#https://maxcvservices.dnb.com/V3.0/organizations/804735132/products/CNTCT?CountryISOAlpha2Code=US&PrincipalIdentificationNumber=5412658&PrincipalIdentificationNumberTypeCode=24215
product_codes_contactProductService = {'People-Standard':'CNTCT','People-Enhanced':'CNTCT_PLUS'}
def contactProductService_OrderProduct(duns,product_id,auth_token,country_code,version=3.0):
    url = 'https://maxcvservices.dnb.com/V'+str(version)+'/organizations/'+str(duns)+'/products/'+str(product_id)+'?CountryISOAlpha2Code='+country_code
    r = requests.get(url,headers={'Authorization':auth_token})
    assert r.status_code==200,"Invalid duns or product_id"+str(r.status_code)
    return json.loads(r.content)


#works for Financial Statements but not with Financila Highlights.
product_codes_financialProductService = {'Financial_Statements':'FIN_ST_PLUS','Financial_Highlights':'FIN_HGLT'}
def financialProductService(duns,product_id,auth_token,country_code,version=3.0):
    url='https://maxcvservices.dnb.com/V3.0/organizations/'+str(duns)+'/products/'+product_id+'?CountryISOAlpha2Code='+country_code
    r = requests.get(url,headers={'Authorization':auth_token})
    assert r.status_code==200,"Invalid duns or product_id"+str(r.status_code)
    return json.loads(r.content)

product_codes_firmographicProductService = {'Detailed Company Profile - Standard':'DCP_STD',
                                             'Detailed Company Profile - Enhanced':'DCP_ENH',
                                             'Detailed Company Profile - Premium':'DCP_PREM',
                                             'Alternative Detailed Company Profile - Standard':'DCP_ALT_STD',
                                             'Alternative Detailed Company Profile - Enhanced':'DCP_ALT_ENH',
                                             'Alternative Detailed Company Profile - Premium':'DCP_ALT_PREM',
                                             'Diversity Indicators - Standard':'DVR_STD',
                                             'Diversity Indicators - Enhanced':'DVR_ENH',
                                             'USA Patriot Act Plus':'PAC_PLUS'}

#works!
def firmographicProductService(duns,product_id,auth_token,country_code,version=2.1):
    url='https://maxcvservices.dnb.com/V2.1/organizations/'+str(duns)+'/products/'+product_id
    r = requests.get(url,headers={'Authorization':auth_token})
    assert r.status_code==200,"Invalid duns or product_id"
    return json.loads(r.content)

#works!
#can provide either industry_code_value or industry_code_type.
product_codes_IndustryProductService = {'Research-Industry code':'IND_STD','Research - State/Province':'IND_ADV'}
def industryProductService(auth_token,product_id,industry_code_value=None,industry_code_type=None,state_territory_code=None,version=3.0):
    url = ''
    if(industry_code_value!=None):
        url = 'https://maxcvservices.dnb.com/V3.0/industries/industrycode-'+str(industry_code_value)+'/'+product_id
    elif(state_territory_code!=None):
        url =  'https://maxcvservices.dnb.com/V'+str(version)+'/industries/location-'+state_territory_code+'/'+product_id
    else:
        assert industry_code_value!=None or state_territory_code!=None,"Please enter either industry_code or state_territory_code"
    r = requests.get(url,headers={'Authorization':auth_token})
    assert r.status_code==200,"Invalid duns or product_id"
    return json.loads(r.content)

#works!
product_codes_LinkageProductService = {'Corporate Linkage - Standard':'LNK_UPF','Corporate Linkage - Enhanced':'LNK_FF'}
def linkageProductService(duns,product_id,auth_token,version=3.1):
    url='https://maxcvservices.dnb.com/V3.1'+'/organizations/'+str(duns)+'/products/'+product_id
    r = requests.get(url,headers={'Authorization':auth_token})
    assert r.status_code==200,"Invalid duns or product_id"
    return json.loads(r.content)

#works
product_codes_public_records_service = {'Suits':'PUBREC_SUITS',
                                        'Liens':'PUBREC_LIENS',
                                        'Judgments':'PUBREC_JDG',
                                        'UCC Filings':'PUBREC_UCC',
                                        'Business Registrations':'PUBREC_BR',
                                        'Corporate Entity Type & Ownership':'PUBREC_OS',
                                        'Suits, Liens, Judgments & Bankruptcies - Detail':'PUBREC_DTLS',
                                        'Filing List':'PUBREC_FL'}
 #works except for Filings. Need to figure out query URL for Filings product.                                    
def publicRecordService(duns,product_id,auth_token,version=3.0):
    url='https://maxcvservices.dnb.com/V3.0'+'/organizations/'+str(duns)+'/products/'+product_id
    r = requests.get(url,headers={'Authorization':auth_token})
    assert r.status_code==200,"Invalid duns or product_id"
    return json.loads(r.content)



product_codes_sbri_service = {'Small Business Risk Insight - Standard':'SBRI_STD','Small Business Risk Insight - Enhanced':'SBRI_ENH'}
def SBRIService(duns,product_id,auth_token,version='3.2',subject_id=None):
    url = 'https://maxcvservices.dnb.com/V{version}/organizations/'+str(duns)+'/products/'+product_id
    r = requests.get(url,headers={'Authorization':auth_token})
    assert r.status_code==200,"Invalid duns or product_id"
    return json.loads(r.content)



def getCompaniesBypostalCode(auth_token,postalcode,countryCode='US',radiusSearchCountryCode='US',searchModeDescription='Advanced'):
    url = 'https://maxcvservices.dnb.com/V4.0/organizations?findcompany=true&RadiusSearchPostalCode-1='+str(postalcode)+'&CountryISOAlpha2Code-1='+str(countryCode)+'&RadiusSearchCountryISOAlpha2Code-1='+str(radiusSearchCountryCode)+'&SearchModeDescription='+str(searchModeDescription)
    r = requests.get(url,headers={'Authorization':auth_token})
    assert r.status_code==200,"Invalid duns or product_id"
    return json.loads(r.content)

