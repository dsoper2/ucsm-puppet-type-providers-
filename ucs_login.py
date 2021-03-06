#!/usr/bin/python
import hiera
from ucsmsdk.ucshandle import UcsHandle
import json
import sys
import jsonpickle
import pickle
class ucs_login:
    def ucs_login(self,ip,username,password):
    	results = {}
    	handle = UcsHandle(ip, username, password)
    	try:
            handle.login()
	    #mo = handle.query_dn("org-root/boot-policy-ciscotest")
    	    #print(mo)
    	    results['logged_in'] = True
	    #print("Logged In !!!!")
    	except:
            results['logged_in'] = False
    	return handle

def main(ip,username,password):
    hiera_client = hiera.HieraClient('/etc/puppet/modules/ucsm-puppet/hiera.yaml',environment='dev')
    loginInstance=ucs_login()
    handle = loginInstance.ucs_login(ip,username,password)
    ucs_handle=pickle.dumps(handle)
    #handle.logout()
    #print("Logged out successfully")
    #print(type(ucs_handle))
    return ucs_handle
if __name__ == '__main__':
    main()

