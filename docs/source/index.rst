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

old
---
The Common Automation Framework Engine (CAFE) is the core engine/driver used
to build an automated testing framework. It is designed to be used as the base
engine for building an automated framework for API and non-UI resource
testing. It is designed to support functional, integration and reliability
testing. The engine is NOT designed to support performance or load testing.

CAFE core provides models, patterns, and supported libraries for building
automated tests. It provides its own lightweight unittest based runner,
however, it is designed to be modular. It can be extended to support most
test case front ends/runners (nose, pytest, lettuce, testr, etc...) through
driver plug-ins.

.. note::

    Questions? Join us on Freenode in the #cafehub channel


Relevant Links
================
* GitHub: `Repository`_
* CI: `CI`_
* Coverage: *Coming soon*


Contents
============
.. toctree::
   :maxdepth: 2

   cafe/index
   installation/index
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