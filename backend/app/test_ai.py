from groq_service import extract_structured_data

sample_resume = """
Parth Tolia
• +91 505429901 • Dubai, UAE • parthtolia517@gmail.com
• https://www.linkedin.com/in/parth-tolia-aab04577/
SUMMARY
Seasoned RPA and Automation Specialist with 10 years of experience designing and deploying intelligent automation across diverse domains including Audit, Banking, Telecom, Tax, HR, IT, Finance, Insurance, Business Development, and Advisory. Expert in UiPath, Automation Anywhere, and Power Automate with a strong focus on process reengineering, SDLC, and agile delivery. Adept at translating complex business requirements into scalable automation solutions, leading cross-functional teams, and driving digital transformation initiatives that boost efficiency and ROI.
WORK EXPERIENCE
Grant Thornton UAE – Dubai, UAE 08/2022 - PRESENT
Senior Executive
• Spearheaded end-to-end RPA initiatives across multiple departments including Audit, Tax, HR, IT, Business Development, and Advisory, using Power Automate, Automation Anywhere, and SharePoint Online to enhance operational efficiency and accuracy.
• Drove the full automation lifecycle from process discovery to hypercare, ensuring seamless deployments aligned with digital transformation goals.
• Leveraged AI/ML capabilities for OCR, unstructured data processing, and intelligent routing.
• Provided strategic guidance to stakeholders during automation exploration and solutioning phases, ensuring alignment with business objectives.
• Led cross-functional teams, coordinating efforts between internal developers and external vendors to ensure timely and quality RPA delivery.
• Championed RPA best practices and frameworks, fostering a culture of continuous improvement and innovation.
First Abu Dhabi Bank – Dubai, UAE 01/2022 - 08/2022
Senior RPA Consultant
• Led automation delivery across critical banking processes using UiPath, including Orchestrator APIs, OCR, Excel, Outlook, SharePoint, and cognitive components.
• Created detailed automation documentation including PDD, SDD, and BRD, ensuring traceability and clarity across the SDLC.
• Contributed to the evolution of RPA frameworks, enhancing reusability and maintainability.
• Acted as a key liaison between business stakeholders and technical teams to ensure automation alignment with organizational KPIs.
Etisalat – Dubai, UAE 11/2019 - 01/2022
Senior RPA Developer
• Delivered enterprise-grade automation solutions across Telecom operations using UiPath, improving business continuity and reducing manual effort.
• Managed the installation, upgrade, and maintenance of UiPath ecosystem (Studio, Orchestrator, Process Mining, Insights, and Action Center).
• Directed the operations team and coordinated with vendor partners to deliver high-quality RPA solutions within agile project timelines.
Cognizant Technology Solutions – Pune, India 01/2018 - 10/2019
Associate
• Led RPA implementations for HR and Insurance domains using Agile and DevOps methodologies, ensuring automation scalability and efficiency.
• Collaborated with business analysts to identify automation candidates and prepared robust documentation.
• Provided technical leadership on multiple parallel projects, ensuring adherence to coding standards and delivery timelines.
Infosys LTD.– Pune, India 02/2015 - 01/2018
Senior RPA Developer
• Automated ELT pipelines and OBIEE report scheduling using ODI and Informatica, significantly reducing manual intervention.
• Integrated RPA with enterprise reporting systems, enhancing data flow and accuracy.
Windowmaker Software – Gujarat, India 04/2014 - 01/2015
Software Developer
• Developed internal tools using C# .NET and Oracle PL/SQL to enhance system performance and database interactions.
• Created stored procedures and triggers that reduced query latency and improved data integrity.
EDUCATION
Dharmsinh Desai University - Gujarat, India
Bachelor of Technology in Computer Engineering, April 2014
PROFESSIONAL SKILLS
• RPA & Intelligent Automation Tools: UiPath (Studio, Orchestrator, Insights, Process Mining, Action Center), Automation Anywhere A360, Power Automate Desktop & Cloud, AI Builder, Document Understanding, Cognitive Services
• Programming & Scripting: C#, Python, Java, VBScript, VBA, PL/SQL
• Automation Technologies & Integrations: SharePoint Online, Excel Automation, Outlook Integration, PDF Processing, OCR & Cognitive Services, REST/SOAP APIs, Orchestrator APIs
• Database Technologies: SQL Server, Oracle, MySQL – Query optimization, stored procedures, functions, packages
• ETL & Reporting Tools: Oracle Data Integrator (ODI), Informatica, Power BI – Data transformation, report automation, dashboard creation
• Software Development & DevOps: Agile, Scrum, Git, Jira, SVN – SDLC management and source control
• Process Documentation & Design: Process Design Documents (PDD), Solution Design Documents (SDD), Business Requirement Documents (BRD), Technical Design Documents (TDD)
• Others: PandaDoc, Excel Macros, Regex, JSON/XML Parsing, Exception Handling & Logging Frameworks
CERTIFICATION
• UiPath: UiPath Certified Advanced RPA Developer, Foundation, Orchestrator for Developers, Document Understanding
• Automation Anywhere: Advanced RPA Professional (A2019), Master RPA (A360), Bot Developer
• Microsoft Power Platform: PL-500, PL-900, Power Automate Developer Badge
"""

data = extract_structured_data(sample_resume)
print(data)