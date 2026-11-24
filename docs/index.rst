my-arithmetic-ethantakahashi
============================

Bibliothèque Python d'arithmétique réalisée dans le cadre du TP
*Mise en place d'un pipeline CI/CD* (Master 1 informatique, La Rochelle Université).

Elle fournit le calcul du plus grand commun diviseur (PGCD) de deux entiers
avec l'algorithme d'Euclide.

Installation
------------

.. code-block:: console

   $ pip install my-arithmetic-ethantakahashi

Exemple
-------

.. code-block:: python

   >>> from my_arithmetic_ethantakahashi.arithmetic import pgcd
   >>> pgcd(12, 18)
   6

.. toctree::
   :maxdepth: 2
   :caption: Sommaire

   api