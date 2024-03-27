# CYBR4580/8950 Project Milestone 2: Prototype and Research Paper Outline

## Setup Environments

1. Setup a Proof-of-Concept Taxii \ STIX automation 

## Project Realization 

1. Research and review relevant Cyber Threat Intelligence (CTI) documents, prior CTI program guides, tooling, and other relevant literature.
> OpenCTI was selected as the prototype platform as it is an open-source project which can be installed upon any open-source Linux operating system.  OpenCTI is a comprehensive package with the ability to ingest data from dozens of community intelligence feeds.  Data is presented in a straightforward manner for the user to easily see the updated global threat details.

> As mentioned, OpenCTI allows for data connectors to be added as data sources.  We selected the more popular connector feeds: AlienVault, CrowdStrike, AbuseIPDB, and GreyNoise.  These were selected because they are industry heavyweights and can be trusted to provide good data.  However, some of the free API integration with these connectors is rate limited.

2. Conduct stakeholder analysis to identify the audience and their relevant needs based on organization size or specialized job types.
> We have conducted our stakeholder analysis based on the "SANS SOC Survey" published by the SANS Institute in 2022 and 2023. This report provided us with about one thousand data points indicating the relationship between organization size, information security team size, and an organization's security budget. Based on this survey, we identified the mean value of the organizational security budget and calculated the average spend per user based on an organization's size. From this calculation, we determined that the smaller a business is, the higher the overall security spend per user will be. 
3. Utilizing the relevant literature, create solutions to documented issues with prior implementations of CTI program guides and best practices.
> List some documented findings
4. Build example automated tooling to ingest and aggregate CTI.
> For this objective we have created an on-prem proof-of-concept (PoC) including several open-source technologies. We selected ELK, OpenCTI, and MISP Threat Sharing for our tooling to ingest, aggregate, and reporting. Each tool has a unique purpose. ELK's primary responsibility is to collect and aggregate all logs from endpoints, threat intelligence feeds, and threat intelligence lists. OpenCTI is a medium for analyzing, aggregating, and ingesting threat intelligence feeds, taxii feeds, rss feeds, and more. MISP provides a medium for ingesting threat intelligence lists from different locations and content types. With all of this data, we can provide both reactive and proactive CTI solutions for potential stakeholders. In a production environment this solution can be modified to use another SIEM/data aggregation solution.

<div class="align-center">
	<img src="https://github.com/24SP-UNO-Capstone/Milestone1/blob/main/images/CTI-Stack-V1.2.png" alt="what am I doing here?">
<div>

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

Visual showing automation pipelines? 

Visual showing TAXII explanation? 

Visual showing threat intel from a specific attacker? 

MITRE ATT&CK? 


## Issue Tracking \ Planning

TBD


## Presentation

TBD
