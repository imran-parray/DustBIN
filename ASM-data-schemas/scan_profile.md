### Scope Request

```json
{
	"scope":"snapsec.co",
	"scan-type":"scan-type-1"
}


```



### Profiles

```json
{
	"name":"scan-type-1",
	"commands":[
	{
		"tool":"nmap",
		"command":"nmap --min-rate 1000 -p500 ${{IP}}"
	},
	{
		"tool":"subfinder",
		"command":"sufider --min-rate 1000 -p500 ${{IP}}"
	},
	{
		"tool":"xhttp",
		"command":"xhttp --min-rate 1000 -p500 $IP"
	},
	{
		"tool":"amass",
		"command":"amass --min-rate 1000 -p500 $IP"
	}

	]
}

/profiles





{
	"name":"scan-type-2",
	"commands":[
	{
		"tool":"nmap",
		"command":"nmap --min-rate 1000 -p500 $IP"
	},
	{
		"tool":"subfinder",
		"command":"sufider --min-rate 1000 -p500 $IP"
	},
	{
		"tool":"xhttp",
		"command":"xhttp --min-rate 1000 -p500 $IP"
	},
	{
		"tool":"amass",
		"command":"amass --min-rate 1000 -p500 $IP"
	}

	]
}

```
