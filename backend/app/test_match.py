from services.match_service import match_resumes

jd_text = """
Workflow and Process Optimization

Analyze and map existing processes (bids, staffing, HR, finance, technical production, reporting) to identify opportunities for automation and AI-enabled improvement.
Prioritize a backlog of use cases based on impact, feasibility, risk, and alignment with business goals.

Stakeholder Collaboration And Requirements

Engage cross-functional teams to gather requirements, clarify pain points, and co-design solutions that address business needs.
Communicate complex technical concepts clearly to both technical and non-technical stakeholders.

Technology Scouting And Solution Design

Research internal and external markets for cutting-edge AI, RPA, and digital tools, including those used across SYSTRA business units, and assess fit for purpose and IT standards.
Evaluate build-vs-buy options and create solution designs, prototypes/PoCs, and business cases.

Delivery and Deployment

Lead end-to-end delivery from concept through deployment, ensuring alignment with architecture, security, data privacy, and internal IT guidelines.
Recommend and support rollout of AI/RPA platforms, integrations, and automations; coordinate with vendors and internal IT as needed.
Produce high-quality documentation (designs, runbooks, SOPs) and ensure knowledge transfer.

Project Management

Lead full project lifecycle from concept to deployment, ensuring compliance with internal IT guidelines.

Change Enablement and Adoption 

Drive change management, communication, and training to maximize adoption and value realization.
Provide hyper care support, gather feedback, and iterate solutions post-launch.

Governance, Risk, and Responsible AI 

Ensure solutions adhere to responsible AI principles, model risk management, and data governance.
Establish monitoring, performance baselines, and controls for ongoing operations.

Impact Measurement and Reporting 

Define KPIs and success metrics (e.g., cycle time reduction, cost savings, error rate, adoption) and report outcomes to stakeholders and leadership.

Profile/Skills

Profile

3–5 years of experience in business analysis, consulting, or process improvement, with a focus on AI and automation.
Hands-on experience in coding, solution development, and deployment.
Familiarity with Large Language Models (LLMs) and AI tools compatible with the SYSTRA IT framework.
Excellent communication and interpersonal skills; proven ability to collaborate effectively across technical and non-technical teams.
Strong analytical, problem-solving, and documentation skills.

Preferred Skills

Experience with RPA platforms (e.g., UiPath, Power Automate, Automation Anywhere).
Knowledge of machine learning concepts and frameworks; exposure to MLOps and model lifecycle basics is a plus.
Strong project management skills with a track record of delivering complex initiatives.
Proven success implementing AI/RPA projects from discovery to scaled deployment.
Advantageous: experience with APIs and integrations, data analysis/BI (e.g., Power BI), Python/SQL, and process mining tools.

Systra is an equal opportunities company; this position is open to all applicants.
"""

results = match_resumes(jd_text)

for r in results:
    print(r)