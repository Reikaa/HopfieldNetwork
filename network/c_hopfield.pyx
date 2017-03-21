# -*- coding: utf-8 -*-
###########################################
#IMPLEMENTATION OF HOPFIELD NEURAL NETWORK#
###########################################
cimport numpy as cnp
import numpy as np
from tqdm import tqdm


#-----------------------||| Activation functions |||---------------------------------------#

def f1(result, *state):
    return 1 if result > 0 else -1    

def f2(result, *state):
    return 1 if result >= 0 else -1 
    
def f3(result, state):
    return 1 if result > 0 else -1 if result < 0 else state    


#-----------------------||| Hopfield network |||------------------------------------------#

cdef class HopfieldNetwork(object):
    """Hopfield neural network class"""
    
    cdef:
        public list dataset, outputs, f
        public int lng, x_y, epochs
        public object unlearn_rate
        public cnp.ndarray w_matrix
    
    def __cinit__(self, data_to_learn, data_to_present, epochs=1):
        self.dataset = data_to_learn           #data the network is going to learn
        self.outputs = data_to_present
        self.lng = len(data_to_learn[0])              #length of a single matrix 
        self.x_y = int(np.sqrt(self.lng))
        self.epochs = epochs                    #number of presentations
        self.w_matrix = None                  #weights matrices
        self.f = [f1, f2, f3]
        self.unlearn_rate = {"img": 0.0001,"nb": 0.01}
        
        self.init_weights_matrix()
   
#------------------------------------------------------------------------------------------#
    cdef init_weights_matrix(self):
        """weights matrix initialization"""
        cdef:
            cnp.ndarray v

        self.w_matrix = np.zeros((self.lng, self.lng))
        
        for data in self.dataset.copy():
            v = np.array(data).reshape(1, self.lng)
            self.w_matrix += v * v.T
        
        for x in range(self.w_matrix.shape[0]):
            for y in range(self.w_matrix.shape[1]):
                if x == y:
                    self.w_matrix[x][y] = 0
        
        self.w_matrix /= self.lng

#------------------------------------------------------------------------------------------#
    def unlearn_pattern(self, pattern, mode):
        cdef:
            cnp.ndarray v

        v = np.array(pattern).reshape(1, self.lng) 
        self.w_matrix -= (v * v.T) * self.unlearn_rate["{}".format(mode)]

        for x in range(self.w_matrix.shape[0]):
            for y in range(self.w_matrix.shape[1]):
                if x == y:
                    self.w_matrix[x][y] = 0
        
        self.w_matrix /= self.lng

#------------------------------------------------------------------------------------------#
    def synchronous_presentation(self, int epochs, int f_id, bint force_stability):
        """update network in a synchronous way"""
        cdef:
            cnp.ndarray stable, inputs, outputs

        stable = np.zeros(len(self.outputs), dtype=object)
        
        while True:
            for t in range(epochs):
                for i, data in enumerate(self.outputs):
                
                    inputs = np.array(data)
                    outputs = np.dot(inputs, self.w_matrix)
                
                    for j in tqdm(range(len(outputs))):
                        self.outputs[i][j] = self.f[f_id](outputs[j], inputs[j])
                 
                    stable[i] = np.all(np.sign(outputs) == np.sign(inputs))
            
                    print("Item number {} is done!".format(i))
            
            if not np.all(stable) and force_stability:
                continue
            else:
                break


        return stable
   
#------------------------------------------------------------------------------------------#
    def asynchronous_presentation(self, int epochs, int f_id, bint force_stability):
        """update network in an asynchronous way"""
        cdef:
            cnp.ndarray stable, inputs, outputs, randomized

        stable = np.zeros(len(self.outputs), dtype=object)
        
        while True:
            for i, data in enumerate(self.outputs):
                randomized =  np.arange(len(data))
                np.random.shuffle(randomized)

                for idx in tqdm(randomized):
                    inputs = np.array(data)
                    outputs = np.dot(inputs, self.w_matrix)
                    data[idx] = self.f[f_id](outputs[idx], inputs[idx])
                    
                    stable[i] = np.all(np.sign(outputs) == np.sign(inputs))
                    
                print("Item number {} is done!".format(i))
            
            if not np.all(stable) and force_stability:
                continue
            else:
                break

        return stable 
            

