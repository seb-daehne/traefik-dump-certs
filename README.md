## Dump traefik certificates from acme.json

This is designed to watch for changes in the acme.json file that traefik generates and dump the certs in to the specified directory


## environment variables

`ACME_JSON` - full path to the acme.json
`CERT_DIR` - specifies the directory the certs get written to

# docker example

```
docker  run --rm -ti -v $(pwd):/certs -v $(pwd)/acme.json:/acme.json --env CERT_DIR=/certs --env ACME_JSON=/acme.json dump_cert`
```
