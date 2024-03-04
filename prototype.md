We will build a prototype companion application for this project.  The application will use open-source software to keep aligned with our established goals of keeping the project accessible with a lost entry cost.  The main software components will be Elasticsearch, Logstash, and Kibana which is known as an ELK Stack within the cybersecurity industry.

Elasticsearch is a search and analytics engine which can absorb a wide variety of inputs.  Real-time data searching is supported along with various APIs and custom query building.  Elasticsearch supports scalability if data ingestion becomes an issue.  

Logstash is the data pipeline service which does the input ingesting, transforms it (if needed), and sends it to a storage area.  It can handle structured and nonstructured data which adds to its processing versatility.  Logstash also supports multiple protocols like syslog or Beats allowing it to be adaptable to nearly any configuration.  Like Elasticsearch, Logstash is also scalable.

Kibana is the last element of an ELK stack.  Kibana provides data visualization for the data supplied by Elasticsearch or Logstash.  Dashboards can be easily customized for an organization's needs to provide easily digestible information.  Kibana meshes well with Elasticsearch and Logstash to parse large amounts of data into a more easily consumed format.


Our goal is to have a packaged application which can be run either in a Docker container or on a standalone virtual machine/workstation.  The STIX/TAXII nomenclature will be used throughout to provide a common language for threat analysis and hunting.
