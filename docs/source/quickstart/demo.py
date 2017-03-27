import json
import logging
import os
import sys

from cafe.engine.models.base import AutoMarshallingModel
from cafe.engine.http.client import AutoMarshallingHTTPClient
from cafe.common.reporting import cclogging
from cafe.drivers.unittest.fixtures import BaseTestFixture


class Issue(AutoMarshallingModel):

    def __init__(self, url, repository_url, labels_url, comments_url, events_url,
                 html_url, id, number, title, user, labels, state, locked,
                 assignee, assignees, milestone, comments, created_at,
                 updated_at, closed_at, body, closed_by):
        
        self.url = url
        self.repository_url = repository_url
        self.labels_url = labels_url
        self.comments_url = comments_url
        self.events_url = events_url
        self.html_url = html_url
        self.id = id
        self.number = number
        self.title = title
        self.user = user
        self.labels = labels
        self.state = state
        self.locked = locked
        self.assignee = assignee
        self.assignees = assignees
        self.milestone = milestone
        self.comments = comments
        self.created_at = created_at
        self.updated_at = updated_at
        self.closed_at = closed_at
        self.body = body
        self.closed_by = closed_by

    @classmethod
    def _json_to_obj(cls, serialized_str):
        resp_dict = json.loads(serialized_str)
        user = User(**resp_dict.get('user'))
        
        assignees = []
        for assignee in resp_dict.get('assignees'):
            assignees.append(User(**assignee))

        assignee = User(**resp_dict.get('assignee'))

        labels = []
        for label in labels:
            labels.append(Label(**label))
        
        return Issue(
            url=resp_dict.get('url'),
            repository_url=resp_dict.get('repository_url'),
            labels_url=resp_dict.get('labels_url'),
            comments_url=resp_dict.get('comments_url'),
            events_url=resp_dict.get('events_url'),
            html_url=resp_dict.get('html_url'),
            id=resp_dict.get('id'),
            number=resp_dict.get('number'),
            title=resp_dict.get('title'),
            user=user,
            labels=labels,
            state=resp_dict.get('state'),
            locked=resp_dict.get('locked'),
            assignee=assignee,
            assignees=assignees,
            milestone=resp_dict.get('milestone'),
            comments=resp_dict.get('comments'),
            created_at=resp_dict.get('created_at'),
            updated_at=resp_dict.get('updated_at'),
            closed_at=resp_dict.get('closed_at'),
            body=resp_dict.get('body'),
            closed_by=resp_dict.get('closed_by'))


class User(AutoMarshallingModel):

    def __init__(self, login, id, avatar_url, gravatar_id, url, html_url,
                 followers_url, following_url, gists_url, starred_url,
                 subscriptions_url, organizations_url, repos_url, events_url,
                 received_events_url, type, site_admin):
        
        self.login = login
        self.id = id
        self.avatar_url = avatar_url
        self.gravatar_id = gravatar_id
        self.url = url
        self.html_url = html_url
        self.followers_url = followers_url
        self.following_url = following_url
        self.gists_url = gists_url
        self.starred_url = starred_url
        self.subscriptions_url = subscriptions_url
        self.organizations_url = organizations_url
        self.repos_url = repos_url
        self.events_url = events_url
        self.received_events_url = received_events_url
        self.type = type
        self.site_admin = site_admin
    
    @classmethod
    def _json_to_obj(cls, serialized_str):
        resp_dict = json.loads(serialized_str)
        return User(**resp_dict)


class Label(AutoMarshallingModel):

    def __init__(self, id, url, name, color, default):
        
        self.id = id
        self.url = url
        self.name = name
        self.color = color
        self.default = default
    
    @classmethod
    def _json_to_obj(cls, serialized_str):
        resp_dict = json.loads(serialized_str)
        return Label(**resp_dict)
 

class GitHubClient(AutoMarshallingHTTPClient):

    def __init__(self, base_url):
        super(GitHubClient, self).__init__('json', 'json')
        self.base_url = base_url
        
    def get_project_issue(self, org_name, project_name, issue_id):
            
        url = '{base_url}/repos/{org}/{project}/issues/{issue_id}'.format(
            base_url=self.base_url, org=organization, project=project,
            issue_id=issue_id)
        return self.get(url, response_entity_type=Issue)


os.environ['CAFE_ENGINE_CONFIG_FILE_PATH']='.'
cclogging.init_root_log_handler()
root_log = logging.getLogger()
root_log.addHandler(logging.StreamHandler(stream=sys.stderr))
root_log.setLevel(logging.DEBUG)

base_url = 'https://api.github.com'
organization = 'cafehub'
project = 'opencafe'
client = GitHubClient(base_url)
response = client.get_project_issue(organization, project, '40')

class BasicGitHubTest(BaseTestFixture):

    @classmethod
    def setUpClass(cls):
        super(BasicGitHubTest, cls).setUpClass() # Sets up logging, stats reporting
        base_url = 'https://api.github.com'
        cls.organization = 'cafehub'
        cls.project = 'opencafe'
        cls.client = GitHubClient(base_url)
    
    def test_get_issue_response_code_is_200(self):
        response = self.client.get_project_issue(
            self.organization, self.project, '40')
        self.assertEqual(response.status_code, 200)
    
    def test_id_is_not_null_for_get_issue_request(self):
        response = self.client.get_project_issue(
            self.organization, self.project, '40')
        issue = response.entity
        self.assertIsNotNull(issue.id)