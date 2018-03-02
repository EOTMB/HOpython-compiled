import ctypes as C
import numpy as np

flp = C.POINTER(C.c_float)
math = C.CDLL('./libhopythoncompiled.so')

intC = math.add_int(3,4)
print "El resultado de la suma de integers es", intC

math.add_float.argtypes = [C.c_float,C.c_float]
math.add_float.restype = C.c_float
floatC = math.add_float(5.0,6.5)
print "El resultado de la suma de floats es",floatC

intpA = C.c_int(6)
intpB = C.c_int(8)
resIntP = C.c_int()
math.add_int_ref(C.byref(intpA),C.byref(intpB),C.byref(resIntP))
print "El resultado de la suma de ints referenciados es", resIntP.value

floatpA = C.c_float(5.0)
floatpB = C.c_float(9.5)
resFloatP = C.c_float()
math.add_float_ref(C.byref(floatpA),C.byref(floatpB),C.byref(resFloatP))
print "El resultado de la suma de floats es" , resFloatP.value

n = C.c_int(3)

arr1 = np.arange(3,dtype=C.c_int)
arr2 = np.flip(arr1,0)
resArr = np.zeros(3)
math.add_int_array(arr1.ctypes.data_as(flp),arr2.ctypes.data_as(flp),resArr.ctypes.data_as(flp),n)
print "El resultado de la suma entre los arrays es", resArr[0],resArr[1],resArr[2]

dotArr1 = np.arange(3,dtype=C.c_float)
dotArr2 = np.flip(dotArr1,0)
resDot = math.dot_product(dotArr1.ctypes.data_as(flp),dotArr2.ctypes.data_as(flp),n)

print "El resultado del producto escalar entre los dos vectores es", resDot
