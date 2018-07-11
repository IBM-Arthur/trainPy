#!/usr/bin/env python

import jenkins

def helloworld(Name):

    jenkins_server_url='http://prdpcrwdsdw02.w3-969.ibm.com:8180'

    try:
        print(Name)
        jenkins.Jenkins(jenkins_server_url, username='wrong', password='wrong',timeout=120)
        print(Name)
    except jenkins.JenkinsException as e:
        print('Jenkins Server connection error!')
        print(e.message)
    print ("hello world!",Name)
if __name__ == "__main__":
    name = input('please input your name:')
    helloworld(name)
