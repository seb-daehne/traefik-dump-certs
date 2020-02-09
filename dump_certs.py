#!/usr/bin/env python3
import json
import base64
import os
import inotify.adapters

cert_dir = os.environ.get('CERT_DIR')
if cert_dir is None:
    print("environment variable CERT_DIR not specified - exiting")
    exit(-1)

acme_json = os.environ.get('ACME_JSON')
if acme_json is None:
    print("environment variable ACME_JSON not specified - exiting")
    exit(-1)

def dump_certs():
    with open(acme_json) as acme_file:
        data = json.load(acme_file)

    for value in data['Certificates']:
        print("+ cert: " + str(value['Domain']['Main']))

        filename_cert = os.path.join(cert_dir, value['Domain']['Main']+'_cert.pem')
        cert_file = open(filename_cert, 'wb')
        cert_file.write(base64.b64decode(value['Key']))
        cert_file.close()

        filename_key = os.path.join(cert_dir, value['Domain']['Main']+'_cert.pem')
        key_file = open(filename_key, 'wb')
        key_file.write(base64.b64decode(value['Key']))
        key_file.close()

# initial
dump_certs()

notifier = inotify.adapters.Inotify()
notifier.add_watch(acme_json)

for event in notifier.event_gen(yield_nones=False):
    (_, type_names, _, _) = event
    if 'IN_CLOSE_WRITE' in type_names:
        print(" + change in " + acme_json + " detected - reread")
        dump_certs()
