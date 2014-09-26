/*
 * Copyright (c) 2014 Li Yun <leven.cn@gmail.com>
 * All Rights Reserved.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
 * IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

package hello;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import org.junit.After;
import org.junit.Before;
import org.junit.Ignore;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;


/**
 * Tests for {@link Hello}.
 *
 * @author Li Yun <leven.cn@gmail.com>
 * @since JDK 8
 * @since JUnit 4.11
 */
public class HelloTest {
    
    final int intValue = 9;
    String strValue = "9";
    char charValue = '9';
    final int radix = 10;

    @Before
    public void setUp() throws Exception {
    }

    @After
    public void tearDown() throws Exception {
    
    }

    @Test
    public final void thisNotImplemented() {
        fail("Not yet implemented");
    }
	
    @Test
    public void thisAlwaysPasses() {
        
    }
	
    @Test
    @Ignore
    public void thisIsIgnored() {
        
    }
    
    @Rule
    public ExpectedException thrown = ExpectedException.none();
    
    // char => int
    //
    // @see Character.digit(char, int radix)
    @Test
    public final void charToInt() {        
        assertEquals(
                Character.digit(this.charValue, this.radix), this.intValue);
    }
    
    // String => int
    //
    // @see Integer#parseInt(String)
    // @see Integer#parseInt(String, int)
    @Test
    public final void strToInt() {
        
        // normal
        assertEquals(Integer.parseInt(this.strValue), this.intValue);
        
        // exception
        thrown.expect(NumberFormatException.class);
        Integer.parseInt("not number");
        
    }
    
    
    // int => String
    //
    // The method Integer.toString(int) should generally be
    // used in preference to the method String.valueOf(int), as
    // Integer.toString(int) method is likely to yield
    // significantly better time performance by less call hierarchy.
    //
    // @see Integer#toString(int)
    // @see String#valueOf(int)
    @Test
    public final void intToStr() {
        
        // better
        assertEquals(Integer.toString(this.intValue), this.strValue);
        
        // poor
        assertEquals(String.valueOf(this.intValue), this.strValue);
        
    }

}
