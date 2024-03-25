# CYBR4580/8950 Project Milestone 2: Prototype and Research Paper Outline

## Setup Environments

1. Setup a Proof-of-Concept Taxii \ STIX automation 

## Project Realization 

1. Research and review relevant Cyber Threat Intelligence (CTI) documents, prior CTI program guides, tooling, and other relevant literature.
> We researched more and identified our CTI frameworks, and opensource tools, ingestion sources, etc. Explain some research findings, conclusions, and identify some key sources.
2. Conduct stakeholder analysis to identify the audience and their relevant needs based on organization size or specialized job types.
> We have conducted our stakeholder analysis based on the "SANS SOC Survey" published by the SANS Institute in 2022 and 2023. This report provided us with about one thousand data points indicating the relationship between organization size, information security team size, and an organization's security budget. Based on this survey, we identified the mean value of the organizational security budget and calculated the average spend per user based on an organization's size. From this calculation, we determined that the smaller a business is, the higher the overall security spend per user will be. 
3. Utilizing the relevant literature, create solutions to documented issues with prior implementations of CTI program guides and best practices.
> List some documented findings
4. Build example automated tooling to ingest and aggregate CTI.
> For this objective we have created an on-prem proof-of-concept (PoC) including several open-source technologies. We selected ELK, OpenCTI, and MISP Threat Sharing as 

## Research Paper Outline

### Abstract

Insert 500 work argument made in paper


 - **Executive Summary**
   - Stakeholder Analysis \ Audience section 
   - Brief section: What is Threat Intel, how is it used, benefits of it
   - Brief section: The Intelligence Life Cycle, The Diamond Model
   - Brief section: Stix, TAXII, possible automation of threat intel
 - **Introduction**
   - Identify benefits and need for cyber threat intelligence
 - **Prior works**
   - Discuss findings of prior works, highlight critiques and potential changes in our work.
 - **Describe the requirements for a Threat intel program**
   - Server needed to run the automation of tasks
     - Run via lambda functions instead?  
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
    - Recommended threat intel feeds to monitor
     - Describe the benefits each feed offers.
     - Describe possible automated actions with feeds
     - Describe feeds that require manual intervention
       - CISA known exploited CVEs
       - ISAC Center Alerting
   - Recommended actions to take with the newly collected intel
     - Blocking IPs in firewalls
     - Blocking Hashes in AV
     - Build detections for TTPs
   - Examples of Reports that can be generated with Threat Intel
   - Examples of how threat intel analysts can provide value to their organizations 


## Visual Understanding 

Visual showing automation pipelines? 

Visual showing TAXII explanation? 

Visual showing threat intel from a specific attacker? 

MITRE ATT&CK? 

<div class="align-center">
	<img src="https://github.com/24SP-UNO-Capstone/Milestone1/blob/main/images/CTI-Stack-V1.2.png" alt="what am I doing here?">
<div>


## Issue Tracking \ Planning

TBD


## Presentation

TBD
