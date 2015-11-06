from sage.all import *
from sage.symbolic import *
def sym_or_num_Integral(f,variables,lower_bound=[None],upper_bound=[None],algorithm='maxima'):
    '''
    needs to check if bounds are list or not
    returns analytic solution if found - otherwise numeric solution
    also allows multiple integreals
    '''
    if isinstance(variables,list):
        if not isinstance(lower_bound,list):
            lower_bound=[lower_bound]
        while len(lower_bound)!=len(variables):
            if len(lower_bound)>len(variables): break
            lower_bound.append(None)
        if not isinstance(upper_bound,list):
            upper_bound=[upper_bound]
        while len(upper_bound) != len(variables):
            if len(lower_bound)>len(variables): break
            upper_bound.append(None)
        if len(variables)==1:
            return sym_or_num_Integral(f,variables[0],lower_bound,upper_bound)
        var_list=[variables[1:],lower_bound[1:],upper_bound[1:],algorithm]
        return sym_or_num_Integral(sym_or_num_Integral(f,variables[0],lower_bound,upper_bound,algorithm),*var_list)
    #Base Case
    result=integral(f,variables,lower_bound[0],upper_bound[0])
    #Check if there was a closed form solution
    if 'integrate' in str(result):
        return result.n()
    else:
        return result
def is_symbol(x):
    '''
    naive check if something is a symboll - i believe there there is a better one using ginacs but confusing on how to access- can find usage in Expression.derivative
    '''
    if isinstance(x,list) or isinstance(x,tuple):
        for i in x:
            return is_symbol(i)
    elif isinstance(x,Expression):
        if len(x.variables())==1 and x.variables()[0]==x:
            return True
    else:
        return False
    
def _newIntegral(f,variables,lower_bound=[None],upper_bound=[None],algorithm='maxima'):
    '''
    needs to check if bounds are list or not
    actually does integral after newIntegral processes input
    '''
    if isinstance(variables,list):
        if not isinstance(lower_bound,list):
            lower_bound=[lower_bound]
        while len(lower_bound)!=len(variables):
            if len(lower_bound)>len(variables): break
            lower_bound.append(None)
        if not isinstance(upper_bound,list):
            upper_bound=[upper_bound]
        while len(upper_bound) != len(variables):
            if len(lower_bound)>len(variables): break
            upper_bound.append(None)
        if len(variables)==1:
            return _newIntegral(f,variables[0],lower_bound,upper_bound)
        var_list=[variables[1:],lower_bound[1:],upper_bound[1:],algorithm]
        return _newIntegral(_newIntegral(f,variables[0],lower_bound,upper_bound,algorithm),*var_list)
    #Base Case
    return integral(f,variables,lower_bound[0],upper_bound[0])
def newIntegral(f,*args,**kwargs):
    '''
Integration wrt multiple variables newIntegral(f(x,y),x,y)
    or newIntegral(f(x,y),(x,0,2),y)
    or newIntegral(f(x,y),(x,0,2),y(1,5))
    this should work for any number of variables to integrate over
    Keeps the functionality of the old integral: newIntegral(f,x,0,2)=integral(f,x,0,2)
    uses _newIntegral to actual recurse over input after input was processed.
    '''
    variables=[]
    lower_bound=[]
    upper_bound=[]
    def extract_from_tuple(args,variables,lower_bound,upper_bound):
        if len(args)==3:
            lower_bound.append(args[1])
            upper_bound.append(args[2])
        elif len(args)==2:
            lower_bound.append(args[1])
            upper_bound.append(None)
        elif len(args)==1:
            lower_bound.append(None)
            upper_bound.append(None)
        else:
            print "Incorrectly Sized Tuple"
        variables.append(args[0])
        return variables,lower_bound,upper_bound

    for i in args:
        if len(args)==3 and not is_symbol(args[1]) and not is_symbol(args[2]):
            variables.append(args[0])
            lower_bound.append(args[1])
            upper_bound.append(args[2])
        elif len(args)==2 and not is_symbol(args[1]):
            variables.append(args[0])
            lower_bound.append(args[1])
            upper_bound.append(None)
        elif isinstance(i,list) or isinstance(i,tuple):
            variables,lower_bound,upper_bound=extract_from_tuple(i,variables,lower_bound,upper_bound)
        elif is_symbol(i):
            variables.append(i)
            lower_bound.append(None)
            upper_bound.append(None)
        else:
            print "ambiguous input"
            return
    return _newIntegral(f,variables,lower_bound,upper_bound,kwargs)
def test_newIntegral():
    var('y z x c')
    assume(y>0)
    pretty_print(newIntegral(sin(x),x,pi,2*pi))
    pretty_print(newIntegral(sin(x)*y,(x,0,2),(y,0,2)))
    pretty_print(newIntegral(sin(x)*y,x,y))
    pretty_print(newIntegral(sin(x),(x,0,y)))
    pretty_print(newIntegral(y*z*x*c,(y,x,z),c))
    pretty_print(newIntegral(sin(x), x))
    pretty_print(newIntegral(sin(x),x*y))
