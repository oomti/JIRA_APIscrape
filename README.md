# JIRA_APIscrape
A python script that scrapes JIRA API into a JSON representation

Uses beautiful soup 4.

Crawls JIRA API documentation from 

https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/

Writes out a JSON containing all API calls in the format of:
```
{
  name : {name
    method
    route
    params : {
      headerParameters
      bodyParameters
      queryParameters
      pathParameters
    }
  },
}
```
---
Manually formatted JSON for indentation and separating lines.

To be used in an other project
