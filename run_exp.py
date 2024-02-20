import subprocess
import shlex
import json
import requests 
import time
import os

device1 = "of:0000000000000001"
device2 = "of:0000000000000002"
app = 666

pattern = ''' curl -u onos:rocks -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '''
url = ''' 'http://localhost:8181/onos/v1/flows?appId=666' '''


dummy_payload = """{
        "flows": [
        {
          "priority": 40001,
          "timeout": 0,
          "isPermanent": true,
          "deviceId": "of:0000000000000001",
          "treatment": {
            "instructions": [
              {
                "type": "OUTPUT",
                "port": "2"
              }
            ]
          },
          "selector": {
            "criteria": [
              {
                "type": "IN_PORT",
                "port": "1"
              },
              {
                "type": "ETH_SRC",
                "mac": "9a:d8:73:d8:90:6a"
              },
              {
                "type": "ETH_DST",
                "mac": "9a:d8:73:d8:90:6b"
              }
            ]
          }
        }
        ]
    }"""

class ONOS_interface:
    def __init__(self):
        self.flow_rules = list()
        return

    def run_curl_cmd(self, cmd):
        args = shlex.split(cmd)
        process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        resp = json.loads(stdout.decode('utf-8'))
        return resp

    def get_rule(self):
        delete_str = 'http://localhost:8181/onos/v1/flows/application/666'
        resp = requests.get(delete_str, auth=('onos', 'rocks'))
        return resp

    def delete_rule(self):
        delete_str = 'http://localhost:8181/onos/v1/flows/application/666'
        resp = requests.delete(delete_str, auth=('onos', 'rocks'))
        return resp

    def delete_rules_from_flow_rules(self):
        delete_str = 'http://localhost:8181/onos/v1/flows/of%3A0000000000000001/'
        for flowId in self.flow_rules:
            delete_str_flowId = delete_str + flowId
            resp = requests.delete(delete_str_flowId, auth=('onos', 'rocks'))
            #print("resp =", resp)
        return

    def get_rules_from_flow_rules(self):
        get_str = 'http://localhost:8181/onos/v1/flows/of%3A0000000000000001/'
        for flowId in self.flow_rules:
            get_str_flowId = get_str + flowId
            resp = requests.get(get_str_flowId, auth=('onos', 'rocks'))
            #print("resp =", resp)
        return

    def create_payload_rule(self, priority, timeout):
        data = json.loads(dummy_payload)
        data["flows"][0]['priority'] = int(priority)
        data["flows"][0]['timeout'] = int(timeout)
        json_data_payload = json.dumps(data)
        return json_data_payload

    def run_test3_test(self):
        #(pf2, 2), (pf1, 3.9), (pf2, 6.8)
        json_data_payload1 = self.create_payload_rule(40001, 5)
        cmd_dummy_payload1 = pattern + ''' ' ''' + json_data_payload1 + ''' ' ''' + str(url)
        json_data_payload2 = self.create_payload_rule(40002, 2)
        cmd_dummy_payload2 = pattern + ''' ' ''' + json_data_payload2 + ''' ' ''' + str(url)
        # run the test suite
        time.sleep(2)
        resp1 = self.run_curl_cmd(cmd_dummy_payload2)
        time.sleep(4.8)
        resp3 = self.run_curl_cmd(cmd_dummy_payload2)
        return

    def run_test1(self):
        #(pf1, 2), (pf2, 4.9)
        json_data_payload1 = self.create_payload_rule(40001, 5)
        cmd_dummy_payload1 = pattern + ''' ' ''' + json_data_payload1 + ''' ' ''' + str(url)
        json_data_payload2 = self.create_payload_rule(40002, 2)
        cmd_dummy_payload2 = pattern + ''' ' ''' + json_data_payload2 + ''' ' ''' + str(url)
        # run the test suite
        time.sleep(2)
        resp1 = self.run_curl_cmd(cmd_dummy_payload1)
        time.sleep(2.9)
        resp2 = self.run_curl_cmd(cmd_dummy_payload2)
        return

    def run_test2(self):
        #(pf1, 2), (pf2, 4.1)
        json_data_payload1 = self.create_payload_rule(40001, 5)
        cmd_dummy_payload1 = pattern + ''' ' ''' + json_data_payload1 + ''' ' ''' + str(url)
        json_data_payload2 = self.create_payload_rule(40002, 2)
        cmd_dummy_payload2 = pattern + ''' ' ''' + json_data_payload2 + ''' ' ''' + str(url)
        # run the test suite
        time.sleep(2)
        resp1 = self.run_curl_cmd(cmd_dummy_payload1)
        time.sleep(2.1)
        resp2 = self.run_curl_cmd(cmd_dummy_payload2)
        return

    def run_test3(self):
        #(pf2, 2), (pf1, 3.9), (pf2, 6.8)
        json_data_payload1 = self.create_payload_rule(40001, 5)
        cmd_dummy_payload1 = pattern + ''' ' ''' + json_data_payload1 + ''' ' ''' + str(url)
        json_data_payload2 = self.create_payload_rule(40002, 2)
        cmd_dummy_payload2 = pattern + ''' ' ''' + json_data_payload2 + ''' ' ''' + str(url)
        # run the test suite
        time.sleep(2)
        resp1 = self.run_curl_cmd(cmd_dummy_payload2)
        time.sleep(1.9)
        resp2 = self.run_curl_cmd(cmd_dummy_payload1)
        time.sleep(2.9)
        resp3 = self.run_curl_cmd(cmd_dummy_payload2)
        return

    def run_test4(self):
        #(pf2, 2) (pf1, 3.9), (pf2, 6)
        json_data_payload1 = self.create_payload_rule(40001, 5)
        cmd_dummy_payload1 = pattern + ''' ' ''' + json_data_payload1 + ''' ' ''' + str(url)
        json_data_payload2 = self.create_payload_rule(40002, 2)
        cmd_dummy_payload2 = pattern + ''' ' ''' + json_data_payload2 + ''' ' ''' + str(url)
        # run the test suite
        time.sleep(2)
        resp1 = self.run_curl_cmd(cmd_dummy_payload2)
        time.sleep(1.9)
        resp2 = self.run_curl_cmd(cmd_dummy_payload1)
        time.sleep(2.1)
        resp1 = self.run_curl_cmd(cmd_dummy_payload2)
        return

    def run_test5(self):
        #(pf2, 2) (pf2, 10), (pf1, 11.1)
        json_data_payload1 = self.create_payload_rule(40001, 5)
        cmd_dummy_payload1 = pattern + ''' ' ''' + json_data_payload1 + ''' ' ''' + str(url)
        json_data_payload2 = self.create_payload_rule(40002, 2)
        cmd_dummy_payload2 = pattern + ''' ' ''' + json_data_payload2 + ''' ' ''' + str(url)
        # run the test suite
        time.sleep(2)
        resp1 = self.run_curl_cmd(cmd_dummy_payload2)
        time.sleep(8)
        resp2 = self.run_curl_cmd(cmd_dummy_payload2)
        time.sleep(1.1)
        resp3 = self.run_curl_cmd(cmd_dummy_payload1)
        return

    def run_test6(self):
        #(pf1, 2) (pf1, 13), (pf2, 18.1)
        json_data_payload1 = self.create_payload_rule(40001, 5)
        cmd_dummy_payload1 = pattern + ''' ' ''' + json_data_payload1 + ''' ' ''' + str(url)
        json_data_payload2 = self.create_payload_rule(40002, 2)
        cmd_dummy_payload2 = pattern + ''' ' ''' + json_data_payload2 + ''' ' ''' + str(url)
        # run the test suite
        time.sleep(2)
        resp1 = self.run_curl_cmd(cmd_dummy_payload1)
        time.sleep(13)
        resp2 = self.run_curl_cmd(cmd_dummy_payload1)
        time.sleep(5.1)
        resp3 = self.run_curl_cmd(cmd_dummy_payload2)
        return

onos = ONOS_interface()
#onos.run_test1()
#onos.run_test2()
#onos.run_test3()
#onos.run_test3()
#onos.run_test4()
#onos.run_test5()
#onos.run_test6()


json_data_payload1 = onos.create_payload_rule(40001, 5)
cmd_dummy_payload1 = pattern + ''' ' ''' + json_data_payload1 + ''' ' ''' + str(url)
json_data_payload2 = onos.create_payload_rule(40002, 2)
cmd_dummy_payload2 = pattern + ''' ' ''' + json_data_payload2 + ''' ' ''' + str(url)

def run_test():
    time.sleep(2)
    resp1 = onos.run_curl_cmd(cmd_dummy_payload1)
    print("resp1 =", resp1)
    time.sleep(2)
    resp2 = onos.get_rule()
    print("resp2 =", resp2)
    time.sleep(2)
    resp3 = onos.delete_rule()
    print("resp3 =", resp3)    


for i in range(1, 23):
    priority = int(40000 + i)
    json_data_payload = onos.create_payload_rule(priority, 0)
    cmd_dummy_payload = pattern + ''' ' ''' + json_data_payload + ''' ' ''' + str(url)
    pid = os.fork()
    if pid == 0:
        #onos.get_rule()
        resp_pf = onos.run_curl_cmd(cmd_dummy_payload)
        print("resp_pf =", resp_pf)
        os._exit(0)
    else:
        #time.sleep(0.25)
        onos.delete_rule()
        #time.sleep(2)
        try:
            os.wait()  # Wait for the child process to complete
        except ChildProcessError:
            print("No child processes to wait for.")

# run the test suite
#run_test()



#resp2 = onos.run_curl_cmd(cmd_dummy_payload2)
#time.sleep(1.5)
#resp1 = onos.run_curl_cmd(cmd_dummy_payload1)
#time.sleep(2)
#resp2 = onos.run_curl_cmd(cmd_dummy_payload2)
#time.sleep(2.5)
#resp1 = onos.run_curl_cmd(cmd_dummy_payload1)
#time.sleep(2)
#resp1 = onos.run_curl_cmd(cmd_dummy_payload1)

#time.sleep(10)

# Second test sequence
#time.sleep(2)
#resp1 = onos.run_curl_cmd(cmd_dummy_payload2)
#time.sleep(6)
#resp1 = onos.run_curl_cmd(cmd_dummy_payload1)
#time.sleep(3)
#resp1 = onos.run_curl_cmd(cmd_dummy_payload2)
#time.sleep(2)
#resp1 = onos.run_curl_cmd(cmd_dummy_payload1)
#time.sleep(1.5)
#resp1 = onos.run_curl_cmd(cmd_dummy_payload1)
#time.sleep(5.5)
#resp1 = onos.run_curl_cmd(cmd_dummy_payload2)
