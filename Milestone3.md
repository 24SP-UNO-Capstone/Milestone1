# CYBR4580/8950 Project Milestone 3: Prototype and Research Paper 

## Overview 

## Environment Setup

## Project Realization 

## Research Paper Outline

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
