import numpy as np

def mystery1D1o(x):
    f = 4.12*(x-13.5)**2;df = 8.24*(x-13.5);ddf = 8.24
    return f

def mystery1D2o(x):
    f = 4.12*(x-13.5)**2;df = 8.24*(x-13.5);ddf = 8.24
    return f,df

def mystery2D1o(x):
    f = (x[0]+14.45)**2 + (x[1]-30.5)**2
    df = np.array([2*(x[0]+14.45),2*(x[1]-30.5)])
    dff = np.array([[2,0],[0,2]])
    return f

def mystery2D2o(x):
    f = (x[0]+14.45)**2 + (x[1]-30.5)**2
    df = np.array([2*(x[0]+14.45),2*(x[1]-30.5)])
    dff = np.array([[2,0],[0,2]])
    return f,df

def mystery2D3o(x):
    f = (x[0]+14.45)**2 + (x[1]-30.5)**2
    df = np.array([2*(x[0]+14.45),2*(x[1]-30.5)])
    dff = np.array([[2,0],[0,2]])
    return f,df,ddf
