https://www.ncsc.gov.uk/files/An-introduction-to-threat-intelligence.pdf 
CERT-UK whitepaper covering key concepts, threat intelligence’s role with network defense, common languages and frameworks and best practices for threat intelligence. Links to other related works, may be useful when gathering general information related to our topic.  (8 pages)


https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-150.pdf
National Institute of Standards and Technology (NIST) guide to cyber threat information sharing. Great resource coving many different topics along with explanations of terms used. Includes examples of actions that can be taken after the collection of threat information. Will be very useful when building our project.  (43 pages)


https://oasis-open.github.io/cti-documentation/ 
Additional information surrounding Cyber threat Intelligence transport mechanism TAXII and the structured language of STIX. 

https://www.memcyco.com/home/cyber-threat-intelligence-framework/ 
brief webpage from a commercial entity about building a threat intelligence strategy. Has multiple key objectives that could be completed without the vendor being involved. 


https://attack.mitre.org/ 
Collection of useful threat information that we could utilize into our project. Contains TTPs, Threat Actor Campaign information, and mitigation options for findings. 

https://media.defense.gov/2019/Jul/16/2002158108/-1/-1/0/CTR_NSA-CSS-TECHNICAL-CYBER-THREAT-FRAMEWORK_V2.PDF 
National Security Agency (NSA) Technical Cyber Threat Framework V2. Last updated July of 2019, appears very similar to MIRE ATT&CK framework and related information. May not be useful to our project. 


Other sources of information we could possibly utilize in the project. 
https://Ipvoid.com 
https://Urlvoid.com 
https://iplists.firehol.org
https://attack.mitre.org/ 
https://virustotal.com 
https://phishtank.org/ 
https://otx.alienvault.com/ 
https://securitytrails.com   
https://www.cisa.gov/news-events/bulletins/ 
https://nvd.nist.gov/ 
https://www.talosintelligence.com/ 
https://www.paloaltonetworks.com/cortex/threat-intelligence 
https://blog.google/threat-analysis-group/ 
https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/?sort-by=newest-oldest&date=any 
https://therecord.media/ 
https://www.chainalysis.com/ 
https://rules.emergingthreats.net/blockrules/compromised-ips.txt
https://feodotracker.abuse.ch/downloads/ipblocklist.csv
https://openphish.com/feed.txt 
https://sslbl.abuse.ch/blacklist/sslipblacklist.csv
https://osint.digitalside.it/Threat-Intel/digitalside-misp-feed/
https://phishunt.io/
https://www.abuseipdb.com/
https://urlhaus.abuse.ch/downloads/csv/
https://isc.sans.edu/feeds/block.txt 




-----------------------------------------------------------------------------
-----------------------------------------------------------------------------

Kanban board task ideas?

Continue researching past works. 
Build list of officially utilized sources.
Build list of threat information types utilized.
•	Hashes
•	IP addresses
•	Domains
•	TTPs
•	CVEs

Document how personnel in the organization may benefit from this information
•	SOC can utilize this info for incident response
•	Security engineering teams can proactively block threats
•	Vulnerability operations teams can expedite patching processes
•	Fraud teams can investigate abnormal activities 
•	System administrators can harden infrastructure to mitigate risk
•	Other teams? 

Create an example of automation to pull from utilized sources. 
o	TAXII? 
o	Python collection from APIs?

Create examples of actions that organizations can take to defend themselves.
o	Blacklist hashes in AV tools
o	Import into firewall block rules
o	Detect via IDS\IPS
o	Hunt previous logs for newly discovered indicators 

Build out an official markdown document of our CTI framework
•	Include a general “what is CTI and why you should use it”
•	Document the collection of CTI information process
•	Document the actions that should be taken after collection

-----
-----

Resources needed 
Internet Access 
Computer to test the collection of CTI information
Access to literature above 
Python CLI or ability to run scripts 
Chron jobs or ability to schedule tasks 
TAXII software
Access to STIX info 

