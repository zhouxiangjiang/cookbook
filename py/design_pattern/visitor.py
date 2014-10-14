#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''@package design_pattern
Design Pattern - Visitor (Without Recursion)
    
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

import types


class Node(object):
    pass
        
        
class Visitor(object):

    prefix = '_visit_'
    
    def visit(self, node):
        stack = [node]
        result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(result))
                    result = None
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    result = stack.pop()
            except StopIteration:
                stack.pop()
        return result
        
        
    def _visit(self, node):
        method_name = self.__class__.prefix + type(node).__name__
        method = getattr(self, method_name, None)
        if method is None:
            method = self._none_visit
        return method(node)
        
        
    def _none_visit(self, node):
        method_name = self.__class__.prefix + type(node).__name__
        raise RuntimeError('No {0} method'.format(method_name))
        

class Number(Node):
    def __init__(self, value):
        self.value = value

        
class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        

class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand
        

class Add(BinaryOperator):
    pass
    
    
class Negate(UnaryOperator):
    pass
    

class VisitorDemo(Visitor):
    def _visit_Number(self, node):
        return node.value
        
        
    def _visit_Add(self, node):
        yield (yield node.left) + (yield node.right)
        
        
    def _visit_Negate(self, node):
        yield -(yield node.operand)
        
        
if __name__ == '__main__':
    n = Number(0)
    for i in range(1,100000):
        n = Add(n, Number(i))
    
    v = VisitorDemo()
    assert v.visit(n) == 4999950000
    
    
