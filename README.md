MustacheOne
=============================
MustacheOne will quickly let you gather some basic information on IPs or URLs by consolidating the information from different websites.

MustasheOne makes use of the following sites:
* [IPVoid][ipvoid]
* [Network Solutions][networksolutions]
* [Project Honey Pot][projecthoneypot]
* [VirusTotal][virustotal]
* [intoDNS][intodns]
* [NetCraft][netcraft]

Usage:
-----------------
* Single IP usage: MustacheOne.py 208.78.70.16
* Single URL usage: MustacheOne.py github.com
* Combination usage: MustacheOne.py github.com 208.78.70.16 google.com
* Launch WebGUI(Open 127.0.0.1:8080) MustacheOne.py webgui 

Dependencies:
-----------------
* [Python][python]
* [Beautiful Soup][beautifulsoup]
* [simplejson][simplejson]
* [Mako Templating][mako]
* [CherryPy][cherrypy]
* [MarkDown][markdown]

Configuration:
-----------------
You will need to create a file named "config.ini"

Example config.ini
<pre>
	<code>
		[virustotal]
		apikey = yourAPIkey
	</code>
</pre>

[ipvoid]: https://www.ipvoid.com
[networksolutions]: http://www.networksolutions.com
[beautifulsoup]: http://www.crummy.com/software/BeautifulSoup/
[python]: http://www.python.org/
[projecthoneypot]: https://www.projecthoneypot.org/
[robtex]: http://www.robtex.com/
[simplejson]: https://github.com/simplejson/simplejson
[virustotal]: https://www.virustotal.com/
[intodns]: http://www.intodns.com/
[netcraft]: http://news.netcraft.com/
[mako]: http://www.makotemplates.org/
[cherrypy]: http://www.cherrypy.org/
[markdown]: http://packages.python.org/Markdown/

Sample Output for github.com:
-----------------
<pre>

___  ___          _             _           _____            
|  \/  |         | |           | |         |  _  |           
| .  . |_   _ ___| |_ __ _  ___| |__   ___ | | | |_ __   ___ 
| |\/| | | | / __| __/ _` |/ __| '_ \ / _ \| | | | '_ \ / _ \
| |  | | |_| \__ \ || (_| | (__| | | |  __/\ \_/ / | | |  __/
\_|  |_/\__,_|___/\__\__,_|\___|_| |_|\___| \___/|_| |_|\___|                                                            
    https://github.com/cyberphilia/MustacheOne

==========================================================
Report for github.com
2012-10-19 10:17:45.670000
==========================================================
  
************************       
VirusTotal
https://www.virustotal.com
************************ 
	
CLEAN MX: clean site
MalwarePatrol: clean site
ZDB Zeus: clean site
K7AntiVirus: clean site
Yandex Safebrowsing: clean site
MalwareDomainList: clean site
ZeusTracker: clean site
zvelo: clean site
Google Safebrowsing: clean site
BitDefender: clean site
Wepawet: clean site
G-Data: clean site
C-SIRT: clean site
Sucuri SiteCheck: clean site
VX Vault: clean site
SCUMWARE.org: clean site
Opera: clean site
AlienVault: clean site
Sophos: unrated site
Malc0de Database: clean site
SpyEyeTracker: clean site
Phishtank: clean site
Avira: clean site
Antiy-AVL: clean site
Comodo Site Inspector: clean site
SecureBrain: unrated site
ParetoLogic: malware site
URLQuery: unrated site
Minotaur: clean site
         
************************
intoDNS
http://www.intodns.com/
************************
	
**********Parent**********
	***Domain NS records
		Nameserver records returned by the parent servers are:
		ns1.p16.dynect.net.

		['208.78.70.16']

		[TTL=172800]

		ns3.p16.dynect.net.

		['208.78.71.16']

		[TTL=172800]

		ns2.p16.dynect.net.

		['204.13.250.16']

		[TTL=172800]

		ns4.p16.dynect.net.

		['204.13.251.16']

		[TTL=172800]

		 
 a.gtld-servers.net was kind enough to give us that information.
	***TLD Parent Check
		Good.a.gtld-servers.net, the parent server I interrogated, has information for your TLD. This is a good thing as there are some other domain extensions like "co.us" for example that are missing a direct check.
	***Your nameservers are listed
		Good. The parent server a.gtld-servers.net has your nameservers listed. This is a must if you want to be found as anyone that does not know your DNS servers will first ask the parent nameservers.
	***DNS Parent sent Glue
		Good. The parent nameserver sent GLUE, meaning he sent your nameservers as well as the IPs of your nameservers. Glue records are A records that are associated with NS records to

		 provide "bootstrapping" information to the nameserver.(see RFC 1912 section 2.3)
	***Nameservers A records
		Good. Every nameserver listed has A records. This is a must if you want to be found.
**********NS**********
	***NS records from your nameservers
		NS records got from your nameservers listed at the parent NS are:
		ns3.p16.dynect.net['208.78.71.16']

		[TTL=86400]

		ns4.p16.dynect.net['204.13.251.16']

		[TTL=86400]

		ns2.p16.dynect.net['204.13.250.16']

		[TTL=86400]

		ns1.p16.dynect.net['208.78.70.16']

		[TTL=86400]
	***Recursive Queries
		Good. Your nameservers (the ones reported by the parent server) do not report that they allow recursive queries for anyone.
	***Same Glue
		The A records (the GLUE) got from the parent zone check are the same as the ones got from your nameservers. You have to make sure your parent server has the same NS records for your zone as you do according to the RFC. This tests only nameservers that are common at the parent and at your nameservers. If there are any missing or stealth nameservers you should see them below!
	***Glue for NS records
		INFO: GLUE was not sent when I asked your nameservers for your NS records.This is ok but you should know that in this case an extra A record lookup is required in order to get the IPs of your NS records. The nameservers without glue are:
 204.13.251.16
		208.78.70.16
		208.78.71.16
		204.13.250.16

		You can fix this for example by adding A records to your nameservers for the zones listed above.
	***Mismatched NS records
		OK. The NS records at all your nameservers are identical.
	***DNS servers responded
		Good. All nameservers listed at the parent server responded.
	***Name of nameservers are valid
		OK. All of the NS records that your nameservers report seem valid.
	***Multiple Nameservers
		Good. You have multiple nameservers. According to RFC2182 section 5 you must have at least 3 nameservers, and no more than 7. Having 2 nameservers is also ok by me.
	***Nameservers are lame
		OK. All the nameservers listed at the parent servers answer authoritatively for your domain.
	***Missing nameservers reported by parent
		OK. All NS records are the same at the parent and at your nameservers.
	***Missing nameservers reported by your nameservers
		OK. All nameservers returned by the parent server a.gtld-servers.net are the same as the ones reported by your nameservers.
	***Domain CNAMEs
		OK. RFC1912 2.4 and RFC2181 10.3 state that there should be no CNAMEs if an NS (or any other) record is present.
	***NSs CNAME check
		OK. RFC1912 2.4 and RFC2181 10.3 state that there should be no CNAMEs if an NS (or any other) record is present.
	***Different subnets
		OK. Looks like you have nameservers on different subnets!
	***IPs of nameservers are public
		Ok. Looks like the IP addresses of your nameservers are public. This is a good thing because it will prevent DNS delays and other problems like
	***DNS servers allow TCP connection
		OK. Seems all your DNS servers allow TCP connections. This is a good thing and useful even if UDP connections are used by default.
	***Different autonomous systems
		OK. It seems you are safe from a single point of failure. You must be careful about this and try to have nameservers on different locations as it can prevent a lot of problems if one nameserver goes down.
	***Stealth NS records sent
		Ok. No stealth ns records are sent
**********SOA**********
	***SOA record
		The SOA record is:

		Primary nameserver: ns1.p16.dynect.net

		Hostmaster E-mail address: hostmaster.github.com

		Serial #: 1350605005 

		Refresh: 3600 

		Retry: 600 

		Expire: 6048001 weeks

		Default TTL: 60
	***NSs have same SOA serial
		OK. All your nameservers agree that your SOA serial number is 1350605005.
	***SOA MNAME entry
		OK. ns1.p16.dynect.net That server is listed at the parent servers.
	***SOA Serial
		Your SOA serial number is: 1350605005. This can be ok if you know what you are doing.
	***SOA REFRESH
		OK. Your SOA REFRESH interval is: 3600.That is OK
	***SOA RETRY
		Your SOA RETRY value is: 600. Looks ok
	***SOA EXPIRE
		Your SOA EXPIRE number is: 604800.Looks ok
	***SOA MINIMUM TTL
		Your SOA MINIMUM TTL is: 60. This value was used to serve as a default TTL for records without a given TTL value and now is used for negative caching (indicates how long a resolver may

		 cache the negative answer). RFC2308 recommends a value of 1-3 hours. Your value of 60 is OK.
**********MX**********
	***MX Records
		Your MX records that were reported by your nameservers are:
		10aspmx3.googlemail.com 

		74.125.141.27 

		 (no glue)

		10alt1.aspmx.l.google.com 

		74.125.143.27 

		 (no glue)

		10alt2.aspmx.l.google.com 

		74.125.141.26 

		 (no glue)

		10aspmx.l.google.com 

		173.194.70.26 

		 (no glue)

		10aspmx2.googlemail.com 

		74.125.143.27 

		 (no glue)

		[These are all the MX records that I found. If there are some non common MX records at your nameservers you should see them below. ]
	***Different MX records at nameservers
		Good. Looks like all your nameservers have the same set of MX records. This tests to see if there are

		any MX records not reported by all your nameservers and also MX records that have the same hostname but different IPs
	***MX name validity
		Good. I did not detect any invalid hostnames for your MX records.
	***MX IPs are public
		OK. All of your MX records appear to use public IPs.
	***MX CNAME Check
		OK. No problems here.
	***MX A request returns CNAME
		OK. No CNAMEs returned for A records lookups.
	***MX is not IP
		OK. All of your MX records are host names.
	***Number of MX records
		Good. Looks like you have multiple MX records at all your nameservers. This is a good thing and will help in preventing loss of mail.
	***Mismatched MX A
		OK. I did not detect differing IPs for your MX records.
	***Duplicate MX A records
		OK. You have some duplicate MX records (MX records with the same IPs). This is not that good but if you know what you are doing than it's ok.
	***Reverse MX A records (PTR)
		Your reverse (PTR) record:
		27.143.125.74.in-addr.arpa-> la-in-f27.1e100.net
		26.141.125.74.in-addr.arpa-> da-in-f26.1e100.net
		27.141.125.74.in-addr.arpa-> da-in-f27.1e100.net
		26.70.194.173.in-addr.arpa-> fa-in-f26.1e100.net

		You have reverse (PTR) records for all your IPs, that is a good thing.
**********WWW**********
	***WWW A Record
		Your www.github.com A record is:

		www.github.com

		[207.97.227.243]
	***IPs are public
		OK. All of your WWW IPs appear to be public IPs.
	***WWW CNAME
		OK. No CNAME
         
************************
NetCraft
http://news.netcraft.com/
************************
	
Site:http://github.com
Last reboot:	140 days agoUptime graph
Domain:github.com
Netblock owner:	github
IP address:207.97.227.239
Site rank:	10288
Country:US
Nameserver:	ns1.p16.dynect.net
Date first seen:August 2011
DNS admin:	hostmaster@github.com
Domain Registrar:godaddy.com
Reverse DNS:	github.com
Organisation:GitHub, Inc.
Nameserver Organisation:	Dynamic Network Services, Inc., 150 Dow St, Manchester, 03101, United States


Hosting History
Netblock Owner		IP address		OS		Web Server		Last changed
github 3783 20th St. Apt. 3 San Francisco CA US 94110		207.97.227.239		Linux		nginx		15-Oct-2012
github 3783 20th St. Apt. 3 San Francisco CA US 94110		207.97.227.239		Linux		nginx		 8-Oct-2012
github 3783 20th St. Apt. 3 San Francisco CA US 94110		207.97.227.239		Linux		nginx		 8-Oct-2012
github 3783 20th St. Apt. 3 San Francisco CA US 94110		207.97.227.239		Linux		nginx		15-Sep-2012
github 3783 20th St. Apt. 3 San Francisco CA US 94110		207.97.227.239		Linux		nginx		 8-Sep-2012
github 3783 20th St. Apt. 3 San Francisco CA US 94110		207.97.227.239		Linux		nginx/1.0.13		15-Aug-2012
github 3783 20th St. Apt. 3 San Francisco CA US 94110		207.97.227.239		Linux		nginx/1.0.13		14-Jul-2012
github 3783 20th St. Apt. 3 San Francisco CA US 94110		207.97.227.239		Linux		nginx/1.0.13		14-Jun-2012
github 3783 20th St. Apt. 3 San Francisco CA US 94110		207.97.227.239		Linux		nginx/1.0.13		13-May-2012
github 3783 20th St. Apt. 3 San Francisco CA US 94110		207.97.227.239		Linux		nginx/1.0.13		13-Apr-2012
         
************************
Network Solutions
http://www.networksolutions.com
************************
	
Current Registrar: GODADDY.COM, LLC
Record Type: Domain Name
Server Type: Other 0
Lock Status: clientDeleteProhibited
WebSite Status: Active
The data contained in GoDaddy.com, LLC's WhoIs database,
while believed by the company to be reliable, is provided "as is"
with no guarantee or warranties regarding its accuracy.  This
information is provided for the sole purpose of assisting you
in obtaining information about domain name registration records.
Any use of this data for any other purpose is expressly forbidden without the prior written
permission of GoDaddy.com, LLC.  By submitting an inquiry,
you agree to these terms of usage and limitations of warranty.  In particular,
you agree not to use this data to allow, enable, or otherwise make possible,
dissemination or collection of this data, in part or in its entirety, for any
purpose, such as the transmission of unsolicited advertising and
and solicitations of any kind, including spam.  You further agree
not to use this data to enable high volume, automated or robotic electronic
processes designed to collect or compile this data for any purpose,
including mining this data for your own personal or commercial purposes. 

Please note: the registrant of the domain name is specified
in the "registrant" field.  In most cases, GoDaddy.com, LLC 
is not the registrant of domain names listed in this database.


   Registered through: GoDaddy.com, LLC (http://www.godaddy.com)
   Domain Name: GITHUB.COM
      Created on: 09-Oct-07
      Expires on: 09-Oct-18
      Last Updated on: 22-Aug-11

   Registrant:
   GitHub, Inc.
   548 4th St
   San Francisco, California 94107
   United States

   Administrative Contact:
      Werner, Thomas  tom@github.com
      GitHub, Inc.
      589 Howard St.
      Floor 4
      San Francisco, California 94105
      United States
      +1.7606720832

   Technical Contact:
      Werner, Thomas  tom@github.com
      GitHub, Inc.
      589 Howard St.
      Floor 4
      San Francisco, California 94105
      United States
      +1.7606720832

   Domain servers in listed order:
      NS1.P16.DYNECT.NET
      NS2.P16.DYNECT.NET
      NS3.P16.DYNECT.NET
      NS4.P16.DYNECT.NET
The previous information has been obtained either directly from the registrant or a registrar of the domain name other than Network Solutions. Network Solutions, therefore, does not guarantee its accuracy or completeness.
         
************************
Google
http://www.google.com
************************
	
Google queries to help with recon
	* Subdomains excluding www: site:github.com -www.github.com
	* Office files from github.com: filetype:xlsx OR filetype:pptx OR filetype:docx site:github.com
	* PDF files from github.com: filetype:pdf site:github.com
	* Links to github.com: link:github.com
	* Email Addresses: "@github.com" -www.github.com

</pre>

Sample Output for 208.78.70.16:
-----------------
<pre>

___  ___          _             _           _____            
|  \/  |         | |           | |         |  _  |           
| .  . |_   _ ___| |_ __ _  ___| |__   ___ | | | |_ __   ___ 
| |\/| | | | / __| __/ _` |/ __| '_ \ / _ \| | | | '_ \ / _ \
| |  | | |_| \__ \ || (_| | (__| | | |  __/\ \_/ / | | |  __/
\_|  |_/\__,_|___/\__\__,_|\___|_| |_|\___| \___/|_| |_|\___|                                                            
    https://github.com/cyberphilia/MustacheOne

==========================================================
Report for 208.78.70.16
2012-10-19 10:18:26.479000
==========================================================
  
************************       
VirusTotal
https://www.virustotal.com
************************ 
	
CLEAN MX: clean site
MalwarePatrol: clean site
ZDB Zeus: clean site
K7AntiVirus: clean site
Yandex Safebrowsing: clean site
MalwareDomainList: clean site
ZeusTracker: clean site
zvelo: clean site
Google Safebrowsing: clean site
Opera: clean site
G-Data: clean site
C-SIRT: clean site
Sucuri SiteCheck: clean site
VX Vault: clean site
SCUMWARE.org: clean site
Dr.Web: clean site
AlienVault: clean site
Sophos: unrated site
Malc0de Database: clean site
SpyEyeTracker: clean site
Phishtank: clean site
Avira: clean site
Antiy-AVL: clean site
Comodo Site Inspector: clean site
SecureBrain: unrated site
Netcraft: clean site
ParetoLogic: clean site
URLQuery: unrated site
Wepawet: unrated site
Minotaur: clean site
         
************************
IP Void
https://www.ipvoid.com
************************
	
Report: Rescan
					|11-10-2012, 02:48:13 GMT (1 week ago)|All Reports
IP Address: 208.78.70.16 (Network Tools) (View Websites Hosted Here)
ISP: Dynamic Network Services
Organization: Dynamic Network Services
IP Hostname: ns1.p16.dynect.net
IP Country: United States (US)
Detections 0/36 (0.00%)
Status CLEAN

MyWOT: CLEAN
SpamRATS: CLEAN
DNSBL_AbuseCH: CLEAN
EFnet_RBL: CLEAN
TornevallNET: CLEAN
SpamCop: CLEAN
PSBL: CLEAN
WPBL: CLEAN
MalwareDomainList: CLEAN
malc0de: CLEAN
ZeuS Tracker: CLEAN
SpyEye Tracker: CLEAN
PhishTank: CLEAN
Autoshun: CLEAN
DShield: CLEAN
SnortAttack: CLEAN
OpenBL_org: CLEAN
MSRBL: CLEAN
Bogons_Team_Cymru: CLEAN
SCUMWARE: CLEAN
URIBL: CLEAN
MalwareBlacklist: CLEAN
GoogleSafeBrowsing: CLEAN
Spamhaus: CLEAN
SURBL: CLEAN
URLVir: CLEAN
ThreatLog: CLEAN
VScan: CLEAN
ProjectHoneypot: CLEAN
BlockList_de: CLEAN
AHBL: CLEAN
Backscatterer: CLEAN
VirBL: CLEAN
CBL_AbuseAt: CLEAN
SORBS: CLEAN
EmergingThreats: CLEAN
         
************************
Project Honey Pot
http://www.projecthoneypot.org
************************
	
We don't have data on this IP currently. If you know something, you may leave a comment.
         
************************
Network Solutions
http://www.networksolutions.com
************************
	
#
# Query terms are ambiguous.  The query is assumed to be:
#     "n 208.78.70.16"
#
# Use "?" to get help.
#

#
# The following results may also be obtained via:
# http://whois.arin.net/rest/nets;q=208.78.70.16?showDetails=true&showARIN;=false&ext;=netref2
#

NetRange:       208.78.68.0 - 208.78.71.255
CIDR:           208.78.68.0/22
OriginAS:       AS33517
NetName:        DNSINC-2
NetHandle:      NET-208-78-68-0-1
Parent:         NET-208-0-0-0-0
NetType:        Direct Allocation
RegDate:        2007-05-16
Updated:        2012-03-02
Ref:            http://whois.arin.net/rest/net/NET-208-78-68-0-1

OrgName:        Dynamic Network Services, Inc.
OrgId:          DNS-33
Address:        150 Dow St.
City:           Manchester
StateProv:      NH
PostalCode:     03101
Country:        US
RegDate:        2004-01-06
Updated:        2011-06-21
Ref:            http://whois.arin.net/rest/org/DNS-33

OrgAbuseHandle: ABUSE514-ARIN
OrgAbuseName:   Abuse Department
OrgAbusePhone:  +1-603-668-4998 
OrgAbuseEmail:  abuse@dyndns.com
OrgAbuseRef:    http://whois.arin.net/rest/poc/ABUSE514-ARIN

OrgNOCHandle: NOC1473-ARIN
OrgNOCName:   Network Operations Center
OrgNOCPhone:  +1-603-668-4998 
OrgNOCEmail:  noc@dyndns.com
OrgNOCRef:    http://whois.arin.net/rest/poc/NOC1473-ARIN

OrgTechHandle: IAA29-ARIN
OrgTechName:   IP Address Administator
OrgTechPhone:  +1-603-296-1598 
OrgTechEmail:  ip-admin@dyn.com
OrgTechRef:    http://whois.arin.net/rest/poc/IAA29-ARIN

RAbuseHandle: ABUSE514-ARIN
RAbuseName:   Abuse Department
RAbusePhone:  +1-603-668-4998 
RAbuseEmail:  abuse@dyndns.com
RAbuseRef:    http://whois.arin.net/rest/poc/ABUSE514-ARIN

RNOCHandle: NOC1473-ARIN
RNOCName:   Network Operations Center
RNOCPhone:  +1-603-668-4998 
RNOCEmail:  noc@dyndns.com
RNOCRef:    http://whois.arin.net/rest/poc/NOC1473-ARIN

RTechHandle: TJD14-ARIN
RTechName:   Daly, Thomas J
RTechPhone:  +1-603-668-4998 
RTechEmail:  tom@dyn.com
RTechRef:    http://whois.arin.net/rest/poc/TJD14-ARIN

#
</pre>