INCIDENT_ISSUE_SUMMARY_TEMPLATE = """
{color:red}*Confidential Information - For Internal Use Only*{color}

*Incident Details*
Description: {{description}}
Type: {{incident_type}}
Priority: {{priority}}
Cost: {{cost}}

*Incident Resources*
[Conversation|{{conversation_weblink}}]
[Investigation Document|{{document_weblink}}]
[Storage|{{storage_weblink}}]
[Conference|{{conference_weblink}}]

Incident Commander: [~{{commander_username}}]
"""

CASE_ISSUE_SUMMARY_TEMPLATE = """
{color:red}*Confidential Information - For Internal Use Only*{color}

*Case Details*
Description: {{description}}
Resolution: {{resolution}}
Type: {{case_type}}
Severity: {{case_severity}}
Priority: {{case_priority}}

*Case Resources*
[Investigation Document|{{document_weblink}}]
[Storage|{{storage_weblink}}]

Investigator: [~{{assignee_username}}]
"""
