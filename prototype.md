# Prototype

## Technologies
- Elastic Search
- Kibana
- Cribl Stream
- OpenCTI
  - Alienvault OTX
  - Abuse.ch
  - Abuseipdb
  - MITRE ATT&CK
  - CVE
  - NIST API
  - GreyNoise
  - CISA Known Exploited Vulnerabilities 
- MISP Threat Sharing

## Description

We will build a prototype companion application for this project. The application will use open-source software to align with our established goals of keeping the project accessible with a low cost of entry. The main software components will be Elasticsearch, Kibana, and OpenCTI.

Elasticsearch is a search and analytics engine that can absorb various inputs. Real-time data searching is supported along with various APIs and custom query building. Elasticsearch supports clustering nodes with a master node for scalability if data ingestion becomes an issue. 

Historically, ELK stacks utilize a log shipper such as LogStash for ingesting, filtering, and shipping logs from the source endpoint to elastic search for processing. However, our prototype uses two methods to gather and ship logs. The first method is via an Elastic Fleet server. This server serves as the controller for distributing agent policies to the agents being installed on target endpoints. This method will be used to collect data from OpenCTI. The other method of shipping logs will be via Cribl Stream; this solution would require licensing for daily throughput costs in an enterprise environment. Cribl will replace LogStash, presenting itself to the beat agents as an Elastic endpoint before processing and shipping the logs to Elastic search.

Kibana is the last element of an ELK stack. Kibana provides data visualization for the data supplied by Elasticsearch or Logstash. Dashboards can be easily customized to meet an organization's needs and provide easily digestible information. Kibana meshes well with Elasticsearch and Logstash to parse large amounts of data into a more easily consumed format.

OpenCTI may be used as a freely available application for threat visualization and sharing. OpenCTI is an open-source platform allowing organizations to ingest, manage, report, and visualize cyber threat intelligence knowledge. It adheres to the STIX framework and integrates with other tools like MISP, TheHive, MITRE ATT&CK, etc.

We aim to demonstrate a solution that can be run either in an on-premises data center or the cloud. The STIX/TAXII nomenclature will be used throughout to provide a common language for threat analysis and hunting.

<div class="align-center">
	<img src="https://github.com/24SP-UNO-Capstone/Milestone1/blob/main/images/CTI-Stack-V1.2.png" alt="what am I doing here?">
<div>