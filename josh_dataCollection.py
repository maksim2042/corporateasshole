import requests 
import pprint
import json



token = \
"""WLSSzjRE0MfyxnZhTA6YZ4gyufsHftl7sUfdvaUAq863tIgGxtTrMEPW0hNWSujEA2E86rC5CG+6LK3DnmoPdWk+kdCqz8oNpxNugMpbCVU4W05kr/RQwCcwvaya4IOxzXwByaERVMoZUL9EH3es3f78njZ6G2locOwKTpafT0P3/MHjAhJZ7qG/Yuw9onKm8lAx+DR7/+USbOn1evyNzNLXYQW585VDYWar3uO8F3GRdM821RkKwYOcX2SXLCvfAWBbEHqgPaipRWdd5qlTRYf+lyCqpOy9JUJ9wCBCOvucfl6p6++e+sZ/3M3Kx53jGAM/x6TcuWcjxCCsr0ag4g=="""


def company(duns):
    version = '2.1'
    url = 'https://maxcvservices.dnb.com/V2/organizations/%s/products/DCP_PREM'
    r = requests.get(url % (duns,),headers={
        'Authorization':token
    })
    result = json.loads(r.content)
    return result

def findcompany(company,auth_token=token,version=4.0):
    url = 'https://maxcvservices.dnb.com/V'+str(version)+'/organizations'
    r = requests.get(url,headers={
        'Authorization':auth_token
       },
        params={
        'OrganizationName':company,'findcompanycleansematch':True,"includeTopExecutives":True,
        'findcompany':True
        }
    )
    assert r.status_code==200,"Invalid duns or product_id"
    #if successful it returns a string which we convert into a dict which we return.
    result = json.loads(r.content)
    response = result['FindCompanyResponse']['FindCompanyResponseDetail']['FindCandidate']
    for val in response:
        if 'ConsolidatedEmployeeDetails' in val:
            employees = val['ConsolidatedEmployeeDetails']['TotalEmployeeQuantity']
            duns = val['DUNSNumber']
            name = val['OrganizationPrimaryName']['OrganizationName']['$']
            print name,duns,employees
    return result

if __name__ == '__main__':
    print "getting company"
    r = findcompany('chevron')
    print "done"
