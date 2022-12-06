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
  "root_domain": "snapsec.co",
  "count": "3",
  "subdomains": [
    "1.snapsec.co",
    "2.snapsec.co",
    "3.snapsec.co"
  ]
}
```


## Extra details

#### Use -oJ for JSON Output

![image](https://user-images.githubusercontent.com/27428157/205863335-0056b391-36ba-4ef9-91e3-aea33683d566.png)
