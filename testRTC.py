import requests
import getpass

def testRTC():
    rtc_base_url = 'https://igartc02.swg.usma.ibm.com/jazz'
    AUTH_URL = rtc_base_url + '/authenticated/identity'
    rtc_prject_area='_Zg2DQMnqEeW_p-Za6ipczw'
    username=input('Please input username:')
    password=getpass.getpass('Password:')

    payload = {
      'j_username': username,
      'j_password': password
      }

    return requests.Session().get(AUTH_URL, data=payload , verify=False)

if __name__ == '__main__':
    rtn = testRTC()
    print(rtn.text)
