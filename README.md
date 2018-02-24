# lumos-api

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

### GET /spell/id

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