# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from owlready import *

##Import the ontology from URL
onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl")
onto.load()

##Create a new instance of the class Pizza

#onto.Pizza() ##In this case, the instance will be automatically called pizza_i
#Marguerita = onto.Pizza("Marguerita") ##In this case, the instance will be called "Marguerita"

##Print the instances of the class Pizza
print('Pizzas : ' )
for i in onto.Pizza.instances(): print(i)
print('\n')

##Create a new instance of the class CheeseTopping
#onto.CheeseTopping() ##In this case, the instance will be automatically called cheesetopping_i
#parmesan = onto.CheeseTopping("parmesan") ##In this case, the instance will be called "parmesan"

##Print the instances of the class CheeseTopping
print('Cheese Toppings : ' )
for i in onto.CheeseTopping.instances(): print(i)
print('\n')

##Create a new instance of the class MeatTopping
onto.MeatTopping() ##In this case, the instance will be automatically called meattopping_i
beef = onto.MeatTopping("beef") ##In this case, the instance will be called "beef"

##Print the instances of the class MeatTopping
print('Meat Toppings : ' )
for i in onto.MeatTopping.instances(): print(i)
print('\n')

##Create a new instance of the class FishTopping
onto.FishTopping() ##In this case, the instance will be automatically called fishtopping_i
salmon = onto.FishTopping("salmon") ##In this case, the instance will be called "salmon"

##Print the instances of the class FishTopping
print('Fish Toppings : ' )
for i in onto.FishTopping.instances(): print(i)
print('\n')

##Print the instances of all Toppings
print('Toppings : ' )
for i in onto.Topping.instances(): print(i) ##All the above toppings will be printed as CheeseTopping, MeatTopping and FishTopping are subclasses of the Topping class
print('\n')

##Add toppings to an instance of Pizza (add the property "has topping" to an pizza)
onto.Marguerita.has_topping.append(onto.beef)
onto.Marguerita.has_topping.append(onto.parmesan)

##Print the toppings of an instance of a pizza
print('Toppings on the Marguerita pizza : ')
print(onto.Marguerita.has_topping)
print('\n')


