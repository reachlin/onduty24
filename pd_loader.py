#!/usr/bin/env python
import argparse
import time

import pygerduty.v2

def query_incident(pager, services, csvfile):
  for incident in pager.incidents.list(statuses=["triggered", "acknowledged"], service_ids=services.keys()):
    title = incident.title.replace(",", " ")
    print "%s, %s, %s" % (incident.service.id, incident.id, title)
    # FIXME: not sure how long we can have for a string for ML
    services[incident.service.id] += title
  keys_sorted = services.keys()
  keys_sorted.sort()
  # change to 1, 2, or 3
  csvfile.write("0,")
  for item in keys_sorted:
    csvfile.write(",%s,%s" % (item, services[item]))

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--key", help="PagerDuty API Key", required=True)
  parser.add_argument("--policy", help="PagerDuty policy to monitor", required=True)
  parser.add_argument("--csv", help="Output csv file", required=True)
  args = parser.parse_args()

  pager = pygerduty.v2.PagerDuty(args.key)
  service_to_query = {}
  for service in pager.escalation_policies.show(args.policy).services:
    #print "%s - %s" % (service.id, service.summary)
    service_to_query[service.id] = ""

  with open(args.csv, 'a') as csvfile:
    while True:
      print "querying..."
      query_incident(pager, service_to_query, csvfile)
      time.sleep(600)


if __name__ == "__main__":
  main()
