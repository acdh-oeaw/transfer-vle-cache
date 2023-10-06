# Transfer VLE Cache

This is a small python project that transfers TEI entry data stored in a cache
in dboe_annotation into the XML database that can be accessed using the vleserver_basex
API.

## API code generation

The API access code is generated using openapi-python-generator

```bash
yq -o=json '.' dboeannotation_openapi3_0.yaml > dboeannotation_openapi3_0.json
openapi-python-generator --library aiohttp dboeannotation_openapi3_0.json dboeannotation\
# and
yq -o=json '.' vleserver_openapi3_0.yaml > vleserver_openapi3_0.json
openapi-python-generator --library aiohttp vleserver_openapi3_0.json vleserver
```

This code uses the following environment variables

| Variable                    | Description                                      | default                                                   |
|-----------------------------|--------------------------------------------------|-----------------------------------------------------------|
| DBOEANNOTATION_HOST         | DBOE Annotation host that has data in its cache  | https://dboeannotation-test.acdh-dev.oeaw.ac.at           |
| DBOEANNOTATION_USER         | User for this DBOE Annotation host               | vle                                                       |
| DBOEANNOTATION_PASSWORD     | Password for this DBOE Annotation host           | changeme_please                                           |
| VLESERVER_HOST              | The XML database host the data should be sent to | http://localhost:8984                                     |
| VLESERVER_BASIC_AUTH_BASE64 | The already Base64 encoded string after `Basic`  | The equivalent of admin:sha256(admin), needs to be set up |
