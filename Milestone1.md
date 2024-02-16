## Cyber Threat Intelligence Project- Milestone 1: Requirements analysis and planning (Project Proposal Stage)
---
- [Cyber Threat Intelligence Project- Milestone 1: Requirements analysis and planning (Project Proposal Stage)](#cyber-threat-intelligence-project--milestone-1-requirements-analysis-and-planning-project-proposal-stage)
- [Team Members](#team-members)
- [Executive Project Summary](#executive-project-summary)
- [Risk list](#risk-list)
- [Project Methodology](#project-methodology)
    - [Literature Review](#literature-review)
    - [Technical Plan](#technical-plan)
- [Resources Needed](#resources-needed)
- [Proposed project timeline](#proposed-project-timeline)
- [First Sprint Plan](#first-sprint-plan)

## Team Members

- Dillon Petschke
- John Kieran
- Josh Kelley

## Executive Project Summary
---
In today's ultra-connected business world, organizations can no longer afford to be reactive in their cybersecurity posture. Emerging threats are discovered daily, and adversaries often exploit 0-day vulnerabilities, social engineering techniques, and known exploitation methods with increasing success. A proactive response is needed to ensure all assets are sufficiently secured. This project will explore and compile a Cyber Threat Intelligence (CTI) program framework to be applied in many scenarios to better inform organizations' security teams of ongoing threats and attackers. We are choosing this project to expand our expertise as security practitioners and identify issues with prior implementations of CTI frameworks to provide a positive value to potential stakeholders in our final deliverables. 

In many small or medium-sized organizations, security must be given the resources, personnel, or time necessary to deploy a full-scale Cyber Threat Intelligence team adequately. The benefits of such a program can be instrumental in defending the business's assets and critical infrastructure from adversaries. Understanding this is different from the reality for most organizations. We aim to identify the best way to implement an effective CTI program that can produce actionable intelligence for security teams while not requiring state-of-the-art resources that are cost-prohibitive for organizations and security teams of this size. This framework may include open-source threat intelligence feeds, reporting templates, tooling to ingest and aggregate threat intelligence, and industry best practices for implementing an effective program. 



## Risk list
---
|Risk name (value)  | Impact     | Likelihood | Description |
|-------------------|------------|------------|-------------|
| Skillset limitations (32) | 4 | 8 | Due to the diverse nature of IT and Cybersecurity, some members of the group (all of us) may not have been exposed to different methodologies and techniques of conducting necessary tasks. In order to combat this, we will work together to learn as necessary to better the team as a whole. |
| Student availability (56) | 8 | 7 | Due to the team having professional careers and lives outside of CYBR8950, it is likely there will be scheduling limitation and conflicts that occur. This will lead to a major impact as the workload must be distributed evenly to be successful. |
| Open Source License Restrictions (48) | 6 | 8 | Open-source technologies while free to use individually, may have certain restrictions placed on them in the business environment. Seeing as this is the case we will identify those tools, and document the proper method of using the tool and alternatives that do not have this restriction. |
| Access to technological resources (21) | 3 | 7 | Given the scope of the project in CTI, it is likely we will not have access to a number of business grade tooling that would otherwise be available to the consumers of this guide. Given this we can identify Open-Source or free work arounds to appropriately test and convey the success of this guide. |
| Lack of prior works (42) | 7 | 6 | As is standard for research related topics, there can exist a hole in relevant related works. In order to mitigate this risk, we will utilize a number of diverse sources of information including academic journals, blogs, websites, and books. |

## Project Methodology

#### Literature Review
---
The concept of Cyber Threat Intelligence as a preventive defense plan has attracted considerable attention across the industry in recent years.  Existing literature from corporate entities such as Lockheed Martin's [Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) framework or Mandiant's [CTI Analyst Core Competencies Framework](https://www.mandiant.com/resources/blog/cti-analyst-core-competencies-framework) can provide a basis for a robust cybersecurity defense portfolio.  Additionally, academic efforts have also provided their own CTI frameworks, with [The Diamond Model](https://www.recordedfuture.com/blog/diamond-model-intrusion-analysis) as a prime example.  Other academic works include: [TINKER: A framework for Open source Cyberthreat Intelligence](https://arxiv.org/abs/2102.05571) and the [MITRE ATT&CK project](https://attack.mitre.org/ ) developed by the Massachusetts Institute of Technology, Research and Engineering group. 

Further supporting documents like the [Structured Threat Information Expression (STIX™)](https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html) from Oasis Open provide terminology and relational guidance when classifying potential threats. Additional open-source projects such as [TAXII](https://www.oasis-open.org/standard/taxii-version-2-1/ ) are also supported by Oasis Open and are repeatedly mentioned in cited works as an opportunity for automated intelligence collection. 

Government organizations have also developed best practices and recommendations, such as the UK’s (CERT) Computer Emergency Response Team’s [whitepaper](https://www.ncsc.gov.uk/files/An-introduction-to-threat-intelligence.pdf) covering key concepts and strategies. Along with the United States (NSA) National Security Agency and their [V2 Cyber threat framework](https://media.defense.gov/2019/Jul/16/2002158108/-1/-1/0/CTR_NSA-CSS-TECHNICAL-CYBER-THREAT-FRAMEWORK_V2.PDF ). Additionally, the National Institute of Standards and Technology (NIST) guide to [cyber threat information sharing](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-150.pdf) covers multiple topics around intelligence sharing and techniques. 

Multiple private sector or commercially publicized works are also available, such as Memcyco’s [threat intelligence framework](https://www.memcyco.com/home/cyber-threat-intelligence-framework/). Along with large corporations such as Microsoft, Google, Palo Alto, and others disclosing their own threat intelligence, threat actor reports, indicators of compromise, and more. 

Please see [Literature Review.md](https://github.com/24SP-UNO-Capstone/Milestone1/blob/main/Literature%20Review.md) for citations, URLs, and relevance to our project. 

#### Technical Plan 
---

1.	Research and review relevant Cyber Threat Intelligence (CTI) documents, prior CTI program guides, tooling, and other relevant literature.

>This step will identify best practices, successful methodologies, and valuable tools utilized in the industry. Allowing us to learn from others’ failures, lessons learned, or obstacles. We will improve upon these suggested practices and document our findings ultimately informing our final CTI framework development in later steps.

<br/><br/>

2.	Conduct stakeholder analysis to identify the audience and their relevant needs based on organization size or specialized job types.

>Stakeholder analysis will inform our future project scoping efforts. Focusing on specific stakeholders, we can develop the best framework to meet the audience’s needs, suggest actions that are relevant, and generate appropriate report templates.

<br/><br/>

3.	Utilizing the relevant literature, create solutions to documented issues with prior implementations of CTI program guides and best practices.

>Utilizing research and findings from step 1, we will begin to develop our Cyber Threat Intelligence framework. Keeping the stakeholders in mind, we will begin producing our CTI framework document. 

<br/><br/>

4.	Build example automated tooling to ingest and aggregate CTI.

>To be included in our framework document, we will develop an example architecture that can be replicated by the stake holders to begin their CTI ingestion and aggregation journey. 

<br/><br/>

5.	Create examples of CTI reports with actionable intelligence.

>Report templates specifically focused on CTI will be developed for the audience, allowing them to provide value to their organization. These templates can be generated using information collected by CTI feeds or sources. 

<br/><br/>

6.	Create example recommendations based on available security tooling to execute actionable intelligence reports.

>In this step, we will generate actionable steps that the audience can utilize previously generated reports and threat intelligence gathered. For example, suggesting the stakeholder blacklist file hashes in their antivirus tool, or prevent inbound email messages from known malicious senders.  

<br/><br/>

7.	Create an official Cyber Threat Intelligence (CTI) Framework utilizing research findings, implementation best practices, documented examples of successful reporting, and document templates.

>A final CTI framework will be generated and available for public use. Along with intel collection recommendations, suggested tooling, report templates, and actionable examples relevant to our stakeholders. 

<br/><br/>

## Resources Needed
---

|Resource  | Dr. Hale needed? | Investigating Team member | Description |
|-------------------|---------|---------------------------|-------------|
| Open Source Intelligence Feeds | No | Dillon | Any worthwhile CTI will need actionable input.  We will need to source sufficiently useful input streams for framework's users.  The feeds will need to be free or low-cost to make the framework as approachable as possible. |
| Relevant Prior Literature | No | Team | We plan to build on prior industry knowledge and compile the best elements of each. |
| STIX/TAXII Standards | No | Josh | The STIX/TAXII nomenclature allows for improved threat sharing, better detection and response, bolstered collaboration, and enables automation in response to events. |

## Proposed project timeline
---

<div class="align-center">
	<img src="./images/burn_down1.png" alt="what am I doing here?" style="width:497px;height:298px;">
<div>

## First Sprint Plan
---

Kanban board can be located [here](https://github.com/orgs/24SP-UNO-Capstone/projects/1/views/1)

- Dillon Petschke
  - Continue research and review of relevant prior works.
  - Cite works appropriately and create annotations summarizing relevant and important findings.
  - Conduct stakeholder analysis to identify the audience and their relevant needs to target needs based on organization size.
    
- John
  - Continue research and review of relevant prior works.
  - Cite works appropriately and create annotations summarizing relevant and important findings. 

- Josh
  - Continue research and review of relevant prior works.
  - Cite works appropriately and create annotations summarizing relevant and important findings. 
