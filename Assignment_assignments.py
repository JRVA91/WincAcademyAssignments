# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
from string import Template
t = Template("Hello, $name!")
def greet(name, template_string=t):
    template_string = t.substitute(name=name)
    return template_string

print(greet('bob'))

#Planets hold gravity as meter per squared second
planets = {
    'sun': 274, 
    'jupiter': 24.9, 
    'neptune': 11.2, 
    'saturn': 10.4, 
    'earth': 9.8, 
    'uranus': 8.9, 
    'venus': 8.9, 
    'mars': 3.7, 
    'mercury': 3.7, 
    'moon': 1.6, 
    'pluto': 0.6
    }
def force(mass, body=planets['earth']):
    return float(mass)*float(body)

print(force(10,planets['saturn']))

def pull(m1,m2,d):
    g = 6.674*(10**-11)
    force = g*((m1*m2)/d**2)
    return force

print(pull(800,1500, 3))
