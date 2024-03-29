# CYBR4580/8950 Project Milestone 2: Prototype and Research Paper Outline

## Setup Environments

General information about our environment plans and development strategy can be found in the [prototype](https://github.com/24SP-UNO-Capstone/Milestone1/blob/main/prototype.md) page. 

Documentation about ELK, our deployment methodology, and current settings can be found in the [ELK markdown document](https://github.com/24SP-UNO-Capstone/Milestone1/blob/main/ELK.md). 

Open CTI installation, connector information, RSS feed, and TAXII setup can be found in the [OpenCTI - Docker](https://github.com/24SP-UNO-Capstone/Milestone1/blob/main/OpenCTI%20-%20Docker.md). 

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
 - Successfully set up ELK in a test environment and implemented a basic configuration.
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
> Complexity and Scalability:
> 
>   A CTI framework can be difficult for smaller teams to implement due to limited resources.  Conversely, starting with a more simple framework can lead to a different set of difficulties if the framework needs to scale up.Our proposed OpenCTI solution is scalable and easy to set up.  A base OpenCTI instance can be installed on a workstation with minimal CPU cores, but we would advise at least 16gb of RAM to allocate.

> Resource Intensive:
> 
>   Maintaining a CTI framework can be resource intensive based on many factors like personnel skillsets, specialized tools, or the need for continuing training and education.  Smaller businesses may not have the resources to dedicate to this task. OpenCTI  is largely a hands-off and automated solution once installed and configured. However, it does require a fairly robust base infrastructure on which to be installed.

> Data Overload:
> 
>   Undoubtedly a CTI framework can generate and output an enormous amount of data which can overwhelm a small security team.  The presented logs, alerts, and reports generated with round-the-clock data processing will force the team to prioritize what data is the most important.  This constant feed of data will need to be filtered to only show the most relevant information to executives and decision makers.OpenCTI is configurable with various data connectors allowing small teams to add their preferred data sources to limit the amount of data overload presented to team members.-Privacy and Legal ConcernsDepending on the industry, sharing of threat information may be hampered by privacy or legal challenges.  Security teams of all sizes will need to be aware of any regulatory requirements that could impact the sharing or storage of threat information. This issue is present regardless of team size.  We cannot address this directly, and responsibility falls upon the security team themselves.

> Vendor Lock-In:
> 
>   Some CTI frameworks are proprietary to a vendor's product stack. Any kind of vendor lock like this could present a roadblock if the business decides to change direction.  Keeping with a more open solution would allow for easier transitions. OpenCTI is an open-source project which can be freely implemented.  Depending on the preferred license (Community Edition vs. Enterprise), a differing produce license does apply.

4. Build example automated tooling to ingest and aggregate CTI.
> For this objective we have created an on-prem proof-of-concept (PoC) including several open-source technologies. We selected ELK, OpenCTI, and MISP Threat Sharing for our tooling to ingest, aggregate, and reporting. Each tool has a unique purpose. ELK's primary responsibility is to collect and aggregate all logs from endpoints, threat intelligence feeds, and threat intelligence lists. OpenCTI is a medium for analyzing, aggregating, and ingesting threat intelligence feeds, taxii feeds, rss feeds, and more. MISP provides a medium for ingesting threat intelligence lists from different locations and content types. With all of this data, we can provide both reactive and proactive CTI solutions for potential stakeholders. In a production environment this solution can be modified to use another SIEM/data aggregation solution.




## Research Paper Outline

**Question:** Is it feasible for a SMB to create and leverage the advantages of a Cyber Threat Intelligence program for proactive and reactive analysis?

### Abstract

> In the evolving cyber threat landscape, companies who sit back and take a purely reactive approach to security are bound to pay for it. In order to address modern security threats, organizations must be able to identify and respond to threats before they are realized. Cyber Threat Intelligence (CTI) is the best mechanism to do this. Over the last 20 years, security programs, information-sharing initiatives, and cybersecurity vendors have exploded the CTI market, producing trillions of data points per year for customer consumption. While having access to this data is excellent, the data has to be operationalized into actionable intelligence. Once this intelligence is actionable, the CTI program can provide upper management with data that can provide an advantage for decision-making in the Cybersecurity space. In order to leverage this data, small and medium businesses (SMBs) must identify the feasibility of creating and maintaining a CTI program that utilizes the resources available to them. This paper analyzes whether or not it is feasible for SMBs to create such a program to feed proactive decision-making and reactive response. 

> To answer this question, we must analyze our target audience to identify their available resources and scale our final solution based on that analysis. Based on our current analysis, SMBs have the overall highest spend per user among the groups identified in the SANs SOC Survey. However, these organizations also have the lowest overall security program spending. In order to combat this, we will primarily focus on open-source tooling and freely available threat intelligence. In an actual production deployment, most organizations will likely already have access to commercial threat intelligence feeds through pre-existing vendor relationships, such as via their EDR, Cloud tenant, and SIEM tooling, which can be integrated into our proposed solution. 

 - **Introduction**
   - Brief section: What is Threat Intel, how is it used, benefits of it
   - Brief section: The Intelligence Life Cycle, The Diamond Model
   - Brief section: Stix, TAXII, possible automation of threat intel
   - Identify benefits and need for cyber threat intelligence
   - Stakeholder Analysis \ Audience section 
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

[Project Board](https://github.com/orgs/24SP-UNO-Capstone/projects/1/views/1)