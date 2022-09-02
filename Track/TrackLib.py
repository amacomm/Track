import ctypes
from sys import platform


lib = ctypes.CDLL(r"lib\TrackLib(x64).dll")
if platform != 'win32':
    lib = ctypes.CDLL(r"lib\TrackLib.so")

class Dot(ctypes.Structure):
    '''
    The class characterizes a point on the plane.
    '''
    _fields_ = [('x', ctypes.c_float),
                ('y', ctypes.c_float)]

def Matches_All(t1, t2, eps = 50.0):
    '''
    This function determines the similarity of routes in their direction proximity to each other and total duration.
    '''

    lib.Matches_All.restype = ctypes.c_float
    lib.Matches_All.argtypes = [ctypes.POINTER(Dot), ctypes.c_int,ctypes.POINTER(Dot), ctypes.c_int, ctypes.c_float]

    arr1 = (Dot * len(t1))(*t1)
    arr2 = (Dot * len(t2))(*t2)
    size1 = ctypes.c_int(len(t1))
    size2 = ctypes.c_int(len(t2))
    e= ctypes.c_float(eps)

    return lib.Matches_All(arr1, size1, arr2 , size2, e)

def matches(t1, t2, eps = 50):
    '''
    This function determines the similarity of the first route in relation to the second in its direction and nearness.
    '''
    lib.matches.restype = ctypes.c_float
    lib.matches.argtypes = [ctypes.POINTER(Dot), ctypes.c_int,ctypes.POINTER(Dot), ctypes.c_int, ctypes.c_float]

    arr1 = (Dot * len(t1))(*t1)
    arr2 = (Dot * len(t2))(*t2)
    size1 = ctypes.c_int(len(t1))
    size2 = ctypes.c_int(len(t2))
    e= ctypes.c_float(eps)

    return lib.matches(arr1, size1, arr2 , size2, e)

def length(t):
    '''
    This function determines the length of the route.
    '''
    lib.length.restype = ctypes.c_float
    lib.length.argtypes = [ctypes.POINTER(Dot), ctypes.c_int]

    arr = (Dot * len(t))(*t)
    size = ctypes.c_int(len(t))

    return lib.length(arr, size)

def same_direct(p1, p2, p3, p4):
    '''
    This function indicates that the direction of movement matches.
    '''
    lib.same_direct.restype = ctypes.c_bool
    lib.same_direct.argtypes = [Dot, Dot,Dot,Dot]

    return lib.same_direct(p1, p2, p3, p4)

def TTP(p1, p2, p):
    '''
    This function determines the distance from the point to the segment.
    '''
    lib.TTP.restype = ctypes.c_float
    lib.TTP.argtypes = [Dot, Dot, Dot]

    return lib.TTP(p1, p2, p)

def scalar_product(p1, p2):
    '''
    Function returns the result of the scalar product.
    '''
    lib.scalar_product = ctypes.c_float
    lib.scalar_product = [Dot, Dot]

    return lib.scalar_product(p1, p2)
