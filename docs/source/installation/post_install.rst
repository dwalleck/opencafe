==================
Post Install Steps
==================

After the OpenCafe package is installed, it needs to be initialized. This
is done using the `cafe-config init` command.

.. code-block:: bash

    (cafe-env) Daryls-MacBook-Pro:projects dwalleck$ cafe-config init
    =================================
    * Initializing Engine Install
    * Creating default directories in /Users/dwalleck/projects/cafe-env/bin/../.opencafe
    * ...created /Users/dwalleck/projects/cafe-env/bin/../.opencafe
    * ...created /Users/dwalleck/projects/cafe-env/bin/../.opencafe/data
    * ...created /Users/dwalleck/projects/cafe-env/bin/../.opencafe/configs
    * ...created /Users/dwalleck/projects/cafe-env/bin/../.opencafe/logs
    * ...created /Users/dwalleck/projects/cafe-env/bin/../.opencafe/temp
    * Creating default engine.config at /Users/dwalleck/projects/cafe-env/bin/../.opencafe/engine.config
    =================================

Executing this command will create the `.opencafe` directory structure, which
will help us manage our test data and logs. This directory is created in the
home directory for the current user. When this command is run inside a virtual
environment, the directory will be created in the root directory of that
environment.

.. code-block:: bash

    (cafe-env) Daryls-MacBook-Pro:.opencafe dwalleck$ ls -la
    total 8
    drwxr-xr-x  7 dwalleck  staff  238 Mar 17 13:38 .
    drwxr-xr-x  8 dwalleck  staff  272 Mar 17 13:38 ..
    drwxr-xr-x  2 dwalleck  staff   68 Mar 17 13:38 configs
    drwxr-xr-x  2 dwalleck  staff   68 Mar 17 13:38 data
    -rw-r--r--  1 dwalleck  staff  410 Mar 17 13:38 engine.config
    drwxr-xr-x  2 dwalleck  staff   68 Mar 17 13:38 logs
    drwxr-xr-x  2 dwalleck  staff   68 Mar 17 13:38 temp



What directories and files were created and where?
What do the entries in the engine.config mean?
What is the convention used for configuration/data/logging?



You cannot change the location of engine.config, but you can change the
location of the other directories

[OPENCAFE_ENGINE]
config_directory = /Users/dwalleck/projects/cafe-env/bin/../.opencafe/configs
data_directory = /Users/dwalleck/projects/cafe-env/bin/../.opencafe/data
log_directory = /Users/dwalleck/projects/cafe-env/bin/../.opencafe/logs
temp_directory = /Users/dwalleck/projects/cafe-env/bin/../.opencafe/temp
master_log_file_name = cafe.master
logging_verbosity = STANDARD
default_test_repo = cloudroast
