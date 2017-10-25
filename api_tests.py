#  api_tests.py
##  VRN  10/25/2017

import requests
import json
import time

class Api_tests(object):
    
    def post_newpw(self, pw):
        url = 'http://radiant-gorge-83016.herokuapp.com/hash'
        headers = {'content-type': 'application/json'}
        payload = { "password": pw }
        #print payload
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        rstatus = (r.status_code == requests.codes.ok)
        if ( rstatus == False ):
            print r.status_code
            return rstatus
        else:
            jobid = r.json()
            #print "Job ID = %s" %jobid  
            return jobid           
    
    
    def post_multiple_pw(self, pw1, pw2, pw3):
        url = 'http://radiant-gorge-83016.herokuapp.com/hash'
        headers = {'content-type': 'application/json'}
        payload = []
        newpw = {}
        newpw = {"password":pw1}
        payload.append(newpw)
        newpw = {'password':pw2}
        payload.append(newpw)
        newpw = {'password':pw3}
        payload.append(newpw)    
        #print "payload = %s" %payload
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        rstatus = (r.status_code == requests.codes.ok)
        if ( rstatus == False ):
            print r.status_code
            return rstatus
        else:
            jobid = r.json()
            print "Job ID = %s" %jobid  
            return jobid    
    
    def get_pwhash(self, jobid):
        url = 'http://radiant-gorge-83016.herokuapp.com/hash/%s'
        r = requests.get (url %jobid )
        rstatus = (r.status_code == requests.codes.ok)
        if ( rstatus == False ):
            print r.status_code
            return rstatus
        else:
            pw_hash = r.text
            #print pw_hash
            return pw_hash
          
    def post_shutdown_req(self):
        url = 'https://radiant-gorge-83016.herokuapp.com/hash'
        headers = {'content-type':'application/x-www-form-urlencoded'}
        r = requests.post(url, data='shutdown', headers=headers)
        rstatus = (r.status_code == requests.codes.ok)
        if ( rstatus == False ):
            print r.status_code
            return rstatus
        else:
            return r.status_code          
        
        return
        
    def get_server_stats(self):
        url = 'https://radiant-gorge-83016.herokuapp.com/stats'
        r = requests.get(url)
        rstatus = (r.status_code == requests.codes.ok)
        if ( rstatus == False ):
            print r.status_code
            return rstatus
        else:
            stats1 = r.json()
            stats = r.text
            #print stats
            return stats        
        