# SMAX API package

SMAX API package is full API wrapper around functionality of Micro Focus SMAX application

  - Full support for tenant operations
  - Support of administration methods
  - Full support of Suite Admin operation and maintenence

You can also:
  - Automate SMAX using this package
  - Integrate SMAX with other applications (Slack, monitoring and alerting apps etc.)
  - Generate various reports, queries and similar, even though option is not availalbe in SMAX
  - Interact with SMAX using programmatic approach

### Tech

I tried keeping it as simple as possible, only package not included in base Python distribution used is requests

* Requests - used to initiate requests with SMAX urls
* json - used to present information and send information to SMAX
* urlib.parse - used to parse urls for filters etc.

Package is fully open source and available for unlimited usage and modification

### Installation


```sh
pip install smax
```



Example of usage

Smax package is divided in 5 separate classes, each handling one section of SMAX, classes are: 
Run
Build
Configuration
MasterData
SmaxAdmin

there are alos several static methods acting as helpers
```sh
#Example: get incidents by creation date;
from smax import Run

smax = Run(username='user.name@email.com',
           password='password',
           base_url='https://your.smax.instance.com',
           tenant_id=234324)
print(smax.get_incidents('Id,RegisteredForActualService', 'EmsCreationTime btw (1560294000000,1560985199999)'))
> {'meta': {'completion_status': 'OK', 'query_time': 1560981082765367, 'errorDetailsList': [], 'total_count': 11, 'errorDetailsMetaList': []}, 'entities': [{'related_properties': {}, 'entity_type': 'Incident', 'properties': {'LastUpdateTime': 1560353119448, 'Id': '159551', 'RegisteredForActualService': '25052'}}, {'related_properties': {}, 'entity_type': 'Incident', 'properties': {'LastUpdateTime': 1560373353259, 'Id': '159740', 'RegisteredForActualService': '25052'}}, {'related_properties': {}, 'entity_type': 'Incident', 'properties': {'LastUpdateTime': 1560417679626, 'Id': '159840', 'RegisteredForActualService': '25051'}}, {'related_properties': {}, 'entity_type': 'Incident', 'properties': {'LastUpdateTime': 1560852349561, 'Id': '160042', 'RegisteredForActualService': '25051'}}, {'related_properties': {}, 'entity_type': 'Incident', 'properties': {'LastUpdateTime': 1560944646537, 'Id': '160044', 'RegisteredForActualService': '25051'}}, {'related_properties': {}, 'entity_type': 'Incident', 'properties': {'LastUpdateTime': 1560959716546, 'Id': '160050', 'RegisteredForActualService': '24849'}}, {'related_properties': {}, 'entity_type': 'Incident', 'properties': {'LastUpdateTime': 1560854092198, 'Id': '160142', 'RegisteredForActualService': '25051'}}, {'related_properties': {}, 'entity_type': 'Incident', 'properties': {'LastUpdateTime': 1560878672863, 'Id': '160440', 'RegisteredForActualService': '25052'}}, {'related_properties': {}, 'entity_type': 'Incident', 'properties': {'LastUpdateTime': 1560955717971, 'Id': '160442', 'RegisteredForActualService': '25051'}}, {'related_properties': {}, 'entity_type': 'Incident', 'properties': {'LastUpdateTime': 1560942093879, 'Id': '160444', 'RegisteredForActualService': '25051'}}, {'related_properties': {}, 'entity_type': 'Incident', 'properties': {'LastUpdateTime': 1560961427162, 'Id': '160447', 'RegisteredForActualService': '25051'}}]}

#If you ever get stuck, you can always refer to docs built in with the package itself;
print(smax.get_help(smax.get_incidents))
>        Get incidents based on params passed
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, 
        default is None
        :return: Returns JSON result of incident query

```
### Development

Want to contribute? Great!



### Todos

 - Cover package import/export methods
 - Extend base functionality of each module
 - Write functions covering graphing and trending for report generation
 - Unit tests

License
----

MIT


