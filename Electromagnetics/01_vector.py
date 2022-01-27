from math import *
import numpy as np
# scalar
a = 10
print("a = {0}".format(a))

# vector
va = np.array([10, 20, 30])        # Cartesian Coordinate System
print("Vector a = {0:+} ax {1:+} ay {2:+} az".format(va[0], va[1], va[2]))
amp_va = sqrt(va[0]**2 + va[1]**2 + va[2]**2)
unit_va = va / amp_va
print("Amplitude of vector a = {0:+}".format(amp_va))
print("Unit vector of vector a = {0:+} ax {1:+} ay {2:+} az".format(unit_va[0], unit_va[1], unit_va[2]))
# Vector Algebra
vb = np.array([-15, 30, -10])
# Vector Addition
v_add = va + vb
print("a + b = {0:+} ax {1:+} ay {2:+} az".format(v_add[0], v_add[1], v_add[2]))
# Vector Subtraction
v_sub = va - vb
print("a - b = {0:+} ax {1:+} ay {2:+} az".format(v_sub[0], v_sub[1], v_sub[2]))
# Vector Multiplication of vector and scalar
# scalar
v_mul_scalar = a * va
print("a * vector a = {0:+} ax {1:+} ay {2:+} az".format(v_mul_scalar[0], v_mul_scalar[1], v_mul_scalar[2]))
# vector (dot product)
# v_dot_vector = np.sum(va * vb)    # Using definition
v_dot_vector = np.dot(va, vb)       # Using function "dot"
print("vector a dot vector b = {0:+}".format(v_dot_vector))
# vector (cross product)
v_mul_vector_ab = np.cross(va, vb)       # Using function "dot"
print("vector a cross vector b = {0:+} ax {0:+} ay {0:+} az".format(v_mul_vector_ab[0], v_mul_vector_ab[1], v_mul_vector_ab[2]))

v_mul_vector_ba = np.cross(vb, va)       # Using function "dot"
print("vector b cross vector a = {0:+} ax {0:+} ay {0:+} az".format(v_mul_vector_ba[0], v_mul_vector_ba[1], v_mul_vector_ba[2]))

# vector position
# origin vector
o = np.array([0, 0, 0])
# vector oa
oa = va - o
print("Vector oa = {0:+} ax {1:+} ay {2:+} az".format(oa[0], oa[1], oa[2]))
# vector ob
ob = vb - o
print("Vector ob = {0:+} ax {1:+} ay {2:+} az".format(ob[0], ob[1], ob[2]))
# vector ab
ab = vb - va
print("Vector ab = {0:+} ax {1:+} ay {2:+} az".format(ab[0], ab[1], ab[2]))

# Orthogonal Coordinate System

# Cartesian
# (x, y, z)

# Cylindrical
# (rho, phi, z)
# rho = sqrt(x^2 + y^2)
# phi = atan(y/x)
# z = z

# Spherical
# (r, theta, phi)
# r = sqrt(x^2 + y^2 + z^2)
# theta = acos(z/r)
# phi = atan(y/x)

# Cylindrical -> Cartesian
# x = rho * cos(phi)
# y = rho * sin(phi)
# z = z

# Spherical -> Cartesian
# x = r * sin(theta) * cos(phi)
# y = r * sin(theta) * sin(phi)
# z = r * cos(theta)

cartesian = np.array([1, 2, 3])
x = cartesian[0]
y = cartesian[1]
z = cartesian[2]

cylindrical = np.array([sqrt(x**2 + y**2), atan(y/x), z])
rho = cylindrical[0]
phi = cylindrical[1]

r = sqrt(x**2 + y**2 + z**2)
zr = z / r
theta = acos(zr)
spherical = np.array([r, theta, phi])

print("Cartesian Coordinates : {}".format(cartesian))
print("Cylindrical Coordinates : {}".format(cylindrical))
print("Spherical Coordinates : {}".format(spherical))

xc = cylindrical[0] * cos(cylindrical[1])
yc = cylindrical[0] * sin(cylindrical[1])
zc = cylindrical[2]
cylindrical_cartesian = np.array([xc, yc, zc])
print("Cylindrical to Cartesian : {}".format(cylindrical_cartesian))

xs = spherical[0] * sin(spherical[1]) * cos(spherical[2])
ys = spherical[0] * sin(spherical[1]) * sin(spherical[2])
zs = spherical[0] * cos(spherical[1])
spherical_cartesian = np.array([xs, ys, zs])
print("Spherical to Cartesian : {}".format(spherical_cartesian))
