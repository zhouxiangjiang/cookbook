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
 * Java class definition.
 * 
 * <h2>Access Level</h2>
 * <p>
 * Use the <strong>most restrictive</strong> access level that makes sense for a
 * particular member. Use <code>private</code> unless you have a good reason not
 * to. Avoid <code>public</code> fields except for <strong>constants</strong>.
 * <code>public</code> fields are <strong>not recommended for production
 * code</strong>, since they tend to link you to a particular implementation and
 * limit your flexibility in changing your code.
 * </p>
 * 
 * @since JDK 8
 */
public class HelloClass {

	// Constant Attributes
	//
	// If a primitive type or a string is defined as a constant and the value
	// is known at compile time, the compiler replaces the constant name
	// everywhere in the code with its value. This is called a "compile-time
	// constant". If the value of the constant in the outside world changes,
	// you will need to recompile any classes that use this constant to get
	// the current value.
	public static final double PI = 3.141592653589793;

	private static int class_attribute = 0; // class attribute

	// Static Initialization Block
	//
	// If initialization for class attributes requires some logic
	// (for example, error handling or a <code>for</code> loop to fill a
	// complex array), simple assignment is inadequate. To provide the same
	// capability for class attributes, the Java programming language includes
	// "static initialization blocks".
	//
	// A class can have any number of static initialization blocks, and they
	// can appear anywhere in the class body. The runtime system guarantees
	// that static initialization blocks are called in the order that they
	// appear in the source code.
	static {
		// TODO: initialization code goes here ...
	}

	protected int instance_attribute = 0; // instance attribute

	/**
	 * Constructor
	 * 
	 * <p>
	 * If present, the invocation of <strong>another constructor</strong> (e.g.,
	 * <code>this()</code>) must be the <strong>first line</strong> in the
	 * constructor.
	 * </p>
	 * 
	 * <p>
	 * Methods called from <strong>constructors</strong> should generally be
	 * declared <code>final</code>. If a constructor calls a non-final method, a
	 * subclass may redefine that method with surprising or undesirable results.
	 * </p>
	 * 
	 * @param i
	 *            Init value of instance attribute
	 */
	public HelloClass(int i) {
		class_attribute++;
		this.instance_attribute = i;
	}

	public HelloClass() {
		this(0);
	}

	/**
	 * Instance method
	 * 
	 * @param i
	 *            Parameter of instance method
	 */
	public void instanceMethod(int i) {
		this.instance_attribute += i;
	}

	/**
	 * Overloaded method
	 * 
	 * <strong>NOTE</strong>: Overloaded methods should be used sparingly, as
	 * they can make code much less readable.
	 * 
	 * @param f
	 *            Nothing
	 */
	public void instanceMethod(float f) {
		// TODO
	}

	/**
	 * Object Methods
	 *
	 * <ul>
	 * <li>{@link #clone()} - Creates and returns <strong>a copy</strong> of
	 * this object.
	 * <li>{@link #equals(Object)} - Indicates whether some other object is
	 * "<strong>equal to</strong>" this one.
	 * <li>{@link #finalize()} - Called by the <strong>garbage
	 * collector</strong> on an object when garbage.
	 * <li>{@link #getClass()} - Returns the <strong>runtime class</strong> of
	 * an object.
	 * <li>{@link #hashCode()} - Returns a <strong>hash code value</strong> for
	 * the object.
	 * <li>{@link #toString()} - Returns a <strong>string
	 * representation</strong> of the object.
	 * </ul>
	 */
	@Override
	public String toString() {
		return String.valueOf(this.instance_attribute);
	}

	// start point of Java program
	public static void main(String[] args) {
		HelloClass h = new HelloClass(1); // create an object/instance
		System.out.println(HelloClass.class_attribute);
		System.out.println(h);
	}
}

/**
 * Inheritance
 * 
 * @since JDK 7
 */
class Child extends HelloClass {

	/**
	 * Child Constructor
	 * 
	 * <p>
	 * <code>super</code> means instance of super class (e.g.,
	 * {@link HelloClass})
	 * </p>
	 * 
	 * <p>
	 * <strong>Note</strong>: If a constructor does not explicitly invoke a
	 * superclass constructor, the Java compiler automatically inserts a call to
	 * the <strong>no-argument constructor</strong> of the superclass. If the
	 * super class does not have a no-argument constructor, you will get a
	 * compile-time error. <code>Object</code> does have such a constructor, so
	 * if <code>Object</code> is the only superclass, there is no problem.
	 * </p>
	 */
	public Child() {
		super();
	}

	/**
	 * Instance method inheritance from parent class {@link HelloClass}
	 * 
	 * @param i
	 *            Parameter of instance method
	 */
	@Override
	public void instanceMethod(int i) {
		this.instance_attribute += i;
	}
}

/**
 * Java Nested Class Definition
 * 
 * @since JDK 8
 */
class OuterClass {

	private NestedClass nc;

	public OuterClass() {
		this.nc = new NestedClass();
	}

	public static void main(String[] args) {
		OuterClass oc = new OuterClass();
		System.out.println(oc.nc);
	}

	/**
	 * Nested class.
	 * 
	 * <p>
	 * <strong>Nested classes</strong> are divided into two categories:
	 * <code>static</code> and <strong>non-static</strong>.
	 * </p>
	 * <ul>
	 * <li>Nested classes that are declared <code>static</code> are simply
	 * called <strong>static nested classes</strong>.
	 * <li>Non-static nested classes are called <strong>inner classes</strong>.
	 * </ul>
	 * 
	 * <p>
	 * Nested classes can be declared <code>private</code>, <code>public</code>,
	 * <code>protected</code>, or <em>package private</em> as default.
	 * </p>
	 * <ul>
	 * <li><strong>Inner classes</strong> have access to other members of the
	 * enclosing class, even if they (members of enclosing class) are declared
	 * <code>private</code>.
	 * <li><strong>Static nested classes</strong> do <strong>NOT</strong> have
	 * access to other members of the enclosing class.
	 * </ul>
	 */
	private class NestedClass {

		@Override
		public String toString() {
			return "Nested Class";
		}
	}
}