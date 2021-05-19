# JSScanner
Js File Scanner
This is Js File Scanner . Which are scan  in js file and  find juicy information Toke,Password Etc.

[![Watch the video](https://img.youtube.com/vi/hsT5BL_EV-g/1.jpg)](https://www.youtube.com/watch?v=hsT5BL_EV-g)

## Installation :
```
git clone https://github.com/0x240x23elu/JSScanner.git
cd JSScanner
pip3 install -r requirements.txt
```

## Note

```
If you Want to Add New Regex , Please check Regex in python regex checker . Regex File Regex.txt
Output file bydefault output.txt
```

## How to Use

```
echo "example.com" | waybackurls | grep -iE '\.js'|grep -ivE '\.json'|sort -u  > j.txt
or
echo "example.com" | waybackurls | httpx > live.txt

```
```
python3 JSScanner.py
Please Enter Any File: text.txt (your links file)
Path Of Regex/Patten File: regex.txt (your regex file)

or

python3 JSScanner.py --urls jsfiles.txt --regex regex.txt --output output.txt
```
## Open redirect 

```
 Now JSScanner fetch open redirect param from Live site
 Copy Below Regex in Regex.txt
 
 (next=|url=|target=|rurl=|dest=|destination=|redir=|redirect_uri=|redirect_url=|redirect=|/redirect/|cgi-bin/|redirect.cgi|/out/|/out|view=|loginto=|image_url=|go=|return=|returnTo=|return_to=|checkout_url=|dest=|redirect=|uri=|path=|continue=|url=|window=|to=|out=|view=|dir=|show=|navigation=|Open=|url=|file=|val=|validate=|domain=|callback=|return=|page=|feed=|host=|port=|next=|data=|reference=|site=)((http|https):\/\/)(([\w.-]*)\.([\w]*)\.([A-z]))\w+
 
(next=|url=|target=|rurl=|dest=|destination=|redir=|redirect_uri=|redirect_url=|redirect=|/redirect/|cgi-bin/|redirect.cgi|/out/|/out|view=|loginto=|image_url=|go=|return=|returnTo=|return_to=|checkout_url=|dest=|redirect=|uri=|path=|continue=|url=|window=|to=|out=|view=|dir=|show=|navigation=|Open=|url=|file=|val=|validate=|domain=|callback=|return=|page=|feed=|host=|port=|next=|data=|reference=|site=)(http|https)

(next=|url=|target=|rurl=|dest=|destination=|redir=|redirect_uri=|redirect_url=|redirect=|/redirect/|cgi-bin/|redirect.cgi|/out/|/out|view=|loginto=|image_url=|go=|return=|returnTo=|return_to=|checkout_url=|dest=|redirect=|uri=|path=|continue=|url=|window=|to=|out=|view=|dir=|show=|navigation=|Open=|url=|file=|val=|validate=|domain=|callback=|return=|page=|feed=|host=|port=|next=|data=|reference=|site=)((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+


```
## video

```
https://www.youtube.com/watch?v=hsT5BL_EV-g
https://youtu.be/hsT5BL_EV-g
[![Watch the video](https://img.youtube.com/vi/hsT5BL_EV-g/1.jpg)](https://www.youtube.com/watch?v=hsT5BL_EV-g)

```
## Some Regex 
```
Thank you 
```
https://github.com/odomojuli
https://github.com/odomojuli/RegExAPI


| Name | Type | Regex |
| :---         |     :---:      |          ---: |
|    |     |    |
|     |       |      |
| Twitter      | Access Token    | [1-9][ 0-9]+-[0-9a-zA-Z]{40}  |
| Twitter	| Access Token | [1-9][ 0-9]+-[0-9a-zA-Z]{40}|	
| Facebook	| Access Token	| EAACEdEose0cBA[0-9A-Za-z]+| 	
| Facebook	| OAuth 2.0	| [A-Za-z0-9]{125}| login/access-tokens/ |
| Instagram	| OAuth 2.0	| [0-9a-fA-F]{7}.[0-9a-fA-F]{32}| 
| Google	| OAuth 2.0 | API Key	| AIza[0-9A-Za-z-_]{35}	| 
| GitHub	| OAuth 2.0	| [0-9a-fA-F]{40}|
| Gmail	| OAuth 2.0	| [0-9(+-[0-9A-Za-z_]{32}.apps.qooqleusercontent.com| 	
| Foursquare	| Client Key	| [0-9a-zA-Z_][5,31]| 	
| Foursquare	| Secret Key	| R_[0-9a-f]{32}| 	
| Picatic	| API Key	| sk_live_[0-9a-z]{32}| 	
| Stripe	| Standard API Key	| sk_live_(0-9a-zA-Z]{24}| 	
| Stripe	| Restricted API Key	| sk_live_(0-9a-zA-Z]{24}| 	
| Finance	Square	| Access Token	| sqOatp-[0-9A-Za-z-_]{22}| 	
| Finance	Square	| OAuth Secret	| q0csp-[ 0-9A-Za-z-_]{43}| 	
| Finance	| Paypal / Braintree	| Access Token	| access_token,production$[0-9a-z]{161[0-9a,]{32}| 	
| AMS	| Auth Token	| amzn.mws]{8}-[0-9a-f]{4}-10-9a-f1{4}-[0-9a,]{4}-[0-9a-f]{12}| 	
| Twilio	| API Key  | 55[0-9a-fA-F]{32}| 	
| MailGun	| API Key	| key-[0-9a-zA-Z]{32}| 
| MailChimp	| API Key	| [0-9a-f]{32}-us[0-9]{1,2}| 	
| Slack	| API Key	| xox[baprs]-[0-9]{12}-[0-9]{12}-[0-9a-zA-Z]{24}| 	
| Amazon Web Services	| Access Key ID	| AKIA[0-9A-Z]{16}| 	
| Amazon Web Services	| Secret Key	| [0-9a-zA-Z/+]{40}| 	
| Google Cloud Platform	| OAuth 2.0	| [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}| 	
| Google Cloud Platform	| API Key	| [A-Za-z0-9_]{21}--[A-Za-z0-9_]{8}| 	
| Heroku	| API Key	| [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}| 	
| Heroku	| OAuth 2.0	| [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}| 
