#!/usr/bin/env python
import argparse
import time

import pygerduty.v2

def string_to_csv_list(str):
  rtn = ""
  for char in str:
    rtn += "%d," % ord(char)
  return rtn[:-1]

def query_incident(pager, services, csvfile):
  incidents = pager.incidents.list(statuses=["triggered", "acknowledged"],
    service_ids=services)
  incident_list = []
  for incident in incidents:
    title = incident.title.replace(",", " ")
    incident_str = "%s %s" % (incident.service.id, title)
    print incident_str
    incident_list.append(incident_str)
  incident_list.sort()
  incident_list_str = ",".join(incident_list)
  # normally, one incident length is 100,
  # so 10000 is for about 100 incidents, 
  # and that's a lot.
  incident_list_str = incident_list_str.ljust(10000)[:10000]
  # 1st column is the target
  result = "0," + string_to_csv_list(incident_list_str) + "\n"
  csvfile.write(result)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--key", help="PagerDuty API Key", required=True)
  parser.add_argument("--policy", help="PagerDuty policy to monitor", required=True)
  parser.add_argument("--csv", help="Output csv file", required=True)
  args = parser.parse_args()

  pager = pygerduty.v2.PagerDuty(args.key)
  service_to_query = []
  for service in pager.escalation_policies.show(args.policy).services:
    # get all our services
    #print "%s - %s" % (service.id, service.summary)
    service_to_query.append(service.id)

  with open(args.csv, 'a') as csvfile:
    while True:
      print "querying..."
      query_incident(pager, service_to_query, csvfile)
      time.sleep(600)


if __name__ == "__main__":
  main()
