## NSA Cyber Report:

- Obfuscated Data:
  - Obfuscated data makes a CTI analyst's job more difficult due to attackers information being replaced, or concealed in order to attempt to hide their identity, tactics, or intentions. This may include files, executables, exfiled data, or even obfuscation of network traffic.
 
- Encrypted Data:
  - Data is often encrypted increasing the difficulty of inspection and identification of targets. Encryption can occur on both data in transit and at rest. Adversaries may encrypt data to protect or conceal their specific activities.
 
- Anti-Forensic Measures:
  - Threat actors may actively destroy artifacts such as logs and files that would indicate their presence on computers or networks. Therefore making detection of their activities more difficult or impossible. Including making the creation of Indicators of Compromise less likely.

 ## NIST 800-53:

 **Some challenges that apply both to consuming and to producing threat information are:**
- **Establishing Trust.** Trust relationships form the basis for information sharing, but require effort to establish and maintain. Ongoing communication through regular in-person meetings, phone calls, or social media can help accelerate the process of building trust. 

- **Achieving Interoperability and Automation.** Standardized data formats and transport protocols are important building blocks for interoperability. The use of common formats and protocols enables automation and allows organizations, repositories, and tools to exchange threat information at machine speed. Adopting specific formats and protocols, however, can require significant time and resources, and the value of these investments can be substantially reduced if sharing partners require different formats or protocols. During the standards development process, early adopters need to accept the risk that it may be necessary to purchase new tools if significant changes to formats and protocols take place.

- **Safeguarding Sensitive Information.** Disclosure of sensitive information, such as controlled unclassified information (CUI) and personally identifiable information (PII) can result in financial loss, violation of sharing agreements, legal action, and loss of reputation. Sharing security and event information, such as security logs or scan results, could expose the protective or detective capabilities of the organization and result in threat shifting by the actor. 3 The unauthorized disclosure of information may impede or disrupt an ongoing investigation, jeopardize information needed for future legal proceedings, or disrupt response actions such as botnet takedown operations. Organizations should apply handling designations to shared information and implement policies, procedures, and technical controls to actively manage the risks of disclosure of sensitive information.

- **Protecting Classified Information.** Information received from government sources may be marked as classified, making it difficult for an organization to use. Acquiring and maintaining the clearances needed for ongoing access to classified information sources is expensive and time-consuming for organizations. In addition, many organizations employ non-U.S. citizens who are not eligible to hold security clearances and are not permitted access to classified information. [3]




- **Enabling Information Consumption and Publication.** Organizations that want to consume and publish threat information need to have the necessary infrastructure, tools, personnel, and training to do so. Information sharing initiatives should be carefully scoped, because high-frequency, highvolume information exchanges have the potential to overwhelm an organization’s processing capabilities. Organizations that are currently unable to support automated indicator exchange can explore other options such as the manual exchange of best practices or summary indicator information. As additional resources become available, an organization may decide to use automated tools and workflows to process and use threat information


**Some information sharing challenges apply only to the consumption of threat information:**
- **Accessing External Information.** Organizations need the infrastructure to access external sources and incorporate the information retrieved from external sources into local decision-making processes. Information received from external sources has value only to the extent that an organization is equipped to act on the information
- **Evaluating the Quality of Received Information.** Before acting on threat information, an organization needs to confirm that the information is correct, that the threat is relevant, and that the risks of using or not using the information (i.e., potential impacts of action vs. inaction) are well understood.

**Several challenges are only applicable if an organization wants to provide its own information to other organizations:**
- **Complying with Legal and Organizational Requirements.** An organization’s executive and legal teams may restrict the types of information that the organization can provide to others. Such restrictions may include limits on the types of information and the level of technical detail provided. These safeguards are appropriate when they address legitimate business, legal, or privacy concerns, but the imposition of unwarranted or arbitrary restrictions may diminish the utility, availability, quality, and timeliness of shared information.

- **Limiting Attribution.** Organizations may openly participate in information sharing communities, but still require that their contributions remain anonymous. Unattributed information sharing may allow an organization to share more information because there is less perceived risk to the organization’s reputation. The lack of attribution may, however, limit the usefulness of the information because users may have less confidence in information that originates from an unknown source. If the original sources of information cannot be identified, organizations may be unable to confirm that information has been received from multiple independent sources, and thus reduce an organization’s ability to build confidence in received information.
