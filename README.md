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