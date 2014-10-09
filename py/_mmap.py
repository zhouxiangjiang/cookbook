#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''@package py
Memory Mapped Cookbook.


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
    
def test_mmap(filename):
    '''Memory-mapped I/O.
    
    It should be emphasized that memory mapping a file does not cause the
    entire file to be read into memory. That is, it’s not copied into some kind
    of memory buffer or array. Instead, the operating system merely reserves a
    section of virtual memory for the file contents. As you access different
    regions, those portions of the file will be read and mapped into the memory
    region as needed. However, parts of the file that are never accessed simply
    stay on disk. This all happens transparently, behind the scenes.
    
    If more than one Python interpreter memory maps the same file, the
    resulting mmap object can be used to exchange data between interpreters.
    That is, all interpreters can read/write data simultaneously, and changes
    made to the data in one interpreter will automatically appear in the
    others. Obviously, some extra care is required to synchronize things, but
    this kind of approach is sometimes used as an alternative to transmitting
    data in messages over pipes or sockets.
    
    Usage:
    
        >>> test_mmap('_file.data')
        b'Hello World'
        
    '''
    import mmap
    import os
    
    # Initially create a binary file and expand it to a desired size.
    size = 10000 # 10K
    try:
        with open(filename, 'wb') as f:
            f.seek(size-1)
            f.write(b'\x00')
    except IOError as e:
        print('error')
    assert os.path.getsize(filename) == size
    
    # Memory map a file
    try:
        with open(filename, 'r+b') as f:
            # Note: If you want to create a memory-mapping for a writable,
            # buffered file, you should flush() the file first. This is
            # necessary to ensure that local modifications to the buffers are
            # actually available to the mapping.
            f.flush()
            
            m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
            assert len(m) == size
            assert m[0:10] == b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            
            # Modify in place
            m[0:11] = b'Hello World'
            m.close()
    except IOError as e:
        print('error')
    
    # Verify the modifications
    try:
        with open(filename, 'rb') as f:
            print(f.read(11))
    except IOError as e:
        print('error')
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
