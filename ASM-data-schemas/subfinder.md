#### Tool name: 
Subfinder

#### Reporsitory: 
https://github.com/projectdiscovery/subfinder

#### Tool Function: 
	input: Root Level Domain eg(snapsec.co)
	output: outputs subdomains eg (email.snapsec.co, hello.snapsec.co)



### Expected output:

input: snapsec.co

output: 
```json	
		{
		"root_domain":"snapsec.co",
		"count":"3",
		"subdomains":   [
						"1.snapsec.co",
						"2.snapsec.co",
						"3.snapsec.co"
						]
		}
```