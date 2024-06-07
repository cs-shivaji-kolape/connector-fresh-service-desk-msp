## About the connector
Fresh Service Desk MSP is a cloud-based service desk and IT service management (ITSM) platform designed to streamline service management for businesses. It offers a range of features including incident management, problem management, change management, asset management, and more. Freshservice provides a user-friendly interface for managing service requests, automating workflows, tracking assets, and generating reports. Its multi-tenant architecture ensures data segregation and security for different clients. The connector for Freshservice enables automated actions such as creating, updating, deleting, and closing tickets, enhancing the efficiency of service delivery for managed service providers.
<p>This document provides information about the Fresh Service Desk MSP Connector, which facilitates automated interactions, with a Fresh Service Desk MSP server using FortiSOAR&trade; playbooks. Add the Fresh Service Desk MSP Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Fresh Service Desk MSP.</p>

### Version information

Connector Version: 1.0.0


Authored By: spryIQ.co

Contributors: Jitesh Rathod

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-fresh-service-desk-msp`

## Prerequisites to configuring the connector
- You must have the URL of Fresh Service Desk MSP server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Fresh Service Desk MSP server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Fresh Service Desk MSP</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the URL of the Fresh Service Desk MSP server to which you will connect and perform the automated operations.<br>
<tr><td>Api Key<br></td><td>Specify the api key  that is configured for your account to access the Fresh Service Desk MSP endpoint.<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Create Ticket<br></td><td>Creates a ticket in Fresh Service Desk MSP based on the requester, subject, and other input parameters you have specified.<br></td><td>create_ticket <br/>Investigation<br></td></tr>
<tr><td>Get Ticket By ID<br></td><td>Retrieves details of specific tickets from  Fresh Service Desk MSP on the input parameters you have specified.<br></td><td>get_ticket_by_id <br/>Investigation<br></td></tr>
<tr><td>Delete Ticket By ID<br></td><td>Delete of specific tickets from  Fresh Service Desk MSP on the input parameters you have specified.<br></td><td>delete_ticket_by_id <br/>Investigation<br></td></tr>
<tr><td>Update Ticket<br></td><td>Update a ticket in Fresh Service Desk MSP based on the ticket id and other input parameters you have specified.<br></td><td>update_ticket <br/>Investigation<br></td></tr>
<tr><td>Filter Tickets By Query<br></td><td>Retrieves list of tickets matching the specified query.<br></td><td>filter_tickets_by_query <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Create Ticket
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Subject<br></td><td>Specify the subject of the ticket request that you want to create in Fresh Service Desk MSP.<br>
</td></tr><tr><td>Email<br></td><td>Specify email address  of the requester. If no contact exists with this email address in Fresh Service Desk MSP, it will be added as a new contact.<br>
</td></tr><tr><td>CC Email<br></td><td>Specify email address  of the requester. If no contact exists with this email address in Fresh Service Desk MSP, it will be added as a new contact.<br>
</td></tr><tr><td>Status<br></td><td>Select the status of the ticket request to create in Fresh Service Desk MSP.<br>
</td></tr><tr><td>Priorities<br></td><td>Select the priority of the ticket request to create in Fresh Service Desk MSP.<br>
</td></tr><tr><td>Description<br></td><td>Specify the description of the ticket request to create in Fresh Service Desk MSP.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ticket": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "cc_emails": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "fwd_emails": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "reply_cc_emails": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "fr_escalated": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "spam": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "email_config_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "group_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "priority": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "requester_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "requested_for_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "responder_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "source": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "subject": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "to_emails": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "department_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "due_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "fr_due_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "is_escalated": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description_text": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "sub_category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "item_category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "custom_fields": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "auto_checkbox": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "updated_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "tags": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "attachments": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "workspace_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "resolution_notes": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "resolution_notes_html": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Get Ticket By ID
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Ticket ID<br></td><td>Specify id  of the ticket for which you want to retrieve ticket details from Fresh Service Desk MSP.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ticket": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "cc_emails": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "fwd_emails": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "reply_cc_emails": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "fr_escalated": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "spam": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "email_config_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "group_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "priority": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "requester_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "requested_for_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "responder_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "source": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "subject": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "to_emails": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "department_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "due_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "fr_due_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "is_escalated": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description_text": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "sub_category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "item_category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "custom_fields": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "auto_checkbox": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "updated_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "tags": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "attachments": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "workspace_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "resolution_notes": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "resolution_notes_html": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Delete Ticket By ID
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Ticket ID<br></td><td>Specify id  of the ticket for which you want to retrieve ticket details from Fresh Service Desk MSP.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ticket": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "cc_emails": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "fwd_emails": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "reply_cc_emails": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "fr_escalated": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "spam": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "email_config_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "group_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "priority": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "requester_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "requested_for_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "responder_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "source": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "subject": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "to_emails": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "department_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "due_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "fr_due_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "is_escalated": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description_text": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "sub_category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "item_category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "custom_fields": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "auto_checkbox": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "updated_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "tags": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "attachments": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "workspace_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "resolution_notes": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "resolution_notes_html": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Update Ticket
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Ticket ID<br></td><td>Specify id of the ticket for which you want to retrieve ticket details from Fresh Service Desk MSP.<br>
</td></tr><tr><td>Subject<br></td><td>Specify the subject of the ticket request that you want to update in Fresh Service Desk MSP.<br>
</td></tr><tr><td>Description<br></td><td>Specify the description of the ticket request that you want to update in Fresh Service Desk MSP.<br>
</td></tr><tr><td>Email<br></td><td>Specify email address  of the requester. If no contact exists with this email address in Fresh Service Desk MSP, it will be added as a new contact.<br>
</td></tr><tr><td>Status<br></td><td>Select the status of the ticket request for which you want to create tickets from Fresh Service Desk MSP.<br>
</td></tr><tr><td>Priorities<br></td><td>Select the priority of the ticket request for which you want to retrieve tickets from from Fresh Service Desk MSP.<br>
</td></tr><tr><td>File IRI or Attachment IRI<br></td><td>Specify the file to add as an attachment to the specified a ticket. You can select from the following options: Attachment ID: Specify the attachment ID of the file in the FortiSOAR Attachments module. File IRI: Specify the File IRI of the file in the FortiSOAR Attachments module.<br>
<strong>If you choose 'Attachment ID'</strong><ul><li>Attachment ID: Specify the attachment ID of the file in the FortiSOAR Attachments module.</li></ul><strong>If you choose 'File IRI'</strong><ul><li>File IRI: Specify the File IRI of the file in the FortiSOAR Attachments module.</li></ul></td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ticket": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "cc_emails": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "fwd_emails": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "reply_cc_emails": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "fr_escalated": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "spam": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "email_config_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "group_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "priority": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "requester_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "requested_for_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "responder_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "source": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "subject": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "to_emails": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "department_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "due_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "fr_due_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "is_escalated": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description_text": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "sub_category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "item_category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "custom_fields": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "auto_checkbox": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "updated_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "tags": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "attachments": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "workspace_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "resolution_notes": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "resolution_notes_html": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Filter Tickets By Query
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Query<br></td><td>Specify query to filter ticket request for which you want to retrieve list of tickets from Fresh Service Desk MSP.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "ticket": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "cc_emails": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "fwd_emails": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "reply_cc_emails": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "fr_escalated": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "spam": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "email_config_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "group_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "priority": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "requester_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "requested_for_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "responder_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "source": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "subject": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "to_emails": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "department_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "due_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "fr_due_by": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "is_escalated": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description_text": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "sub_category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "item_category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "custom_fields": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "auto_checkbox": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "updated_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "tags": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "attachments": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "workspace_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "resolution_notes": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "resolution_notes_html": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>
## Included playbooks
The `Sample - fresh-service-desk-msp - 1.0.0` playbook collection comes bundled with the Fresh Service Desk MSP connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Fresh Service Desk MSP connector.

- Create Ticket
- Delete Ticket By ID
- Filter Tickets By Query
- Get Ticket By ID
- Update Ticket

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
