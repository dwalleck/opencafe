.. _repository: https://github.com/CafeHub/opencafe
.. _CI: https://travis-ci.org/CafeHub/opencafe

====================================
Welcome to OpenCAFE's documentation!
====================================

What is OpenCAFE?
=================

The Common Automation Framework Engine (CAFE) is a core set of components used
to develop automated test frameworks. This project began from the need to spin
up dozens of automated test suites. We observed that there were certain
problems that teams had to solve for each project, such as how to best manage
test data, results, and logs. To avoid the need to contionuously re-invent
these solutions and to provide consistency in their solving, OpenCafe was
born.

OpenCafe was designed to be the foundation for building automated test suites.
We do provide some guidance/good practices for developing clients for
interfacing with the application under test, it does not (enforce patterns)/(introduce any contstraints)
for how the tests themselves are designed/developed.

Though OpenCafe does provide its own test runner, the OpenCafe components
can be used with most Python test runners including pytest, nose, behave,
testr, and many others. Inversely, the OpenCafe components and conventions
can also be used as a plugin to other test runners (pytest plugin support
is in an alpha state).

.. note::

    Questions? Join us on Freenode in the #cafehub channel


Relevant Links
================
* GitHub: `Repository`_
* CI: `CI`_
* Coverage: *Coming soon*

Principles
==========

- All test infrastructure should be treated like code. It *is* code and not
  throwaway scripts. Treating tests like scripts can result in brittle tests
  that are costly to maintain.
- Test failures should be easy to triage
- Test logs should be an audit trail of everything that happened during a test run
- It should be easy to switch between the test data/environment being used
  for testing. It should be simple to do this at execution time


Contents
============
.. toctree::
   :maxdepth: 2

   quickstart/index
   installation/index
   cafe/index
   components/index
   plugins/index
   client_dev/index
   test_suite_dev/index
   faq/index
   contributing/index
   appendix/index


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`