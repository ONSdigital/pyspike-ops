..  Titling
    ##++::==~~--''``
    
PySpike
:::::::

A Proof-of-Concept for container deployment of Python 3 apps.

PySpike consists of three separate git repositories:

* A library repository
* An application repository
* A `devops repository`_

pyspike-ops
===========

This is the devops repository. It is a package for:

* `Configuring a staging environment`_.
* `Containerising the application`_.

Initial steps
~~~~~~~~~~~~~

Check out the repository and make it your working directory::

    $ git clone https://github.com/ONSdigital/pyspike-ops.git
    $ cd pyspike-ops

Configuring a staging environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``$ docker build -t pyspike-staging -f pyspike/ops/docker/staging.df pyspike/ops/docker``

Containerising the application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``$ docker run --rm --tty pyspike-staging``

.. _devops repository: https://github.com/ONSdigital/pyspike-ops 
