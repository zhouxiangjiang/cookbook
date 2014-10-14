#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package design_pattern
Design Pattern - State Machine
    
Copyright (c) 2014 Li Yun <leven.cn@gmail.com>
All Rights Reserved.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
'''

class State(object):
    '''State Interface'''
    def __init__(self):
        self._transfer(InactiveState)
        
    
    def _transfer(state):
        '''Transfer to other state'''
        self.__class__ = state
        
        
    def active(self):
        raise NotImplementedError
        
        
    def inactive(self):
        raise NotImplementedError
        
        
    def action(self):
        raise NotImplementedError
        
        
class InactiveState(State):
    '''Inactive (initial) State'''
    def active(self):
        self._transfer(ActiveState)
        
        
    def inactive(self):
        raise RuntimeWarning('Already inactive')
        
        
    def action(self):
        raise RuntimeError('Not active')
        
        
class ActiveState(State):
    '''Active state'''
    def active(self):
        raise RuntimeWarning('Already active')
        
        
    def inactive(self):
        self._transfer(InactiveState)
        
        
    def action(self):
        print 'Action'
    