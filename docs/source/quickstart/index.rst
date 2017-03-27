===========
Quick Start
===========

**The goal of this portion of the guide is to be a very deliberate step-by-step
explanation of not only how to use OpenCafe components, but to also explain
what types of problems are solved by using OpenCafe.**

To get started, let's install and initialize OpenCafe. We can do this by
running the following commands:

.. code-block:: bash

    pip install opencafe
    cafe-config init

As an example, lets write a few tests for the GitHub API. Let's assume that we
don't have language bindings or SDKs for our API. We can create a simple
client using the BaseHTTPClient class provided by the OpenCafe HTTP plugin, which
is a lightweight wrapper for the `requests` package. First, we'll need to
install the http plugin:

.. code-block:: bash

    cafe-config plugin install http

Now we can create a simple script to request a list of the repositories in
the CafeHub project:

.. code-block:: python
    
    import json

    from cafe.engine.http.client import BaseHTTPClient


    client = BaseHTTPClient()
    response = client.get('https://api.github.com/orgs/cafehub/repos')
    print response.status_code
    print json.dumps(response.json(), indent=2)

This will generate some warnings that we will address later, but the outcome
should be similar to the following:

.. code-block:: bash

    200
    [
        {
            "issues_url": "https://api.github.com/repos/CafeHub/opencafe/issues{/number}",
            "deployments_url": "https://api.github.com/repos/CafeHub/opencafe/deployments",
            "stargazers_count": 0,
            "forks_url": "https://api.github.com/repos/CafeHub/opencafe/forks",
            "mirror_url": null,
            "subscription_url": "https://api.github.com/repos/CafeHub/opencafe/subscription",
            "notifications_url": "https://api.github.com/repos/CafeHub/opencafe/notifications{?since,all,participating}",
            "collaborators_url": "https://api.github.com/repos/CafeHub/opencafe/collaborators{/collaborator}",
            "updated_at": "2017-03-06T20:16:40Z",
            "private": false,
            "pulls_url": "https://api.github.com/repos/CafeHub/opencafe/pulls{/number}",
            "issue_comment_url": "https://api.github.com/repos/CafeHub/opencafe/issues/comments{/number}",
            "labels_url": "https://api.github.com/repos/CafeHub/opencafe/labels{/name}",
            "has_wiki": false,
            "full_name": "CafeHub/opencafe",
            "owner": {
                "following_url": "https://api.github.com/users/CafeHub/following{/other_user}",
                "events_url": "https://api.github.com/users/CafeHub/events{/privacy}",
                "organizations_url": "https://api.github.com/users/CafeHub/orgs",
                "url": "https://api.github.com/users/CafeHub",
                "gists_url": "https://api.github.com/users/CafeHub/gists{/gist_id}",
                "html_url": "https://github.com/CafeHub",
                "subscriptions_url": "https://api.github.com/users/CafeHub/subscriptions",
                "avatar_url": "https://avatars3.githubusercontent.com/u/6557140?v=3",
                "repos_url": "https://api.github.com/users/CafeHub/repos",
                "received_events_url": "https://api.github.com/users/CafeHub/received_events",
                "gravatar_id": "",
                "starred_url": "https://api.github.com/users/CafeHub/starred{/owner}{/repo}",
                "site_admin": false,
                "login": "CafeHub",
                "type": "Organization",
                "id": 6557140,
                "followers_url": "https://api.github.com/users/CafeHub/followers"
            },
            "statuses_url": "https://api.github.com/repos/CafeHub/opencafe/statuses/{sha}",
            "id": 16419963,
            "keys_url": "https://api.github.com/repos/CafeHub/opencafe/keys{/key_id}",
            "description": "This is a mirror of https://github.com/stackforge/opencafe",
            "tags_url": "https://api.github.com/repos/CafeHub/opencafe/tags",
            "downloads_url": "https://api.github.com/repos/CafeHub/opencafe/downloads",
            "assignees_url": "https://api.github.com/repos/CafeHub/opencafe/assignees{/user}",
            "contents_url": "https://api.github.com/repos/CafeHub/opencafe/contents/{+path}",
            "has_pages": false,
            "git_refs_url": "https://api.github.com/repos/CafeHub/opencafe/git/refs{/sha}",
            "open_issues_count": 21,
            "clone_url": "https://github.com/CafeHub/opencafe.git",
            "watchers_count": 0,
            "git_tags_url": "https://api.github.com/repos/CafeHub/opencafe/git/tags{/sha}",
            "milestones_url": "https://api.github.com/repos/CafeHub/opencafe/milestones{/number}",
            "languages_url": "https://api.github.com/repos/CafeHub/opencafe/languages",
            "size": 753,
            "homepage": "",
            "fork": true,
            "commits_url": "https://api.github.com/repos/CafeHub/opencafe/commits{/sha}",
            "releases_url": "https://api.github.com/repos/CafeHub/opencafe/releases{/id}",
            "issue_events_url": "https://api.github.com/repos/CafeHub/opencafe/issues/events{/number}",
            "archive_url": "https://api.github.com/repos/CafeHub/opencafe/{archive_format}{/ref}",
            "comments_url": "https://api.github.com/repos/CafeHub/opencafe/comments{/number}",
            "events_url": "https://api.github.com/repos/CafeHub/opencafe/events",
            "contributors_url": "https://api.github.com/repos/CafeHub/opencafe/contributors",
            "html_url": "https://github.com/CafeHub/opencafe",
            "forks": 3,
            "compare_url": "https://api.github.com/repos/CafeHub/opencafe/compare/{base}...{head}",
            "open_issues": 21,
            "git_url": "git://github.com/CafeHub/opencafe.git",
            "svn_url": "https://github.com/CafeHub/opencafe",
            "merges_url": "https://api.github.com/repos/CafeHub/opencafe/merges",
            "has_issues": true,
            "ssh_url": "git@github.com:CafeHub/opencafe.git",
            "blobs_url": "https://api.github.com/repos/CafeHub/opencafe/git/blobs{/sha}",
            "git_commits_url": "https://api.github.com/repos/CafeHub/opencafe/git/commits{/sha}",
            "hooks_url": "https://api.github.com/repos/CafeHub/opencafe/hooks",
            "has_downloads": false,
            "watchers": 0,
            "name": "opencafe",
            "language": "Python",
            "url": "https://api.github.com/repos/CafeHub/opencafe",
            "created_at": "2014-01-31T20:35:38Z",
            "pushed_at": "2017-03-15T18:07:14Z",
            "forks_count": 3,
            "default_branch": "master",
            "teams_url": "https://api.github.com/repos/CafeHub/opencafe/teams",
            "trees_url": "https://api.github.com/repos/CafeHub/opencafe/git/trees{/sha}",
            "branches_url": "https://api.github.com/repos/CafeHub/opencafe/branches{/branch}",
            "subscribers_url": "https://api.github.com/repos/CafeHub/opencafe/subscribers",
            "permissions": {
            "admin": false,
            "push": false,
            "pull": true
            },
            "stargazers_url": "https://api.github.com/repos/CafeHub/opencafe/stargazers"
        }
    ]

The BaseHTTPClient simply passes the response back as `requests` would, so we
can treat the response similarly to view its content. At this point, it
doesn't look like the http plugin is adding any more value than `requests`
would. Let's see what we can do about that. First, let's enable logging and
see what happens.

.. code-block:: python

    import json
    import logging
    import os
    import sys

    from cafe.engine.http.client import BaseHTTPClient
    from cafe.common.reporting import cclogging

    os.environ['CAFE_ENGINE_CONFIG_FILE_PATH']='.'
    cclogging.init_root_log_handler()
    root_log = logging.getLogger()
    root_log.addHandler(logging.StreamHandler(stream=sys.stderr))
    root_log.setLevel(logging.DEBUG)

    client = BaseHTTPClient()
    response = client.get('https://api.github.com/orgs/cafehub/repos')

With logging enabled, lets execute our script again to see the difference.

.. code-block:: bash

    Daryls-MacBook-Pro:~ dwalleck$ python test.py
    Environment variable 'CAFE_MASTER_LOG_FILE_NAME' is not set. A null root log handler will be used, no logs will be written.(<cafe.engine.http.client.BaseHTTPClient object at 0x1067c8cd0>, 'GET', 'https://api.github.com/repos/cafehub/opencafe/commits?per_page=1') {}
    No section: 'PLUGIN.HTTP'.  Using default value '0' instead
    Starting new HTTPS connection (1): api.github.com
    https://api.github.com:443 "GET /repos/cafehub/opencafe/commits?per_page=1 HTTP/1.1" 200 None

    ------------
    REQUEST SENT
    ------------
    request method..: GET
    request url.....: https://api.github.com/repos/cafehub/opencafe/commits
    request params..: per_page=1
    request headers.: {'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'User-Agent': 'python-requests/2.13.0'}
    request body....: None


    -----------------
    RESPONSE RECEIVED
    -----------------
    response status..: <Response [200]>
    response time....: 1.32189202309
    response headers.: {'X-XSS-Protection': '1; mode=block', 'Content-Security-Policy': "default-src 'none'", 'Access-Control-Expose-Headers': 'ETag, Link, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval', 'Transfer-Encoding': 'chunked', 'Last-Modified': 'Wed, 15 Mar 2017 18:07:14 GMT', 'Access-Control-Allow-Origin': '*', 'X-Frame-Options': 'deny', 'Status': '200 OK', 'X-Served-By': '5aeb3f30c9e3ef6ef7bcbcddfd9a68f7', 'X-GitHub-Request-Id': 'E552:10884:425C8E:54CAC9:58D2A217', 'ETag': 'W/"a29b0e5499900a03b28b4fcda31f90b0"', 'Link': '<https://api.github.com/repositories/16419963/commits?per_page=1&page=2>; rel="next", <https://api.github.com/repositories/16419963/commits?per_page=1&page=416>; rel="last"', 'Date': 'Wed, 22 Mar 2017 16:11:03 GMT', 'X-RateLimit-Remaining': '42', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'Server': 'GitHub.com', 'X-GitHub-Media-Type': 'github.v3; format=json', 'X-Content-Type-Options': 'nosniff', 'Content-Encoding': 'gzip', 'Vary': 'Accept, Accept-Encoding', 'X-RateLimit-Limit': '60', 'Cache-Control': 'public, max-age=60, s-maxage=60', 'Content-Type': 'application/json; charset=utf-8', 'X-RateLimit-Reset': '1490201561'}
    response body....: [{"sha":"6cf95ff563fe136ff90e3a39c0f78f4d6abd3318","commit":{"author":{"name":"Daryl Walleck","email":"daryl.walleck@rackspace.com","date":"2017-03-15T18:07:14Z"},"committer":{"name":"Jose Idar","email":"joseidar@gmail.com","date":"2017-03-15T18:07:14Z"},"message":"Replaces the Gerrit workflow docs with the Github (#44)\n\nworkflow. Addresses issue #40.","tree":{"sha":"2d9205fa5e774f27f30e5e150cfea53a08e851db","url":"https://api.github.com/repos/CafeHub/opencafe/git/trees/2d9205fa5e774f27f30e5e150cfea53a08e851db"},"url":"https://api.github.com/repos/CafeHub/opencafe/git/commits/6cf95ff563fe136ff90e3a39c0f78f4d6abd3318","comment_count":0},"url":"https://api.github.com/repos/CafeHub/opencafe/commits/6cf95ff563fe136ff90e3a39c0f78f4d6abd3318","html_url":"https://github.com/CafeHub/opencafe/commit/6cf95ff563fe136ff90e3a39c0f78f4d6abd3318","comments_url":"https://api.github.com/repos/CafeHub/opencafe/commits/6cf95ff563fe136ff90e3a39c0f78f4d6abd3318/comments","author":{"login":"dwalleck","id":843116,"avatar_url":"https://avatars2.githubusercontent.com/u/843116?v=3","gravatar_id":"","url":"https://api.github.com/users/dwalleck","html_url":"https://github.com/dwalleck","followers_url":"https://api.github.com/users/dwalleck/followers","following_url":"https://api.github.com/users/dwalleck/following{/other_user}","gists_url":"https://api.github.com/users/dwalleck/gists{/gist_id}","starred_url":"https://api.github.com/users/dwalleck/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/dwalleck/subscriptions","organizations_url":"https://api.github.com/users/dwalleck/orgs","repos_url":"https://api.github.com/users/dwalleck/repos","events_url":"https://api.github.com/users/dwalleck/events{/privacy}","received_events_url":"https://api.github.com/users/dwalleck/received_events","type":"User","site_admin":false},"committer":{"login":"jidar","id":1134139,"avatar_url":"https://avatars2.githubusercontent.com/u/1134139?v=3","gravatar_id":"","url":"https://api.github.com/users/jidar","html_url":"https://github.com/jidar","followers_url":"https://api.github.com/users/jidar/followers","following_url":"https://api.github.com/users/jidar/following{/other_user}","gists_url":"https://api.github.com/users/jidar/gists{/gist_id}","starred_url":"https://api.github.com/users/jidar/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/jidar/subscriptions","organizations_url":"https://api.github.com/users/jidar/orgs","repos_url":"https://api.github.com/users/jidar/repos","events_url":"https://api.github.com/users/jidar/events{/privacy}","received_events_url":"https://api.github.com/users/jidar/received_events","type":"User","site_admin":false},"parents":[{"sha":"61a61f4dccff320d9d29e2d512d8c17fa11d2d71","url":"https://api.github.com/repos/CafeHub/opencafe/commits/61a61f4dccff320d9d29e2d512d8c17fa11d2d71","html_url":"https://github.com/CafeHub/opencafe/commit/61a61f4dccff320d9d29e2d512d8c17fa11d2d71"}]}]
    -------------------------------------------------------------------------------

That's a little better. We get a verbose log entry for the request made and the
response we received.  The output from the http client is meant to be human
readable and to create an audit trail of what occurred while a test or script
is executed.

Now let's add a few more requests to our script:

.. code-block:: python

    import json
    import logging
    import os
    import sys

    from cafe.engine.http.client import BaseHTTPClient
    from cafe.common.reporting import cclogging

    os.environ['CAFE_ENGINE_CONFIG_FILE_PATH']='.'
    cclogging.init_root_log_handler()
    root_log = logging.getLogger()
    root_log.addHandler(logging.StreamHandler(stream=sys.stderr))
    root_log.setLevel(logging.DEBUG)

    client = BaseHTTPClient()
    response = client.get('https://api.github.com/repos/cafehub/opencafe/commits?per_page=1')
    response = client.get('https://api.github.com/repos/cafehub/opencafe/issues?per_page=1')
    response = client.get('https://api.github.com/repos/cafehub/opencafe/forks?per_page=1')

As we make more requests, a few concerns come to mind. Right now we are
hard-coding the base url (https://api.github.com) in each request. At the very
least, we should factor what is likely to change out of our requests:

.. code:: python

    import json
    import logging
    import os
    import sys

    from cafe.engine.http.client import BaseHTTPClient
    from cafe.common.reporting import cclogging

    os.environ['CAFE_ENGINE_CONFIG_FILE_PATH']='.'
    cclogging.init_root_log_handler()
    root_log = logging.getLogger()
    root_log.addHandler(logging.StreamHandler(stream=sys.stderr))
    root_log.setLevel(logging.DEBUG)

    client = BaseHTTPClient()

    base_url = 'https://api.github.com'
    organization = 'cafehub'
    project = 'opencafe'

    response = client.get(
        '{base_url}/repos/{org}/{project}/commits?per_page=1'.format(
            base_url=base_url, org=organization, project=project))

    response = client.get(
        '{base_url}/repos/{org}/{project}/issues?per_page=1'.format(
            base_url=base_url, org=organization, project=project))

    response = client.get(
        '{base_url}/repos/{org}/{project}/forks?per_page=1'.format(
            base_url=base_url, org=organization, project=project))

The GitHub API is expansive, so we could go on for some time defining more
requests. Rather than defining these in-line, defining these functions in a
common class or module would make more sense.

.. code:: python

    import json
    import logging
    import os
    import sys

    from cafe.engine.clients.base import BaseClient
    from cafe.engine.http.client import BaseHTTPClient
    from cafe.common.reporting import cclogging

    class GitHubClient(BaseClient):

        def __init__(self, base_url):
            self.base_url = base_url
            self.client = BaseHTTPClient()
        
        def get_project_commits(self, org_name, project_name):
            return self.client.get(
                '{base_url}/repos/{org}/{project}/commits?per_page=1'.format(
                    base_url=self.base_url, org=organization, project=project))
        
        def get_project_issues(self, org_name, project_name):
            return self.client.get(
                '{base_url}/repos/{org}/{project}/commits?per_page=1'.format(
                    base_url=self.base_url, org=organization, project=project))
        
        def get_project_forks(self, org_name, project_name):
            return self.client.get(
                '{base_url}/repos/{org}/{project}/commits?per_page=1'.format(
                    base_url=self.base_url, org=organization, project=project))
    
    os.environ['CAFE_ENGINE_CONFIG_FILE_PATH']='.'
    cclogging.init_root_log_handler()
    root_log = logging.getLogger()
    root_log.addHandler(logging.StreamHandler(stream=sys.stderr))
    root_log.setLevel(logging.DEBUG)

    base_url = 'https://api.github.com'
    organization = 'cafehub'
    project = 'opencafe'
    client = GitHubClient(base_url)
    
    resp1 = client.get_project_commits(org_name=organization, project_name=project)
    resp2 = client.get_project_issues(org_name=organization, project_name=project)
    resp3 = client.get_project_forks(org_name=organization, project_name=project) 

Now that our HTTP requests are in better shape, let's talk about dealing with
the responses. The response object has a `json` method that will transform the
body of the response into a Python dictionary. While treating the response content as a dictionary is good enough for
quick scripts and possibly for very stable APIs, it scales poorly
when dealing with large APIs or APIs that are in development.

Accessing the response as a dictionary isn't too difficult when a response body
has one or two properties, but let's jump back to the first response output we
looked at. It has dozens of properties, including ones that are nested. Using
the response as-is requires memorizing the response structure or constantly
referencing API documentation as you code. If you make a mistake, you may not find
that out until you run the script. Also, if/when the name of one of the properties
or the structure of the API response changes, this means tediously changing the property each place it is used or
trying to do a string replace across the project, which can have unitended
consequences unless you're very careful.

Writing Request and Response Models
===================================

An alternate approach is to deserialize the JSON response to an object. This
is the approach that most SDKs and language bindings use. This
greatly simplifies refactoring of response properties and has the added bonus
of error detection by linters if you use an invalid property name. If you're
using a code editor which offers autocomplete functionality, you can also
use that when developing new tests, which removes most of the need to
reference API documentation after you've done the groundwork developing the
response models. Here's an example of what the response model for our first
request would look like:

.. code:: python

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

Any class that inherits from the AutoMarshallingModel class is expected
to implement the _json_to_obj method, _obj_to_json method, or both. This
depends on whether the model is being used to handle requests, responses,
or both.

This example requires quite a bit of boilerplate code. However, because
these objects are explicitly defined, static analysis tools will be able to
assist us going forward. We also wanted to use this simple, explict way for
this demo so it would be easier to understand. In more practical
implementations, you may want to take advantage of Python's dynamic nature to
simplify the setting of properties.


Writing an Auto-Serializing Client
==================================

Now that we have response models, we can refactor our client to use them.

.. code:: python

    class GitHubClient(AutoMarshallingHTTPClient):

    def __init__(self, base_url):
        super(GitHubClient, self).__init__(
            serialize_format='json', deserialize_format='json')
        self.base_url = base_url
        
    def get_project_issue(self, org_name, project_name, issue_id):
            
        url = '{base_url}/repos/{org}/{project}/issues/{issue_id}'.format(
            base_url=self.base_url, org=organization, project=project,
            issue_id=issue_id)
        return self.get(url, response_entity_type=Issue)

There's a few changes to note. The AutoMarshallingHTTPClient class
subclasses the BaseHTTPClient, so there's no longer a need to create a client.
We can also specify what type of content we want this client to serialize to
and from. The response_entity_type parameter defines what type to expect the
response to be. This together with serialization formats set when the client
was instantiated determine which serialization methods are called on the
response contents.

Managing Test Data
==================



Writing and Running a Test
==========================

Now that we have our test client in order, we can write several tests to see
how OpenCafe handles configuration and logging.

.. code:: python

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
