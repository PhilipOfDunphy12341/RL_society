dry_weight = 50*9.81
max_v_drouge = 50
max_v_main = 25
landing_v = 8
max_tension = 340 # kg
max_strain = 0.3
natural_length_main = 1.5
natural_length_drouge = 2
air_density = 1.225 #kg/m^3
area_drouge = 0.6567
area_main=7.2966
spring_constant = 7412

def Drag(d,u,area,c):
    drag = (1/2.0)*d*(u**2)*area*c
    print (str(drag) + " N")
    print ("Acceleration is "+  str(drag/dry_weight))
    return drag
#drouge drag
Drag(air_density,max_v_drouge,area_drouge,2.2)
#drouge @25
Drag(air_density,max_v_main,area_drouge,2.2)
#main drag
Drag(air_density,max_v_main,area_main,2.2)
#main langing
Drag(air_density,landing_v,area_main,2.2)

def inverse_drag(d, c, a):
    velocity = (dry_weight/((1/2.0)*d*c*a))**(1/2.0)
    print velocity
    return velocity

inverse_drag(air_density, 2.2, area_main)

def tension(
