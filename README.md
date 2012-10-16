MustacheOne
=============================
MustacheOne will quickly let you gather some basic information on IPs or URLs by consolidate the information from different websites.

MustasheOne makes use of the following sites:
* [IPVoid][ipvoid]
* [Network Solutions][networksolutions]
* [Project Honey Pot][projecthoneypot]
* [VirusTotal][virustotal]
* [intoDNS][intodns]

Usage:
-----------------
* Single IP usage: MustacheOne.py 208.78.70.16
* Single URL usage: MustacheOne.py github.com
* Combination usage: MustacheOne.py github.com 208.78.70.16 google.com

Dependencies:
-----------------
* [Python][python]
* [Beautiful Soup][beautifulsoup]
* [simplejson][simplejson]

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