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

/**
 * Hello Java.
 *
 * <h2>Primitive Types</h2>
 * <ul>
 * <li>{@code byte} (8-bit)</li>
 * <li>{@code short} (16-bit)</li>
 * <li>{@code int} (32-bit)</li>
 * <li>{@code long} (64-bit)</li>
 * <li>{@code float} (32-bit IEEE 754)</li>
 * <li>{@code double} (64-bit IEEE 754)</li>
 * <li>{@code boolean} (true, false)</li>
 * <li>{@code char} (16-bit Unicode)</li>
 * </ul>
 * 
 * 
 * <h2>Literal</h2>
 * <ul>
 * <li>{@code 0x} (hex integer)</li>
 * <li>{@code b} (binary integer)</li>
 * <li>{@code F} (float)</li>
 * <li>{@code D} (double)</li>
 * <li>{@code \t} - Tab</li>
 * <li>{@code \n} - Newline</li>
 * <li>{@code \'} - '</li>
 * <li>{@code \"} - "</li>
 * <li>{@code \\} - \</li>
 * <li>{@code long i = 999_999_999L}</li>
 * </ul>
 *  
 * 
 * @see <a href="http://docs.oracle.com/javase/8/docs/index.html">
 *      Java SE 8 Documentation</a>
 * @since JDK 8
 */
@HelloPackage
package hello;

import java.lang.annotation.Documented;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;


/**
 * Meta Annotation - Target.
 * 
 * @see java.lang.annotation
 * @since JDK 8
 */
@Documented  
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.ANNOTATION_TYPE)
@interface MyTarget {
	
    /**
     *  One of ANNOTATION_TYPE, TYPE, PACKAGE, CONSTRUCTOR, METHOD, PARAMETER,
     * FIELD, LOCAL_VARIABLE.
     */
    ElementType[] value();
}


/**
 * Meta Annotation - Retention.
 * 
 * @see java.lang.annotation
 * @since JDK 8
 */
@Documented  
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.ANNOTATION_TYPE)
@interface MyRetention {
	
    /**
     * One of RUNTIME, CLASS, SOURCE.
     */
    RetentionPolicy value();
}


/**
 * Meta Annotation - Documented.
 * 
 * @see java.lang.annotation
 * @since JDK 8
 */
@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.ANNOTATION_TYPE)
@interface MyDocumented {
	
}


/**
 * Meta Annotation - Inherited.
 *
 * @see java.lang.annotation
 * @since JDK 8
 */
@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.ANNOTATION_TYPE)
@interface MyInherited {
	
}


/**
 * JUnit Annotation - Test.
 * 
 * @see org.junit.Test
 * @since JUnit 4.11
 */
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@interface MyTest {
    
}


/**
 * JUnit Annotation - Rule.
 * 
 * @see org.junit.Rule
 * @since JUnit 4.11
 */
@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.FIELD, ElementType.METHOD })
@interface MyRule {
    
}


/**
 * Package annotation for <code>hello</code> package.
 * 
 * @author Li Yun <leven.cn@gmail.com>
 * @since JDK 8
 */
@Target(ElementType.PACKAGE)
@Retention(RetentionPolicy.SOURCE)
@interface HelloPackage {
	
}

/**
 * Class annotation for <code>hello</code> package.
 * 
 * @author Li Yun <leven.cn@gmail.com>
 * @since JDK 8
 */
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.SOURCE)
@interface HelloClass {
	
}


/**
 * Constructor annotation for <code>hello</code> package.
 * 
 * @author Li Yun <leven.cn@gmail.com>
 * @since JDK 8
 */
@Target(ElementType.CONSTRUCTOR)
@Retention(RetentionPolicy.SOURCE)
@interface HelloConstructor {
	
}


/**
 * Method annotation for <code>hello</code> package.
 * 
 * @author Li Yun <leven.cn@gmail.com>
 * @since JDK 8
 */
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.SOURCE)
@interface HelloMethod {
	
}


/**
 * Field annotation for <code>hello</code> package.
 * 
 * @author Li Yun <leven.cn@gmail.com>
 * @since JDK 8
 */
@Target(ElementType.FIELD)
@Retention(RetentionPolicy.SOURCE)
@interface HelloField {
	
}
