#!/usr/bin/python3
# coding: utf-8

import simplejson
import subprocess
import json


def main():
    target = "http://testphp.vulnweb.com/"
    crawlergo = "/mnt/f/kali/git/crawlergo/cmd/crawlergo/crawlergo_cmd"
    chrome = "/mnt/f/kali/dev/chrome-linux/chrome"

    cmd = [ crawlergo , "-c", chrome, "-o", "json", target]
    rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = rsp.communicate()
	#  "--[Mission Complete]--"  is the end-of-task separator string
    result = simplejson.loads(output.decode().split("--[Mission Complete]--")[1])
    req_list = result["req_list"]
    print(json.dumps(req_list[0], indent=4))

    print("############all_req_list###############")
    all_req_list = result["all_req_list"]
    print(json.dumps(all_req_list[0], indent=4))

    print("#############all_domain_list###########")
    all_domain_list = result["all_domain_list"]
    print(json.dumps(all_domain_list[0], indent=4))

    print("##############sub_domain_list##########")
    sub_domain_list = result["sub_domain_list"]
    print(json.dumps(sub_domain_list[0], indent=4))

if __name__ == '__main__':
    main()
