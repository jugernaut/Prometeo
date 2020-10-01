#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 17:35:09 2020

@author: luiggi
"""
import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
#plt.style.use('seaborn')


class planoCartesiano():
    
    def __init__(self, rows = 1, cols = 1, par = None, par_fig={'figsize':(10,5)}, title=''):
        """
        Crea e inicializa una figura de matplotlib.

        Parameters
        ----------
        rows : int, opcional
            Número de renglones del arreglo de subplots. The default is 1.
        cols : int, opcional
            Número de columnas del arreglo de subplots. The default is 1.
        par : list of dicts, opcional
            Lista de diccionarios; cada diccionario define los parámetros que 
            se usarán decorar los `Axes` de cada subplot. The default is None.
        par_fig : dict, opcional
            Diccionario con los parámetros para decorar la figura. 
            The default is {}.

        """
        self.__fig = plt.figure(**par_fig)
        self.__fig.suptitle(title, fontweight='light', fontsize='12', color='blue')
        self.__nfigs =  rows *  cols

        if par != None:
            Nfill = self.__nfigs - len(par)
        else:
            Nfill = self.__nfigs
            par = [ ]
            
        [par.append({}) for n in range(Nfill)]
            
        self.__ax = [plt.subplot(rows, cols, n, **par[n-1]) for n in range(1,self.__nfigs + 1)]
        plt.tight_layout()


    def plot(self, n = 1, x = None, y = None, par=None):        
        assert (n >= 1 and n <= self.__nfigs), \
        "Plotter.plot(%d) out of bounds. Valid bounds : [1,%d]" % (n,self.__nfigs)        

        if par != None:
            out = self.__ax[n-1].plot(x, y, **par)
        else:
            out = self.__ax[n-1].plot(x, y)
                    
        return out        
 
    def scatter(self, n = 1, x = None, y = None, par=None):   
        
        assert (n >= 1 and n <= self.__nfigs), \
        "Plotter.plot(%d) out of bounds. Valid bounds : [1,%d]" % (n,self.__nfigs)        

        if par != None:
            out = self.__ax[n-1].scatter(x, y, **par)
        else:
            out = self.__ax[n-1].scatter(x, y)         
        return out      

    def bar(self, n = 1, x = None, y = None, par=None):        
        assert (n >= 1 and n <= self.__nfigs), \
        "Plotter.plot(%d) out of bounds. Valid bounds : [1,%d]" % (n,self.__nfigs)        

        if par != None:
            out = self.__ax[n-1].bar(x, y, **par)
        else:
            out = self.__ax[n-1].bar(x, y)
                    
        return out     

    def format_func(value, tick_number):
        # find number of multiples of pi/2
        N = int(np.round(2 * value / np.pi))
        if N == 0:
            return "0"
        elif N == 1:
            return r"$\pi/2$"
        elif N == 2:
            return r"$\pi$"
        elif N % 2 > 0:
            return r"${0}\pi/2$".format(N)
        else:
            return r"${0}\pi$".format(N // 2)

    def ticks(self, n = 1, xticks = [], yticks = [], trig = False):           
        assert (n >= 1 and n <= self.__nfigs), \
        "Plotter.plot(%d) out of bounds. Valid bounds : [1,%d]" % (n,self.__nfigs)        

        if trig:
            self.__ax[n-1].xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
            self.__ax[n-1].xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 4))
            self.__ax[n-1].xaxis.set_major_formatter(plt.FuncFormatter(planoCartesiano.format_func))
        else:        
            if len(xticks) != 0:
                self.__ax[n-1].set_xticks(xticks)
            if len(yticks) != 0:
                self.__ax[n-1].set_yticks(yticks)

    def label_ticks(self, n = 1, xlabel = [], ylabel = []):
        assert (n >= 1 and n <= self.__nfigs), \
        "Plotter.plot(%d) out of bounds. Valid bounds : [1,%d]" % (n,self.__nfigs)   
        
        if len(xlabel):
            self.__ax[n-1].set_xticklabels(xlabel)
        if len(ylabel):
            self.__ax[n-1].set_yticklabels(ylabel)
            
    def limits(self, n = 1, x = (), y = ()):
        assert (n >= 1 and n <= self.__nfigs), \
        "Plotter.plot(%d) out of bounds. Valid bounds : [1,%d]" % (n,self.__nfigs)

        if len(x):
            offset = np.fabs(x[1] - x[0]) * 0.2
            self.__ax[n-1].set_xlim((x[0]-offset,x[1]+offset))
        if len(y):
            offset = np.fabs(y[1] - y[0]) * 0.2
            self.__ax[n-1].set_ylim((y[0]-offset,y[1]+offset))

    def colorbar(self, n=1, m=None, par=None):
        assert (n >= 1 and n <= self.__nfigs), \
        "Plotter.plot(%d) out of bounds. Valid bounds : [1,%d]" % (n,self.__nfigs)

        if par != None:
            self.__fig.colorbar(m, ax = self.__ax[n-1], **par)
        else:
            self.__fig.colorbar(m, ax = self.__ax[n-1])

    def legend(self, par=None):
        """
        Muestra las leyendas de todos los subplots, si están definidos.

        Parameters
        ----------
        par : dict, opcional
            Diccionario con los parámetros para decorar las leyendas. 
            The default is None.

        Returns
        -------
        None.
        
        See Also
        --------
        matplotlib.axes.Axes.legend().

        """
        if par != None:   
            [self.__ax[n].legend(**par) for n in range(0,self.__nfigs)]        
        else:
            [self.__ax[n].legend() for n in range(0,self.__nfigs)]    
            

    def show(self):
        """
        Muestra las gráficas de cada subplot.
        
        See Also
        --------
        matplotlib.pyplot.show().
        
        """
        plt.show()
        
    def annotate(self, n = 1, par=None):   
        
        assert (n >= 1 and n <= self.__nfigs), \
        "Plotter.plot(%d) out of bounds. Valid bounds : [1,%d]" % (n,self.__nfigs)        

        return self.__ax[n-1].annotate(**par)


def RMS(ua, u):
    """
    Calcula el error cuadrático medio entre u y ua.
    
    Parameters
    ----------
    ua: np.array
    Arreglo de valores aproximados.
    
    u: np.array
    Arreglo de valores exactos.
    
    Returns
    -------
    float
    El error cuadrático medio entre u y ua.
    """
    return np.sqrt(np.sum((ua - u)**2) / len(ua))
        
#----------------------- TEST OF THE MODULE ----------------------------------   
if __name__ == '__main__':

    axis_par1 = [{'title':'1', 'xlabel':'x', 'ylabel':'y'},
                {'title':'Ejemplo 1', 'xlabel':'$x$', 'ylabel':'sin($x$)'},
                {'title':'3', 'xlabel':'n'}]
    vis1 = planoCartesiano(2, 2, axis_par1, title='Testing: plot() & scatter()')
    
    semanas   = [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10]
    porciones = [ 4, 9,18,30,43,52,57,59,60,60]

    vis1.plot(1, semanas, porciones)
    vis1.ticks(1, xticks=semanas)
    
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y = np.sin(x)
    vis1.ticks(2, trig = True) 
    vis1.plot(2, x, y)
    
    par_f ={'figsize':(5,5)}
    par = [{'title':'Negocio de chilaquiles', 
            'xlabel':'Semanas',
            'ylabel':'Porciones vendidas'}]

    vis2 = planoCartesiano(par=par, par_fig=par_f)
    vis2.plot(x = semanas, y = porciones)
    vis2.scatter(x = semanas, y = porciones)
    vis2.ticks(xticks = semanas)
    vis2.show()




