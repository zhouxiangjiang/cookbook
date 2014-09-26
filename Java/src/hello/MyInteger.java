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

import java.lang.annotation.Native;


/**
 * Own {@code Integer}.
 * 
 * @author Li Yun <leven.cn@gmail.com>
 * @see Integer
 * @since JDK 8
 */
@HelloClass
public final class MyInteger {
    
    /**
     * A constant holding the minimum value an {@code int} can
     * have, -2<sup>31</sup>.
     */
    @HelloField
    @Native
    public static final int   MIN_VALUE = 0x80000000;
    
    
    /**
     * A constant holding the maximum value an {@code int} can
     * have, 2<sup>31</sup>-1.
     */
    @HelloField
    @Native
    public static final int   MAX_VALUE = 0x7fffffff;
    
    
    @HelloField
    public static final int DEFAULT_RADIX = 10;
    
    
    /**
     * The value of the {@code MyInteger}.
     */
    @HelloField
    private int value;
    
    
    @HelloConstructor
    public MyInteger(int value) {
        this.value = value;
    }
    
    
    /**
     * Parses the string argument as a signed integer in the radix
     * specified by the second argument. The characters in the string
     * must all be digits of the specified radix (as determined by
     * whether {@link java.lang.Character#digit(char, int)} returns a
     * nonnegative value), except that the first character may be an
     * ASCII minus sign {@code '-'} ({@code '\u005Cu002D'}) to
     * indicate a negative value or an ASCII plus sign {@code '+'}
     * ({@code '\u005Cu002B'}) to indicate a positive value. The
     * resulting integer value is returned.
     *
     * <p>An exception of type {@code NumberFormatException} is
     * thrown if any of the following situations occurs:
     * <ul>
     * <li>The first argument is {@code null} or is a string of
     * length zero.
     *
     * <li>The radix is either smaller than
     * {@link MyCharacter#MIN_RADIX} or larger than
     * {@link MyCharacter#MAX_RADIX}.
     *
     * <li>Any character of the string is not a digit of the specified
     * radix, except that the first character may be a minus sign
     * {@code '-'} ({@code '\u005Cu002D'}) or plus sign
     * {@code '+'} ({@code '\u005Cu002B'}) provided that the
     * string is longer than length 1.
     *
     * <li>The value represented by the string is not a value of type
     * {@code int}.
     * </ul>
     *
     * <p>Examples:
     * <blockquote><pre>
     * parseInt("0", 10) returns 0
     * parseInt("473", 10) returns 473
     * parseInt("+42", 10) returns 42
     * parseInt("-0", 10) returns 0
     * parseInt("-FF", 16) returns -255
     * parseInt("1100110", 2) returns 102
     * parseInt("2147483647", 10) returns 2147483647
     * parseInt("-2147483648", 10) returns -2147483648
     * parseInt("2147483648", 10) throws a NumberFormatException
     * parseInt("99", 8) throws a NumberFormatException
     * parseInt("Kona", 10) throws a NumberFormatException
     * parseInt("Kona", 27) returns 411787
     * </pre></blockquote>
     *
     * @param      s   the {@code String} containing the integer
     *                  representation to be parsed
     * @param      radix   the radix to be used while parsing {@code s}.
     * @return     the integer represented by the string argument in the
     *             specified radix.
     * @exception  NumberFormatException if the {@code String}
     *             does not contain a parsable {@code int}.
     */
    @HelloMethod
    public static int parseInt(String s, int radix)
            throws NumberFormatException {
        /*
         * WARNING: This method may be invoked early during VM
         * initialization before IntegerCache is initialized. Care must be
         * taken to not use the valueOf method.
         */

        if (s == null) {
            throw new NumberFormatException("null");
        }

        if (radix < MyCharacter.MIN_RADIX) {
            throw new NumberFormatException("radix " + radix
                    + " less than Character.MIN_RADIX");
        }

        if (radix > MyCharacter.MAX_RADIX) {
            throw new NumberFormatException("radix " + radix
                    + " greater than Character.MAX_RADIX");
        }

        int result = 0;
        boolean negative = false;
        int i = 0, len = s.length();
        int limit = -MyInteger.MAX_VALUE;
        int multmin;
        int digit;

        if (len > 0) {
            char firstChar = s.charAt(0);
            if (firstChar < '0') { // Possible leading "+" or "-"
                if (firstChar == '-') {
                    negative = true;
                    limit = MyInteger.MIN_VALUE;
                } else if (firstChar != '+') {
                    throw new NumberFormatException(
                            "For input string: \"" + s + "\"");
                }

                if (len == 1) { // Cannot have lone "+" or "-"
                    throw new NumberFormatException(
                            "For input string: \"" + s + "\"");
                }
                i++;
            }
            multmin = limit / radix;
            while (i < len) {
                // Accumulating negatively avoids surprises near MAX_VALUE
                digit = Character.digit(s.charAt(i++), radix);
                if (digit < 0) {
                    throw new NumberFormatException(
                            "For input string: \"" + s + "\"");
                }
                if (result < multmin) {
                    throw new NumberFormatException(
                            "For input string: \"" + s + "\"");
                }
                result *= radix;
                if (result < limit + digit) {
                    throw new NumberFormatException(
                            "For input string: \"" + s + "\"");
                }
                result -= digit;
            }
        } else {
            throw new NumberFormatException(
                    "For input string: \"" + s + "\"");
        }
        return negative ? result : -result;
    }
    
    
    /**
     * Parses the string argument as a signed decimal integer. The
     * characters in the string must all be decimal digits, except
     * that the first character may be an ASCII minus sign {@code '-'}
     * ({@code '\u005Cu002D'}) to indicate a negative value or an
     * ASCII plus sign {@code '+'} ({@code '\u005Cu002B'}) to
     * indicate a positive value. The resulting integer value is
     * returned, exactly as if the argument and the radix 10 were
     * given as arguments to the {@link #parseInt(java.lang.String,
     * int)} method.
     *
     * @param s    a {@code String} containing the {@code int}
     *             representation to be parsed
     * @return     the integer value represented by the argument in decimal.
     * @exception  NumberFormatException  if the string does not contain a
     *               parsable integer.
     */
    @HelloMethod
    public static int parseInt(String s) throws NumberFormatException {
        return parseInt(s, DEFAULT_RADIX);
    }
    
    
    /**
     * Cache to support the object identity semantics of autoboxing for values
     * between -128 and 127 (inclusive) as required by JLS.
     *
     * The cache is initialized on first usage.  The size of the cache
     * may be controlled by the {@code -XX:AutoBoxCacheMax=<size>} option.
     * During VM initialization, java.lang.Integer.IntegerCache.high property
     * may be set and saved in the private system properties in the
     * sun.misc.VM class.
     */
    private static final class IntegerCache {
        static final int LOW = -128;
        static final int HIGH;
        static final MyInteger[] CACHE;
        static final int INIT_HIGH = 127;

        static {
            // high value may be configured by property
            int h = INIT_HIGH;
            String integerCacheHighPropValue =
                sun.misc.VM.getSavedProperty(
                        "java.lang.Integer.IntegerCache.high");
            if (integerCacheHighPropValue != null) {
                try {
                    int i = parseInt(integerCacheHighPropValue);
                    i = Math.max(i, INIT_HIGH);
                    // Maximum array size is Integer.MAX_VALUE
                    h = Math.min(i, Integer.MAX_VALUE - (-LOW) - 1);
                } catch (NumberFormatException nfe) {
                    // If the property cannot be parsed into an int, ignore it.
                    ;
                }
            }
            HIGH = h;

            CACHE = new MyInteger[(HIGH - LOW) + 1];
            int j = LOW;
            for (int k = 0; k < CACHE.length; k++) {
                CACHE[k] = new MyInteger(j++);
            }

            // range [-128, 127] must be interned (JLS7 5.1.7)
            assert IntegerCache.HIGH >= INIT_HIGH;
        }

        private IntegerCache() { }
    }
    
    /**
     * Returns an {@code MyInteger} instance representing the specified
     * {@code int} value.  If a new {@code MyInteger} instance is not
     * required, this method should generally be used in preference to
     * the constructor {@link #MyInteger(int)}, as this method is likely
     * to yield significantly better space and time performance by
     * caching frequently requested values.
     *
     * This method will always cache values in the range -128 to 127,
     * inclusive, and may cache other values outside of this range.
     *
     * @param  i an {@code int} value.
     * @return an {@code MyInteger} instance representing {@code i}.
     */
    public static MyInteger valueOf(int i) {
        if (i >= IntegerCache.LOW && i <= IntegerCache.HIGH) {
            return IntegerCache.CACHE[i + (-IntegerCache.LOW)];
        }
        return new MyInteger(i);
    }
    
}
