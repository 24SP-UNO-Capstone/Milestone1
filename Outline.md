# Outline
---

 - **Introduction** - JOSH
   - Brief section: What is Threat Intel, how is it used, benefits of it
   - Brief section: The Intelligence Life Cycle, The Diamond Model
   - Brief section: Stix, TAXII, possible automation of threat intel
   - Identify benefits and need for cyber threat intelligence
   - Stakeholder Analysis \ Audience section 
 - **Prior works** - John
   - Discuss findings of prior works, highlight critiques and potential changes in our work.
  
 
> Comparing the more popular existing CTI frameworks (the Diamond Model, MITRE ATT&CK, STIX/TAXII, and Cyber Kill Chain), we can notice some issues and shortcomings of each.

> The Diamond Model provides a structured approach to cyber threats by focusing on four primary elements of an attack: adversary, infastructure, capabilities, and victim.  As a strength, it offers a complete view of an attack for clear visualization, but falls short due to its complexity.  Security staff may need extra training to fully comprehend all that the Diamond Model requires to be successful.

> MITRE ATT&CK is a knowledge base of tactics and techniques, and provides a common language for analyzing cyber threats.  Its community lead contributions along with comprehensive information and standardization makes this a robust framework for monitoring cyber threats.  It is a solid framework with great techincal information but does not often attribute attacks to any bad actors.

> The STIX/TAXII framework provides a common language for sharing and exchange of threat intelligence.  Its strengths revolve around standardization and scalability.  However it is not an informational database, it only provides a common nomenclature for ease of information sharing.

> The Cyber Kill Chain from Lockheed Martin focuses on understanding the stages of a cyber attack and developing defensees.  It promotes a proactive approach to defense while mantaining a simplistic approach.  The framework falls short with its linear methodology which may not be flexble to handle more complex and evolving cyber threats.

> We aim to address these shortcomings and pitfalls by demonstrating a scalable, easy to use framework with open-source tools and a robust data analysis process which can be implemented by a small team of cybersecurity professionals.
> 
 - **Describe the requirements for a Threat intel program** - Dillon
   - Describe the types of CTI proactive vs. reactive
     - Reactive indicating SOAR/SIEM enrichment
     - Proactive generating actionable intelligence based on organization dependent factors such as industry, security posture, business applications, etc.
   - Server needed to run the automation of tasks
     - Run via lambda functions instead?  
   - Cloud resource requirements
   - Licensing requirements
   - Collection of known utilized software to check for CVEs
   - Possible sec-ops pipeline to feed intel into security tools
     - SOAR?
     - python?
     - API integrations required?
   - FTE hours required to manage \ maintain
 - **Our suggested threat intel framework**
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
