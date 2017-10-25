#  runtests.py
##  VRN  10/25/2017

import requests
import json
import time

from api_tests import Api_tests
testrun1 = Api_tests()

class Runtests:

    def test1(self, passw):
        print "Test 1 runnning: POST new password test..."
        response1 = testrun1.post_newpw(passw)
        if ( response1 == False ):
            print "POST new password test failed."
        else:
            print "POST new password test passed. New Job ID: %s" %response1
        print "response1 = %s" %response1
        return response1


    def test2(self, response):
        if (response != False): 
            print "Test 2 running: GET password hash test..."
            response2 = testrun1.get_pwhash(response)
            if ( response2 == False ):
                print "GET password hash test failed." 
            else:
                print "GET password hash test passed. New password hash: %s" %response2
            
        return 
    
    
    def test3(self, pw1, pw2, pw3):
        print "Test 3 running: POST multiple new passwords test..."
        multipw_response = testrun1.post_multiple_pw(pw1, pw2, pw3)
        if ( multipw_response == False ):
            print "POST multiple new passwords test failed."
        else: 
            print "POST multiple new passwords test passed. New Job IDs: %s" %multipw_response
        
        return multipw_response
 
    def test4(self):
        print "Test 4 running: GET server stats test..."
        resp = testrun1.get_server_stats()
        if ( resp == False ):
            print "GET server stats test failed."
        else: 
            print "GET server stats test passed. New Server stats: %s" %resp
        
        return 

    def test5(self):
        print "Test 5 running: POST shutdown request..."
        resp = testrun1.post_shutdown_req()
        if ( resp == False ):
            print "POST shutdown request failed."
        else: 
            print "POST shutdown request passed. " 
        
        return 

def main():
    print " >> Starting the test execution now <<"
    
    runtests = Runtests()
    
    resp = runtests.test1("angry_monkey")       # POST new password test
    runtests.test2(resp)                        # GET password hash test
    runtests.test3("new_test1", "another_test2", "zyx000")      # POST multiple new passwords test
    runtests.test4()                            # GET server stats test
    runtests.test5()                            # Shutdown test. Comment this line out as needed

    print " All done"

if __name__ == '__main__':
    main()
    