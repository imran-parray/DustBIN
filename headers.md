
## What is a browser headers
Every time your web browser opens a web page, it sends a "request" for that page. Part of that request includes a series of "headers". A HTTP headers let the client and the server pass additional information with an HTTP request or response. An HTTP header consists of its case-insensitive name followed by a colon (:), then by its value. Whitespace before the value is ignored.

![image](https://user-images.githubusercontent.com/27428157/145567786-0aff25ec-cdb2-4e9c-963e-719d6cf883a0.png)


## How does the browsers behave with Headers

There are only two cases

- If the Header is understandable by the browser it will take a action according to the value in the header 
- If the the browser didn't understand the browser it will just ignore the header 

we can use http://caniuse.com to check any particular header whether its gonna work in all the browsers or not .



## Web Security and Headers 

HTTP security headers are a fundamental part of website security. Upon implementation, they protect you against the types of attacks that your site is most likely to come across. These headers protect against XSS, code injection, clickjacking, etc.

There are alot of security threats which effects the users directly like XSS,Clickjacking and Insufficient Transport of Credentials and many more but these Threats can be protected by telling the browser to do right things . And This can be easily Achieved by using Browser Security Headers.

Like The Clickjacking can be protected by using CSP header and The Unsecure Transmission over HTTP can be fixed by using HSTS header.

## How does it work

When a user visits a site through his/her browser, the server responds with HTTP Response Headers. These headers tell the browser how to behave during communication with the site. These headers mainly comprise of metadata.

Let's take a live example see how an Website which is vulnerable to XSS(Cross Site) Scripting can be protected using security Headers and see how those headers prevent attackers from exploiting the vulnerability on the vulbnerable website.


- Lets say we uploaded this piece of code on our website which is vulnerable to XSS

```php
<?php


if(isset($_GET['name'])){
	echo $_GET['name'];
}

?>
```

- As soon as we visit the website and enter any XSS payload in `name` parameter you can see the XSS pops-up 


![Screen Shot 2021-12-10 at 5 21 39 PM](https://user-images.githubusercontent.com/27428157/145570126-5aa0e2e3-22a1-41f3-b184-edfd03dcc0c4.png)

- and on having an look at the response headers the following headers were send in the response to the browser


![Screen Shot 2021-12-10 at 5 22 41 PM](https://user-images.githubusercontent.com/27428157/145570227-8e98db15-de8f-4ac5-b2c1-9cf5b3b882c7.png)

- 
