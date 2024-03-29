# CYBR4580/8950 Project Milestone 2: Prototype and Research Paper Outline

## Setup Environments

1. Setup a Proof-of-Concept Taxii \ STIX automation 

## Project Realization 

### Overview 

We have conducted our stakeholder and audience analysis based on information published by the SANS Institute. Our report is intended for IT staff with a focus on cybersecurity obligations in addition to personnel in a security analyst, security engineer, architect, or cybersecurity manager role. It has been designed specifically for organizations with little or zero financial budget designated for Cyber Threat Intelligence goals but still want to improve their intelligence capabilities. 

A prototype of this framework has started to be developed, including successfully starting up an Open CTI platform and implementing a basic configuration. Such as setting up TAXII feed ingestion, RSS feeds, and implementing data connectors to several discovered threat intelligence sources. This prototype utilizes docker to be easily deployable and to streamline a repeatable process for development. 

In addition, we have successfully deployed an ELK stack that will be utilized to collect and aggregate logs from endpoints, Open CTI, and other threat intelligence lists.  

### Outcomes 

 - Completed a stakeholder analysis \ audience selection.
 - Review previous works to gather an understanding of how alternative solutions have been developed.
 - Discovered useful threat intel feeds that can be utilized in a prototype \ proof of concept. 
 - Successfully setup Open CTI in a docker environment and implemented a basic configuration.
   - TAXII Feed ingestion
   - Data Connectors
   - RSS Feed ingestion
 - Successfully set up ELK in a docker environment and implemented a basic configuration.
   - Open CTI threat feed ingestion

### Hindrances 

We encountered issues deploying the original instance of Open CTI. Our lack of experience with docker and the installation process of Open CTI caused missing configuration files, unfilled required settings, default credentials used, and other issues. 

These obstacles have been overcome by reviewing community threads, reading GitHub issues, and analyzing the official troubleshooting guides. Other sources of information such as YouTube demonstrations, stack overflow, and other written resources were used.  

### On-going Risks
 - Open Source License Restrictions 
   - Open CTI does have some restrictions on enterprise use which limits certain features to paying customers. This has a minor impact on our framework as the majority of requirements are met with the free or community version. 
   - ELK TBD
 - Access to technological resources
   - As stated previously, a lack of access to business grade tooling leads us to utilize free or open-source platforms instead. While this is a limiting factor, we still believe we can be successful with our project with the resources available. 
 - Lack of prior works
   - As a team we have been able to collect enough prior work both academically and from commercial resources to aid us in this project so far. Additional research and resources may be needed for our final framework.
 - Student availability
   - As expected with busy schedules, our team has had some minor rescheduling of efforts to fit student availability. These issues have so far been resolved with adjusting meeting times, collaboration over chat tools instead of videos, and weekend working efforts. 
 - Skillset limitations
   - A lack of knowledge and hands-on experience with this topic has made this project a learning experience for all members. We have accommodated most issues with large amounts of research, troubleshooting guides, community support threads and other educational materials to assist us when needed. 


### Additional information

1. Research and review relevant Cyber Threat Intelligence (CTI) documents, prior CTI program guides, tooling, and other relevant literature.
> OpenCTI was selected as the prototype platform as it is an open-source project which can be installed upon any open-source Linux operating system.  OpenCTI is a comprehensive package with the ability to ingest data from dozens of community intelligence feeds.  Data is presented in a straightforward manner for the user to easily see the updated global threat details.

> As mentioned, OpenCTI allows for data connectors to be added as data sources.  We selected the more popular connector feeds: AlienVault, CrowdStrike, AbuseIPDB, and GreyNoise.  These were selected because they are industry heavyweights and can be trusted to provide good data.  However, some of the free API integration with these connectors is rate limited.

2. Conduct stakeholder analysis to identify the audience and their relevant needs based on organization size or specialized job types.
> We have conducted our stakeholder analysis based on the "SANS SOC Survey" published by the SANS Institute in 2022 and 2023. This report provided us with about one thousand data points indicating the relationship between organization size, information security team size, and an organization's security budget. Based on this survey, we identified the mean value of the organizational security budget and calculated the average spend per user based on an organization's size. From this calculation, we determined that the smaller a business is, the higher the overall security spend per user will be. 
3. Utilizing the relevant literature, create solutions to documented issues with prior implementations of CTI program guides and best practices.
> List some documented findings
4. Build example automated tooling to ingest and aggregate CTI.
> For this objective we have created an on-prem proof-of-concept (PoC) including several open-source technologies. We selected ELK, OpenCTI, and MISP Threat Sharing for our tooling to ingest, aggregate, and reporting. Each tool has a unique purpose. ELK's primary responsibility is to collect and aggregate all logs from endpoints, threat intelligence feeds, and threat intelligence lists. OpenCTI is a medium for analyzing, aggregating, and ingesting threat intelligence feeds, taxii feeds, rss feeds, and more. MISP provides a medium for ingesting threat intelligence lists from different locations and content types. With all of this data, we can provide both reactive and proactive CTI solutions for potential stakeholders. In a production environment this solution can be modified to use another SIEM/data aggregation solution.



## Research Paper Outline

**Question:** Is it feasible for a SMB to create and leverage the advantages of a Cyber Threat Intelligence program for proactive and reactive analysis?

### Abstract

Insert 500 work argument made in paper
CISO/Director/Manager reporting
Technological feasibility


 - **Introduction**
   - Stakeholder Analysis \ Audience section 
   - Brief section: What is Threat Intel, how is it used, benefits of it
   - Brief section: The Intelligence Life Cycle, The Diamond Model
   - Brief section: Stix, TAXII, possible automation of threat intel
   - Identify benefits and need for cyber threat intelligence
 - **Prior works**
   - Discuss findings of prior works, highlight critiques and potential changes in our work.
 - **Describe the requirements for a Threat intel program**
   - Server needed to run the automation of tasks
     - Run via lambda functions instead?  
   - Cloud resource requirements
   - Collection of known utilized software to check for CVEs
   - Possible sec-ops pipeline to feed intel into security tools
     - SOAR?
     - python?
     - API integrations required?
   - FTE hours required to manage \ maintain
 - **Our suggested threat intel framework**
   - Describe the types of CTI proactive vs. reactive
     - Reactive indicating SOAR/SIEM enrichment
     - Proactive generating actionable intelligence based on organization dependent factors such as industry, security posture, business applications, etc.
   - The Intelligence Life Cycle
   - The Diamond Model
   - Mitre ATT&CK Framework
   - Threat Intelligence Sharing (STIX/TAXII)
   - Recommended threat intel feeds to monitor
     - Describe the benefits each feed offers.
       - This can be used a baseline to identify the different types/sources of data that are required to generate a sufficiently robust collection of indicators and threat profiles to generate actionable threat intelligence. 
     - Describe possible automated actions with feeds
       - Processing, aggregation, Visualization, etc.
     - Describe feeds/lists that require manual intervention
       - CISA known exploited CVEs
       - ISAC Center Alerting
   - Recommended actions to take with the newly collected intel
     - Blocking IPs in firewalls
     - Blocking Hashes in AV
     - Build detections for TTPs
   - Examples of Reports that can be generated with Threat Intel
     - Decribe the requirements for reporting and the importance of alignments with the needs of management.
   - Examples of how threat intel analysts can provide value to their organizations 
 - **Test Case**
   - Utilizing the prototype environment and a fictional company create a relavent actionable report highlighting the value of the implemented guide. 
     - Report will be based on a single industry vertical to identify threats, and report on those threats matching "management" reporting needs.
 - **Limitations of Implementation and Tooling**
   - Discuss limitations with the CTI guides implementation
     - Focus on limitations of free/opensource tooling for business needs
       - License restrictions, lacking feature parity with enterprise license or other enterprise alternatives. 
       - Lack of support.
     - Realize the potential pitfalls of utilizing open-source data vs. commercial "vetted"/"trusted" data from major cybersecurity vendors.
       - i.e. CS/S1/MS have a vast amount of active intel due to collected data via their CIRT services and customer logs. (CrowdStrike uses customer logs for data, not sure on the rest but it wouldn't surprise me)
 - **Conclusion**
   - Summarize findings and highlight critical points.


## Visual Understanding 

<div class="align-center">
	<img src="https://github.com/24SP-UNO-Capstone/Milestone1/blob/main/images/CTI-Stack-V1.2.png" alt="what am I doing here?">
<div>


## Issue Tracking \ Planning

TBD




