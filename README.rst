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

* `Building a staging environment`_.
* Vendorising the library package.
* Containerising the application.

Building a staging environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``$ docker build -t staging -f pyspike/ops/docker/staging.df pyspike/ops/docker``

.. _devops repository: https://github.com/ONSdigital/pyspike-ops 
