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

/**
 * Own {@code Character}.
 * 
 * @author Li Yun <leven.cn@gmail.com>
 * @see Character
 * @since JDK 8
 */
@HelloClass
public class MyCharacter {
    
    /**
     * The minimum radix available for conversion to and from strings.
     * The constant value of this field is the smallest value permitted
     * for the radix argument in radix-conversion methods such as the
     * {@code digit} method, the {@code forDigit} method, and the
     * {@code toString} method of class {@code Integer}.
     *
     * @see Character#digit(char, int)
     * @see Character#forDigit(int, int)
     * @see Integer#toString(int, int)
     * @see Integer#valueOf(String)
     */
    @HelloField
    public static final int MIN_RADIX = 2;
    
    /**
     * The maximum radix available for conversion to and from strings.
     * The constant value of this field is the largest value permitted
     * for the radix argument in radix-conversion methods such as the
     * {@code digit} method, the {@code forDigit} method, and the
     * {@code toString} method of class {@code Integer}.
     *
     * @see     Character#digit(char, int)
     * @see     Character#forDigit(int, int)
     * @see     Integer#toString(int, int)
     * @see     Integer#valueOf(String)
     */
    @HelloField
    public static final int MAX_RADIX = 36;
    
}
