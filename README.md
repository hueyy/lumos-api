# lumos-api

## Devices

### GET /devices/
-> JSON
`[ { area_id :: int, id :: str, name :: str, value :: boolean }]`

### GET /areas/
-> JSON
`[ {id :: int, name :: str }]`

### PATCH /devices/<deviceID>
send as application/json
`{ area_id :: int, id :: str, name :: str, value :: boolean }`

### PATCH /areas/<areaID>
send as application/json
`{id :: int, name :: str }`

### POST /action/
send as application/json
`{device_id :: string, action :: string}`
action is one of {'on', 'off', 'toggle'}

## Spells

### GET /spell
JSON response:
```
[
    {
        "actions": {
            "555": {
                "device_id": 100,
                "id": 555,
                "value": "on"
            },
            "666": {
                "action": "off",
                "device_id": 101,
                "id": 666
            }
        },
        "id": 100,
        "trigger": {
            "data": {
                "schedule": "daily",
                "time": "0700"
            },
            "type": "clock"
        }
    }
]
```

### GET /spells/id

### DELETE /<spell_id>/trigger

### DELETE /<spell_id>/action/<action_id>

### PUT /<spell_id>/trigger
JSON request:
```
{
    "trigger":{
        "type":"clock",
        "schedule":"everyday",
        "time":"0700"
}
```


### PUT /<spell_id>/action
JSON request:
```
{
    "action":{
        "device_id":"434234",
        "action":"toggle"
    }
```