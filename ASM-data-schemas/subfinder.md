#### Tool name: 
Subfinder

#### Reporsitory: 
https://github.com/projectdiscovery/subfinder

#### Tool Function: 
	input: Root Level Domain eg(snapsec.co)
	output: outputs subdomains eg (email.snapsec.co, hello.snapsec.co)



### Expected output:

input: snapsec.co

output:  For each subdomain Found, Create this JSON record:

```json	
{
  "id": 1234,
  "owner": "org_1234",
  "report_id": "1234",
  "type": "subdomain",
  "value": "emails.snapsec.tech",
  "root_domain": "wakeb.tech",
  "source": "subfinder"
}


```


## Extra details

#### Use -oJ for JSON Output

![image](https://user-images.githubusercontent.com/27428157/205863335-0056b391-36ba-4ef9-91e3-aea33683d566.png)
