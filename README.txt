zps - A zope processes inspector
================================

**zps** is addressed to the manager of zope and plone sites that want to get quickly
get informations about the running instances of zope.

Installation
------------
::

    easy_install psutil
    easy_install rt.zps


Usage
-----

**zps** basic usage is straightforward: ::

    [user@localhost]$zps
    CWD:      /home/user/plone1
    User:     user
    PID:      1234
    Conf:     /home/user/plone1/parts/instance/etc/zope.conf
    Address:  8081
    Memory:   1.96%

    CWD:      /home/user/plone2
    User:     user
    PID:      12345
    Conf:     /home/user/plone2/parts/instance/etc/zope.conf
    Address:  8082
    Memory:   1.96%

The default action is to report, for each running instance of zope that it founds:
* the Current Working Directory (CWD)
* the id of the user who is running the process
* the process PID
* the zope configuration file used by the instance
* the port (as calculated parsing the configuration file)
* the memory usage

To obtain usage information for **zps** just type zps --help, you will get this::

    [user@localhost]$zps
    zps - report a snapshot of the current zope processes.

    USAGE:
     zps
     zps --help
     zps --pid 1111
     zps --port 8080

As you can see **zps** can filter the results per **zps** or port, e.g., if calling **zps**
returns the report about the two instances above, you will have the following::

    [user@localhost]$zps --pid 1234
    CWD:      /home/user/plone1
    User:     user
    PID:      1234
    Conf:     /home/user/plone1/parts/instance/etc/zope.conf
    Address:  8081
    Memory:   1.96%

    [user@localhost]$zps --port 8082
    CWD:      /home/user/plone2
    User:     user
    PID:      12345
    Conf:     /home/user/plone2/parts/instance/etc/zope.conf
    Address:  8082
    Memory:   1.96%

In the case no instance is found, you will have::

    [user@localhost]$zps
    No running zope instance found

**TODO**: filter output information
It may happen that your server starts to be crowded. In that case the output of 
**zps** is quickly parsable.
Two command line flags should then be introduced:

* --show
* --hide

**TODO**: colorize output
It would be a nice feature to highlight with colors the memory usage. 
If the output is in the range:

* 0%-5%: green
* 0%-10%: yellow
* 10%-20%: red
* 20%-100%: blinking red

**Examples**: ::

    [user@localhost]$zps --hide CWD,User,Memory
    PID:      1234
    Conf:     /home/user/plone1/parts/instance/etc/zope.conf
    Address:  8081

    PID:      12345
    Conf:     /home/user/plone2/parts/instance/etc/zope.conf
    Address:  8082

    [user@localhost]$zps --hide CWD,User,Memory
    CWD:      /home/user/plone1
    User:     user
    Memory:   1.96%

    CWD:      /home/user/plone2
    User:     user
    Memory:   1.96%