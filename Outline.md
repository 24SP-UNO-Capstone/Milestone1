# Outline
---
 - Research Question: Given the resource constraints of small to medium business (SMB) security teams, what kinds of cyber threat intelligence programs can be setup for proactive and reactive analysis on a (scalable) budget?
 - **Introduction** - JOSH
   - Brief section: What is Threat Intel, how is it used, benefits of it
    - Identify benefits and need for cyber threat intelligence
   - Brief section: The Intelligence Life Cycle, The Diamond Model
   - Brief section: Stix, TAXII, possible automation of threat intel
   - Stakeholder Analysis \ Audience section 

> The cybersecurity landscape constantly evolves between advancements in security technologies, identification of new vulnerabilities, new threat actor capabilities, and many other factors that play into the overall threat landscape. In order to maintain a firm grasp on the bleeding edge of security preparedness and response capabilities, organizations have adopted both proactive and reactive capabilities. Among these capabilities is the adoption of cyber threat intelligence (CTI). CTI, according to Abu (2018), can be defined as "...evidence-based knowledge, including context, mechanisms, indicators, implications and actionable advice, about an existing or emerging threat that can be used to inform decisions regarding the subject's response to that menace or hazard..." (p. 4). This definition highlights two critical aspects of CTI, notably, actionable advice that can be used to inform the decision-making process of security professionals. Adding CTI to the decision-making process is a proactive approach to CTI. On the contrary, reactive CTI utilizes CTI data to enrich and inform the decision-making process after an event. 

> Modern CTI solutions include threat intelligence feeds, tooling, and standards. However, due to the sheer amount of information available and the questionable quality of said data, organizations are left with a mountain of data, not intelligence. In order to combat this, organizations must adopt the intelligence cycle and the diamond model. The intelligence cycle is a repetitive set of phases necessary to acquire actionable intelligence from data. They culminated from a five-step procedure including planning and direction, collection, processing, analysis and production, and dissemination. Each phase of the intelligence cycle has a specific goal, starting with the planning and direction phase. An organization must plan its threat intelligence activities to define the scope and goals of the cycle. Once the goals are identified, data sources can be identified and collected. Once data is collected, it must be processed and normalized into information. Once the information has been obtained, careful analysis can be conducted to identify information that matches the cycle's goal, and the identified information can be produced into the necessary format for the final dissemination phase. 

> Along with adherence to the intelligence cycle, the diamond model is a critical component of a successful CTI program. The diamond model represents a relationship between four core features found in a security event: an adversary, capability, infrastructure, and victim.
> In order for CTI data to be shared, three standards have been created by MITRE to standardize CTI communication. Structured Threat Information Expression (STIX) is a the standard for threat intelligence sharing platforms to describe threat intelligence data. Cyber Observable eXpression XML schema (CyBox) is used to descibe artifacts or events with related data such as an IPv4 address. Finally, Trusted Austomated eXchange of Indicator Information (TAXII) is an opensource protocol specification used to share cyber threat data between organizations. 

> Given the resource constraints, this research has been scoped to identify the capabilities available to small and medium businesses. To identify this audience, research was gathered from data released by the SANs Institute of Technology in 2022 and 2023, identifying the relationship between organization size, security team size, and security budget. Utilizing these three indicators, the average organizational spending and spending per capita could be calculated to identify acceptable restrictions and scope requirements for delivering recommendations to small and medium business stakeholders properly. 
- Citations
  - 10.11591/ijeecs.v10.i1.pp371-379 - Abu (Para. 1)
  - Crowley, C., Filkins, B., & Pescatore, J. (2024, March 13). SANS 2023 SOC Survey. SANS Institute. https://www.sans.org/white-papers/2023-sans-soc-survey/ 


 - **Prior works** - John
   - Discuss findings of prior works, highlight critiques and potential changes in our work.
  
 
> Comparing the more popular existing CTI frameworks (the Diamond Model, MITRE ATT&CK, STIX/TAXII, and Cyber Kill Chain), we can notice some issues and shortcomings of each.

> The Diamond Model provides a structured approach to cyber threats by focusing on four primary elements of an attack: adversary, infastructure, capabilities, and victim.  As a strength, it offers a complete view of an attack for clear visualization, but falls short due to its complexity.  Security staff may need extra training to fully comprehend all that the Diamond Model requires to be successful.

> MITRE ATT&CK is a knowledge base of tactics and techniques, and provides a common language for analyzing cyber threats.  Its community lead contributions along with comprehensive information and standardization makes this a robust framework for monitoring cyber threats.  It is a solid framework with great techincal information but does not often attribute attacks to any bad actors.

> The STIX/TAXII framework provides a common language for sharing and exchange of threat intelligence.  Its strengths revolve around standardization and scalability.  However it is not an informational database, it only provides a common nomenclature for ease of information sharing.

> The Cyber Kill Chain from Lockheed Martin focuses on understanding the stages of a cyber attack and developing defensees.  It promotes a proactive approach to defense while mantaining a simplistic approach.  The framework falls short with its linear methodology which may not be flexble to handle more complex and evolving cyber threats.

> We aim to address these shortcomings and pitfalls by demonstrating a scalable, easy to use framework with open-source tools and a robust data analysis process which can be implemented by a small team of cybersecurity professionals.


**Proactive and Reactive Responses**:

> Cyber threat intelligence frameworks can be both proactive and reactive when developed correctly. Each organization will benefit differently based on its ability to automate reactions, its ability to integrate other security tools utilized in the environment and the product limitations or abilities of those security tools. Not all vendors or products support automation or the ability to proactively block and quarantine based on organization-built blacklists. It's important to take these features into consideration when selecting your security toolsets. 

> In order to be proactive, basic requirements must be met. Organizations should have a documented understanding of their business industry, and their current security posture, and have their specific business processes, procedures, and applications accounted for. 

> Having these items known allows CTI analysis to accurately show potential threats to the organization. For example, a business in the financial industry located inside of the United States is likely to be targeted by the Carbanak group, a Russian-based threat actor that is known for focusing its attacks against United States financial companies. Knowing this information, this business can now examine common tactics, techniques, and procedures that are linked to Carbanak and take a proactive approach to preventing these exploits, patching known vulnerabilities that Carbanak utilizes, and building detections that would catch this specific group, in case they were to be compromised. 

> A reactive approach to CTI is often automated or orchestrated by a SIEM\SOAR tool. Common cases may include network quarantining a host because a file hash on the device became linked to a threat actor. Other common examples may include removing emails from user inboxes when threat intel shows a certain sender as being malicious. It’s not required these actions be automated, some businesses may manually take these steps after an investigation rather than automate it. This manual option is often used to avoid impact from possibly bad intel coming from a source. 

> It's common that organizations at the beginning of their threat intel program will focus their programs on reactive responses, then later on adding proactive activities as the CTI program matures. Experienced programs may also limit the number of alerts generated by low confidence indicators to limit alert fatigue and focus their efforts on assets or identities that trigger multiple alerts or those that trigger critical findings. 

     
**Computing resource requirements**:

> Threat intelligence programs require either on-premises dedicated resources or cloud-based resources to collect, store, perform analysis, and perform actions with the intelligence they gather. 
Using the suggested containerized solution in this framework, the resources needed for on-premises are minimal. A single container host with a modern CPU, 8 GB of RAM, and 1TB hard drive can meet minimum requirements. Additional hard drive space may be needed depending on how long threat intel data is kept and the amount of intel sources. For environments with additional Elastic features, use cases, and automation, a more powerful container host system would be required. 

> The suggested solution is also compatible with cloud-based container hosting providers such as AWS ECS, Azure container apps, or Google Cloud’s GKE service. Many aspects of this solution could also be automated with Python scripting services such as AWS Lambda, Azure functions, or Google Cloud functions. 


**Licensing considerations**:

> At the time of this writing, the suggested solution includes the following licensing considerations. 
>    - Open CTI 
>      - The community edition is subject to the Apache License version 2.0.
>        - This suggested solution utilizes the community edition at no cost to the consumer.
>      - Enterprise edition is available for users with larger budgets.
>        - Not required, however contains additional for advanced deployments.
>    - Elastic Search \ Kibana
>      - Elastic License 2.0 (ELv2)
>        - This suggested solution utilizes the free self-managed (Basic) solution. 
>        - Additional benefits and features are available at a cost, but not required for this deployment. 
>    - Alien Vault Open Threat Exchange (OTX)
>      - Apache License version 2.0.
>    - MISP Threat Sharing
>      - GNU Affero General Public License v3.0
>    - Abuse.ch
>      - Creative Commons CC0 

> It’s important to review licensing agreements as they may have changed since the writing of this framework. Currently, these licenses allow for free, commercial use of these products. Changes in these licenses may mean that usage of these tools may start including costs to your organization. Future revisions may contain commercial usage restrictions or state that unauthorized usage may be considered a violation of law. 

**Inventory of software and hardware**:


> Before developing a threat intelligence program and the infrastructure to support it. It’s important to first have an inventory of software and hardware utilized inside of your environment. This allows later steps of the intel collection process to be curated to your organization’s needs. 

> For example, if your organization utilizes a specific vendor for firewalls and VPN, you will be highly interested in collecting new CVEs for these devices, rather than monitoring for all CVEs related to all firewall or VPN vendors. Thus, greatly reducing the amount of data collection needed.  This same concept will apply towards software utilized inside the environment. 

> A few best practices when generating your inventory of hardware:

>    - Utilize an active discovery tool to identify devices connected to the network
>    - Consider a passive asset discovery tool that can identify devices based on network monitoring capabilities. 
>    - Utilize DHCP logging to update your asset inventory
>    - Periodically run a manual review of your inventory in addition to automated collection techniques. 


> For software assets consider these best practices:

>    - Gather software information from your centrally managed software solutions. Such as MECM, SCCM, Intune, etc.
>    - Gather software information from software agents running on hosts, such as anti-malware, Tanium, SIEM agents, etc. 
>    - Consider a passive software discovery tool that can identity software based on network monitoring abilities. 
>    - Periodically run a manual review of your software inventory in addition to automated collection techniques.



**Estimated FTE time required**

> The suggested framework in this document was developed with the goal of minimizing the amount of maintenance, hands-on activity, or all-around time spent on CTI. However, much like other IT scenarios, a certain amount of routine maintenance will be required. Such as updating containers periodically, rotating API keys regularly, updating automation scripts and config files with up-to-date standards, or general patching of host operating systems. It's expected this work may add 1-5 hours of work for a security professional per month. 


Possible sec-ops pipeline to feed intel into security tools?  Dillon todo
     - SOAR?
     - python?
     - API integrations required?

    
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
