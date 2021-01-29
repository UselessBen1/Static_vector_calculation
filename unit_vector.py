import math
unit1 = []
unit2 = []
sclar = []
unit_vector = []


maxLengthList = 3
print("enter coordinate x y z continue by enter ")
while len(unit1) < maxLengthList:
    item = float(input("Enter your unit1: "))
    unit1.append(item)
while len(unit2) < maxLengthList:
    item2 = float(input("Enter your unit2: "))
    unit2.append(item2)

i = unit2[0]-unit1[0]
sclar.append(i)
j = unit2[1]-unit1[1]
sclar.append(j)
k = unit2[2]-unit1[2]
sclar.append(k)

dot_product = unit1[0]*unit2[0] + unit1[1]*unit2[1] + unit1[2]+unit2[2]
magnitude = math.sqrt((sclar[0])**2 + (sclar[1])**2 + (sclar[2])**2)

unit_vector.append(sclar[0]/magnitude)
unit_vector.append(sclar[1]/magnitude)
unit_vector.append(sclar[2]/magnitude)

alpha = (math.acos(unit_vector[0]))
beta = (math.acos(unit_vector[1]))
gamma = (math.acos(unit_vector[2]))

alpha_degree = (math.acos(unit_vector[0]))*180/math.pi
beta_degree= (math.acos(unit_vector[1]))*180/math.pi
gamma_degree=(math.acos(unit_vector[2]))*180/math.pi

cross_product_i = (unit1[1]*unit2[2]) - (unit1[2]*unit2[1])
cross_product_j = -((unit1[0]*unit2[2]) - (unit1[2]*unit2[0]))
cross_product_k = (unit1[0]*unit2[1]) - (unit1[1]*unit2[0])

 
print ("\n\n")
print ("sclar= ",sclar)
print ("dot product = ",dot_product)
print ("magnitude= ",magnitude )
print ("unit vector= ", unit_vector)
print ("direction cosine","alpha:",alpha,"beta:",beta,"gamma:",gamma,)
print ("direction cosine in degree: ","alpha:",alpha_degree,"beta:",beta_degree,"gamma:",gamma_degree,)
print ("cross product = ","i",cross_product_i," j",cross_product_j," k",cross_product_k)
print ("equation of line in parametric = (x",-unit1[0],")/",sclar[0],"= (y",-unit1[1],")/",sclar[1],"= (z",-unit1[2],")/",sclar[2] )
