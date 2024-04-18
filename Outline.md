# Outline
---

 - **Introduction** - JOSH
   - Brief section: What is Threat Intel, how is it used, benefits of it
   - Brief section: The Intelligence Life Cycle, The Diamond Model
   - Brief section: Stix, TAXII, possible automation of threat intel
   - Identify benefits and need for cyber threat intelligence
   - Stakeholder Analysis \ Audience section 

> The cybersecurity landscape is constantly evolving between advancements in security technologies, identification of new vulnerabilities, new threat actor capabilities, and many other factors play into the overall threatscape. In order to maintain a firm grasp on the bleeding edge of security preparedness and response capabilities, organizations have adopted both proactive and reactive capabilities. Among these capabilities is the adoption of cyber threat intelligence (CTI). CTI according to Abu (2018) can be defined as , "...evidence-based knowledge, including context, mechanisms, indicators, implications and actionable advice, about an existing or emerging threat that can be used to inform decisions regarding the subject's response to that menace or hazard..." (p. 4). This definition highlights two critical aspects of CTI, notably, actionable advice that can be used to inform the decision making process of security professionals. 
> Modern CTI solutions include threat intelligence feeds, tooling, and standards. However, due to the sheer amount of information available, and questionable quality of said data, organizations are left with a mountain of data not intelligence. In order to combat this, organization's must adopt the intelligence cycle and the diamond model. The intelligence cycle if a repetitive set of phases necessary to acquire actionable intelligence from data. Culminated from a five step procedure including planning and direction, collection, processing, analysis and production, and dissemination. Each phase of the intelligence cycle has a specific goal starting with the planning and direction phase, an organization must plan their threat intelligence activities to define the scope and goals of the cycle. Once the goals are identified, data sources can be identified and collected. Once data is collected it must be processed and normalized into information. Once the information has been obtained careful analysis can be conducted to identify information that matches the cycles goal, and the identified information can be produced into the necessessary format for the final phase of dissemination
- Citations
  - 10.11591/ijeecs.v10.i1.pp371-379 - Abu (Para. 1)


 - **Prior works** - John
   - Discuss findings of prior works, highlight critiques and potential changes in our work.
  
 
> Comparing the more popular existing CTI frameworks (the Diamond Model, MITRE ATT&CK, STIX/TAXII, and Cyber Kill Chain), we can notice some issues and shortcomings of each.

> The Diamond Model provides a structured approach to cyber threats by focusing on four primary elements of an attack: adversary, infastructure, capabilities, and victim.  As a strength, it offers a complete view of an attack for clear visualization, but falls short due to its complexity.  Security staff may need extra training to fully comprehend all that the Diamond Model requires to be successful.

> MITRE ATT&CK is a knowledge base of tactics and techniques, and provides a common language for analyzing cyber threats.  Its community lead contributions along with comprehensive information and standardization makes this a robust framework for monitoring cyber threats.  It is a solid framework with great techincal information but does not often attribute attacks to any bad actors.

> The STIX/TAXII framework provides a common language for sharing and exchange of threat intelligence.  Its strengths revolve around standardization and scalability.  However it is not an informational database, it only provides a common nomenclature for ease of information sharing.

> The Cyber Kill Chain from Lockheed Martin focuses on understanding the stages of a cyber attack and developing defensees.  It promotes a proactive approach to defense while mantaining a simplistic approach.  The framework falls short with its linear methodology which may not be flexble to handle more complex and evolving cyber threats.

> We aim to address these shortcomings and pitfalls by demonstrating a scalable, easy to use framework with open-source tools and a robust data analysis process which can be implemented by a small team of cybersecurity professionals.
> 
 - **Describe the requirements for a Threat intel program** - Dillon todo
   - Describe the types of CTI proactive vs. reactive Dillon todo
     - Reactive indicating SOAR/SIEM enrichment
     - Proactive generating actionable intelligence based on organization dependent factors such as industry, security posture, business applications, etc.

       
**Computing resource requirements**:

Threat intelligence programs require either on-premises dedicated resources or cloud-based resources to collect, store, perform analysis and perform actions with the intelligence they gather. 
Using the suggested containerized solution in this framework, the resources needed for on-premises are minimal. A single container host with a modern CPU, 8 GB of RAM, and 1TB hard drive can meet minimum requirements. Additional hard drive space may be needed depending on how long threat intel data is kept and the amount of intel sources. For environments with additional Elastic features, use cases, and automation, a more powerful container host system would be required. 

The suggested solution is also compatible with cloud-based container hosting providers such as AWS ECS, Azure container apps, or Google cloud’s GKE service. Many aspects of this solution could also be automated with python scripting services such as AWS Lambda, Azure functions, or Google cloud functions. 


**Licensing considerations**:

At the time of this writing, the suggested solution includes the following licensing considerations. 
   - Open CTI 
     - Community edition is subject to the Apache License version 2.0.
       - This suggested solution utilizes the community edition at no cost to the consumer.
     - Enterprise edition is available for users with larger budgets.
       - Not required, however contains additional for advanced deployments.
   - Elastic Search \ Kibana
     - Elastic License 2.0 (ELv2)
       - This suggested solution utilizes the free self-managed (Basic) solution. 
       - Additional benefits and features are available at a cost, but not required for this deployment. 
   - Alien Vault Open Threat Exchange (OTX)
     - Apache License version 2.0.
   - MISP Threat Sharing
     - GNU Affero General Public License v3.0
   - Abuse.ch
     - Creative Commons CC0 

It’s important to review licensing agreements as they may have changed since the writing of this framework. Currently, these licenses allow for free, commercial use of these products. Changes in these licenses may mean that usage of these tools may start including costs to your organization. Future revisions may contain commercial usage restrictions or state that unauthorized usage may be considered a violation of law. 

**Inventory of software and hardware**:


Before developing a threat intelligence program and the infrastructure to support it. It’s important to first have an inventory of software and hardware utilized inside of your environment. This allows later steps of the intel collection process to be curated to your organization’s needs. 

For example, if your organization utilizes a specific vendor for firewalls and VPN, you will be highly interested in collecting new CVEs for these devices, rather than monitoring for all CVEs related to all firewall or VPN vendors. Thus, greatly reducing the amount of data collection needed.  This same concept will apply towards software utilized inside the environment. 

A few best practices when generating your inventory of hardware:

   - Utilize an active discovery tool to identify devices connected to the network
   - Consider a passive asset discovery tool that can identify devices based on network monitoring capabilities. 
   - Utilize DHCP logging to update your asset inventory
   - Periodically run a manual review of your inventory in addition to automated collection techniques. 


For software assets consider these best practices:

   - Gather software information from your centrally managed software solutions. Such as MECM, SCCM, Intune, etc.
   - Gather software information from software agents running on hosts, such as anti-malware, Tanium, SIEM agents, etc. 
   - Consider a passive software discovery tool that can identity software based on network monitoring abilities. 
   - Periodically run a manual review of your software inventory in addition to automated collection techniques.



Possible sec-ops pipeline to feed intel into security tools?  Dillon todo
     - SOAR?
     - python?
     - API integrations required?
   - FTE hours required to manage \ maintain Dillon todo

    
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