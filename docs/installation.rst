
Dependencies
*************

**Python3** via one of the following:

   -  Python 3.4.X+
   -  Python 3.5.X+
   -  Python 3.6.X+

    Other versions of python3 < 3.4 may work, but have not been tested.
    `Python 3 <http://www.python.org>`__ *is a minimum requirement*.


**Linux Operating System**, one of the following:

   -  Redhat Enterprise Linux v7.X
   -  Ubuntu 14.04, Ubuntu 16.04, and corresponding Ubuntu variants
   -  Amazon Linux (2016.03+ )

**Windows Operating System**:

   -  Windows 7
   -  Windows 8 (not tested)
   -  Windows 10

**Installation via Source**

    - `GNU make <https://www.gnu.org/software/make>`__ v4+ binary installed
    - `Python3 <https://www.python.org>`__ v3.4+
    - `Python Package Manager (pip) <https://packaging.python.org/tutorials/installing-packages/>`__
    - `bash v4+ <https://www.gnu.org/software/bash/>`__ v4+

--------------

.. _install:

Installation
*************

Choose your operating system for correct installation instructions:

**Linux Distributions**

   - :ref:`redhat`
   - :ref:`ubuntu`
   - :ref:`amazonlinux`

**Windows Distributions**

   - :ref:`windows7`
   - :ref:`windows10`

**Installation via Source**

    - :ref:`source`

**Post-Installation**

    - :ref:`verify`

**Note**:

    | Generally, any modern Linux distribution may work.
    | `Python 3 <http://www.python.org>`_ *as a minimum requirement*.

------------

.. _redhat:

Redhat Enterprise Linux v7.X / Centos 7.X
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Install Python3 Package Manager

.. code:: bash

        $ sudo yum install python3-pip

-  Install `awscli <https://github.com/aws/aws-cli/>`__

   Detailed instructions can be found in the README located at:
   https://github.com/aws/aws-cli/

   The easiest method, provided your platform supports it, is via
   `pip <http://www.pip-installer.org/en/latest>`__.

.. code:: bash

        $ sudo pip3 install awscli

-  If you have the aws-cli installed and want to upgrade to the latest
   version you can run:

.. code:: bash

        $ sudo pip3 install --upgrade awscli

-  Installation via pip3 (python3 packages via pip package manager)

.. code:: bash

        $ sudo -H pip3 install gitsane

-  :ref:`verify`

Back to :ref:`install` Table of Contents

------------------

.. _ubuntu:

Ubuntu v16.04+, Ubuntu Variants
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Install Python3 Package Manager

.. code:: bash

        $ sudo apt-get install python3-pip

-  Install `awscli <https://github.com/aws/aws-cli/>`__

   Detailed instructions can be found in the README located at:
   https://github.com/aws/aws-cli/

   The easiest method, provided your platform supports it, is via
   `pip <http://www.pip-installer.org/en/latest>`__.

.. code:: bash

        $ sudo pip3 install awscli

-  If you have the aws-cli installed and want to upgrade to the latest
   version you can run:

.. code:: bash

        $ sudo pip3 install --upgrade awscli

-  Installation via pip3 (python3 packages via pip package manager)

.. code:: bash

        $ sudo -H pip3 install gitsane

-  :ref:`verify`

Back to :ref:`install` Table of Contents

------------------

.. _amazonlinux:

Amazon Linux v2016+
~~~~~~~~~~~~~~~~~~~~~

-  Install Python3 Package Manager:

.. code:: bash

        $ sudo yum install python36-pip

        OR

        $ sudo yum install python35-pip / python34-pip    # latest your distribution supports

-  Install gitsane:

.. code:: bash

        $ sudo -H pip3 install gitsane

-  :ref:`verify`

Back to :ref:`install` Table of Contents

------------------

.. _windows7:

Microsoft Windows 7
~~~~~~~~~~~~~~~~~~~~~

-  Install Python3 by downloading the latest `Python3 version for Windows <https://www.python.org/downloads/windows/>`__

- Install gitsane:

.. code:: powershell

    $ pip3 install gitsane

-  :ref:`verify`

Back to :ref:`install` Table of Contents

------------------

.. _windows10:

Microsoft Windows 10
~~~~~~~~~~~~~~~~~~~~~

-  Install Python3 by downloading the latest `Python3 version for Windows <https://www.python.org/downloads/windows/>`__

- Install gitsane:

.. code:: powershell

    $ pip3 install gitsane

-  :ref:`verify`

Back to :ref:`install` Table of Contents

--------------

.. _source:

Build Source Code
~~~~~~~~~~~~~~~~~~~~

To install locally from source code, do the following:

Check out the ``gitsane`` code repository:

.. code:: bash

    $ git clone https://blakeca00@bitbucket.org/blakeca00/gitsane.git

    $ cd gitsane/

Display the list of make targets:

.. code:: bash

    $ make help

.. figure:: ../assets/make-help.png

To install locally in virtual environment, make the install from source target:

.. code:: bash

    $ make source-install

-  :ref:`verify`

--------------


Post-Installation
*****************

.. _verify:

Verify Your Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ gitsane --version


.. figure:: ../assets/gitsane-version.png

Back to :ref:`install` Table of Contents

--------------

( `Table Of Contents <./index.html>`__ )

-----------------

|
