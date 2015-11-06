︠5068d164-e74f-428c-9f33-e4092239626f︠
︠516eb11e-cda0-48be-af4b-5d3a9e4450f4s︠
load('newIntegral.py')
var('r a theta phi b')
assume(b>0,a!=0,a>0)
pretty_print_default()
psi2int=newIntegral(r^2*e^(-2*r/a)*sin(theta),(r,0,b),(theta,0,pi),(phi,0,2*pi))
pretty_print((psi2int*1/(pi*a^3)).simplify())
#pretty_print(newIntegral(r^2*e^(-2*r/a)*sin(theta),(r,0,b),(theta,0,pi),(phi,0,2*pi)))

︡bbe6892d-dead-410e-8e7e-e2ad0a22000c︡︡{"stdout":"(r, a, theta, phi, b)\n","done":false}︡{"html":"<div align='center'>$\\displaystyle \\frac{a^{3} - {\\left(a^{3} + 2 \\, a^{2} b + 2 \\, a b^{2}\\right)} e^{\\left(-\\frac{2 \\, b}{a}\\right)}}{a^{3}}$</div>","done":false}︡{"done":true}

︡e674c1ac-6422-46de-9cc5-a13b4b518faf︡︡{"done":false,"stderr":"Error in lines 1-1\nTraceback (most recent call last):\n  File \"/projects/sage/sage-6.9/local/lib/python2.7/site-packages/smc_sagews/sage_server.py\", line 905, in execute\n    exec compile(block+'\\n', '', 'single') in namespace, locals\n  File \"\", line 1, in <module>\nTypeError: 'module' object is not callable\n"}︡{"done":true}
︠12b995b3-2815-44ef-9d30-2ae50ebbf02c︠









