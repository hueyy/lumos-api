# lumos-api

API description:

GET /devices/
-> JSON
`[ { area_id :: int, id :: str, name :: str, value :: boolean }]`

GET /areas/
-> JSON
`[ {id :: int, name :: str }]`

```
PATCH /devices/<deviceID>
```
send as application/json
`{ area_id :: int, id :: str, name :: str, value :: boolean }`

```
PATCH /areas/<areaID>
```
send as application/json
`{id :: int, name :: str }`

POST /action/
send as application/json
`{device_id :: string, action :: string}`
action is one of {'on', 'off', 'toggle'}



