# ** normalize data of dataset  **


## URL
|                   |                                       |
| ----------------- | :-----------------------------------: |
| ** Method **      | GET                                   |
| ** Structure **   | /api/:version/:dataset/normalize/     |
| ** Example **     | /api/v1/cats_2d/normalize/            |

## Header Params
    
|Key                  |Value                   |Required      |Descript ion                                            |
| ------------------- | :--------------------: | :----------: | ----------                                            |
|X-Access             |String                  |true          |Username of the user who access this api               |

## Path Params

|Field Name  |Type          |Required      |Description              |
| ---------- | :----------: | :----------: | --------------------    |
| version    |String        |true          |version identifier       |
| dataset    |String        |true          |name's dataset           |


## Success Response
```json
{
  "count": 3,
  "data": {
    "class": {
      "0": 1,
      "1": 2,
      "2": 1
    },
    "point": {
      "0": [0.5,0.5],
      "1": [1.0,0.0],
      "2": [0.5,1.0]
    }
  },
  "dimension": 2
}
```

## Error Response
```json
{
  "code": 400,
  "error": {
    "code": 1,
    "message": "Missing header"
  }
}
```

## HTTP Status code

|Error Code   |Meaning                                                                                          |
| ----------- | :----------------------------------------------------------------------------------------------:|
|400          |	Bad Request – Missing header, wrong input data format, or case is not available to be assigned. |
|404          |	Not Found - The specified could not be found.                                                   |
|500          |	Internal Server Error – Something bad happens on the server/database.                           |