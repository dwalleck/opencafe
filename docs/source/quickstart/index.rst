===========
Quick Start
===========

To get started, let's install and initialize OpenCafe. We can do this by
running the following commands:

.. code-block:: bash

    pip install opencafe
    cafe-config init

As an example, lets write a few tests for the GitHub API. Let's assume that we
don't have language bindings or SDKs for our API. We can create a simple
client using the <fill in> class provided by the OpenCafe http plugin, which
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

Next, let's add some assertions to our script:

<code with assertions>

Python's `json` library does a good job of tranforming JSON text into
dictionaries. Accessing the response as a dictionary isn't too difficult
when a response body has one or two properties, but let's jump back to the
first response output we looked at. It has dozens of properties, including
ones that are nested. Using the response as-is requires memorizing the
response structure or constantly referencing documentation as you code. If you
make a mistake, you may not find that out until you run the script. If the
name of one of the properties changes, this means tediously changing the property
each place it is used or trying to do a string replace across the project,
which can have unitended consequences unless you're very careful.

An alternate approach is to deserialize the JSON response to an object. This
greatly simplifies refactoring of response properties and has the added bonus
of error detection by linters if you use an invalid property name. If you're
using a code editor which offers autocomplete functionality, you can also
use that when developing new tests, which removes most of the need to
reference API documentation after you've done the groundwork developing the
response models. Here's an example of what the response model for our first
request would look like:

<response model example>

This requires a bit of boilerplate code. However, because these objects are
explicitly defined, static analysis tools will be able to assist us going
forward. 

<show the not as good shortcut?>
