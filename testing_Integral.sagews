︠5068d164-e74f-428c-9f33-e4092239626f︠
︠516eb11e-cda0-48be-af4b-5d3a9e4450f4s︠
load('newIntegral.py')
var('r a theta phi b')
assume(b>0,a!=0,a>0)
pretty_print_default()
psi2int=newIntegral(r^2*e^(-2*r/a)*sin(theta),(r,0,b),(theta,0,pi),(phi,0,2*pi))
pretty_print((psi2int*1/(pi*a^3)).simplify())
#pretty_print(newIntegral(r^2*e^(-2*r/a)*sin(theta),(r,0,b),(theta,0,pi),(phi,0,2*pi)))

︡4cd49041-af1d-4f72-b411-31c666e62ef4︡︡{"stdout":"(r, a, theta, phi, b)\n","done":false}︡{"html":"<div align='center'>$\\displaystyle \\frac{a^{3} - {\\left(a^{3} + 2 \\, a^{2} b + 2 \\, a b^{2}\\right)} e^{\\left(-\\frac{2 \\, b}{a}\\right)}}{a^{3}}$</div>","done":false}︡{"done":true}








newIntegral(sin(x),x,0,2)
︡9bfdc320-bbdb-44f2-824e-cc587386b35b︡︡{"stdout":"-4*cos(2) + 4\n","done":false}︡{"done":true}
︠627fb129-5e0a-4f6c-bf65-9a25a02ff007s︠

newIntegral(sin(x),x,x)
var('y')
pretty_print(newIntegral(x^2,x,x,y))

︡ed3e4651-cb6f-4f9a-95ee-838621789fb8︡︡{"stdout":"-sin(x)\n","done":false}︡{"stdout":"y\n","done":false}︡{"html":"<div align='center'>$\\displaystyle \\frac{1}{12} \\, x^{4} y$</div>","done":false}︡{"done":true}
︠714b00fe-b775-4ca6-a2d0-44d621a5121e︠


(10^-15/.5*10^-10)^3
︡15381844-8b93-4ed8-8ae8-d96e1b902e6f︡︡{"stdout":"8.00000000000000e-75\n","done":false}︡{"done":true}
︠3e19d24b-2a82-4a34-b272-485d7721113d︠
4*8/3
︡2b16f909-aa0a-4862-b3da-83f072958026︡︡{"stdout":"32/3\n","done":false}︡{"done":true}
︠d70ec077-977b-49b7-8192-280b62f7f8b0︠
hbar
︡4f08c75a-4e6e-4618-a9a3-31bf810c4493︡︡{"done":false,"stderr":"Error in lines 1-1\nTraceback (most recent call last):\n  File \"/projects/sage/sage-6.9/local/lib/python2.7/site-packages/smc_sagews/sage_server.py\", line 905, in execute\n    exec compile(block+'\\n', '', 'single') in namespace, locals\n  File \"\", line 1, in <module>\nNameError: name 'hbar' is not defined\n"}︡{"done":true}
︠fd2d5480-70e9-4b40-9fd3-71231e73d1aa︠









