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
 * <li><code>byte</code> (8-bit)</li>
 * <li><code>short</code> (16-bit)</li>
 * <li><code>int</code> (32-bit)</li>
 * <li><code>long</code> (64-bit)</li>
 * <li><code>float</code> (32-bit IEEE 754)</li>
 * <li><code>double</code> (64-bit IEEE 754)</li>
 * <li><code>boolean</code> (true, false)</li>
 * <li><code>char</code> (16-bit Unicode)</li>
 * </ul>
 * 
 * 
 * <h2>Literal</h2>
 * <ul>
 * <li><code>0x</code> (hex integer)</li>
 * <li><code>0b</code> (binary integer)</li>
 * <li><code>F</code> (float)</li>
 * <li><code>D</code> (double)</li>
 * <li><code>\t</code> - Tab</li>
 * <li><code>\n</code> - Newline</li>
 * <li><code>\'</code> - '</li>
 * <li><code>\"</code> - "</li>
 * <li><code>\\</code> - \</li>
 * <li><code>long i = 999_999_999L</code></li>
 * </ul>
 *  
 * 
 * @see http://docs.oracle.com/javase/8/docs/index.html
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
	 * One of ANNOTATION_TYPE, TYPE, PACKAGE, CONSTRUCTOR, METHOD, PARAMETER,
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
 * Package annotation for <code>hello</code> package.
 * 
 * @author leven.cn@gmail.com
 * @since JDK 8
 */
@Target(ElementType.PACKAGE)
@Retention(RetentionPolicy.SOURCE)
@interface HelloPackage {
	
}

/**
 * Class annotation for <code>hello</code> package.
 * 
 * @author leven.cn@gmail.com
 * @since JDK 8
 */
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.SOURCE)
@interface HelloClass {
	
}


/**
 * Constructor annotation for <code>hello</code> package.
 * 
 * @author leven.cn@gmail.com
 * @since JDK 8
 */
@Target(ElementType.CONSTRUCTOR)
@Retention(RetentionPolicy.SOURCE)
@interface HelloConstructor {
	
}


/**
 * Method annotation for <code>hello</code> package.
 * 
 * @author leven.cn@gmail.com
 * @since JDK 8
 */
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.SOURCE)
@interface HelloMethod {
	
}


/**
 * Field annotation for <code>hello</code> package.
 * 
 * @author leven.cn@gmail.com
 * @since JDK 8
 */
@Target(ElementType.FIELD)
@Retention(RetentionPolicy.SOURCE)
@interface HelloField {
	
}
