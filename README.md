# Sage_Utilities
Collection of things that might improve [sage](http://www.sagemath.org/).  

## newIntegral.py
Supplies two functions:  


sym_or_num_Integral()
 - Written in response to [this](http://ask.sagemath.org/question/30329/symbolic-and-numeric-double-integration-method/) ask.sagemath question
 - Provides an integral function that returns a symbolic solution to an integral if a closed form exists and a numeric solution otherwise
 - Accepts multiple variables of integration and was precursor to newIntegral()  

newIntegral()

 - should provide a solution to trac ticket [#2787](http://trac.sagemath.org/ticket/2787)
 - allows calculation of multiple integral with more natural syntax of integral(x^2,(x,2)) or integral(x^2,x,y,y)
