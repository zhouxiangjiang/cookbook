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
 * A Java program
 * 
 * @see http://www.oracle.com/technetwork/java/javase/downloads/index.html
 * @see http://docs.oracle.com/javase/tutorial/
 * @since JDK 7
 */
class HelloJava {

	// start point of Java program
	public static void main(String[] args) {
		System.out.println("Hello Java!");
	}

	// Variable Arguments
	public void var_args(String... strings) {
		// TODO strings[0], strings[1], ...
	}

}

/**
 * EnumType Definition (Day in a week).
 * 
 * <p>
 * All enums <strong>implicitly</strong> extend {@link java.lang.Enum}.
 * </p>
 * 
 * <p>
 * Since Java does not support multiple inheritance, an <code>enum</code>
 * <strong>cannot extend anything else</strong>.
 * </p>
 * 
 * @since JDK 7
 */
enum Day {

	/*
	 * The compiler automatically creates the constants that are defined
	 * <strong>at the beginning</strong> of the <code>enum</code> body.
	 */
	SUNDAY("Sun"), MONDAY("Mon"), TUESDAY("Tue"), WEDNESDAY("Wed"), THURSDAY(
			"Thu"), FRIDAY("Fri"), SATURDAY("Sat");

	/**
	 * Abbreviation name of the day in a week.
	 */
	private final String abbr;

	/**
	 * Create an instance with abbreviation name.
	 * 
	 * <p>
	 * The <strong>constructor</strong> for an <code>enum</code> type must be
	 * <strong>package-private</strong> or <code>private</code> access.
	 * </p>
	 * 
	 * <p>
	 * <strong>Notes</strong>: You <strong>cannot</strong> invoke an
	 * <code>enum</code> constructor yourself.
	 * </p>
	 * 
	 * @param abbr
	 *            the abbreviation name of the day.
	 */
	private Day(String abbr) {
		this.abbr = abbr;
	}

	/**
	 * Create an instance without anything.
	 */
	private Day() {
		this("Unknown");
	}

	/**
	 * Get the abbreviation name of the day in a week.
	 * 
	 * @return the abbreviation name of the day.
	 */
	public String getAbbreviation() {
		return this.abbr;
	}

	/*
	 * Usage
	 * 
	 * The compiler <strong>automatically adds some special methods</strong>
	 * when it creates an <code>enum</code>
	 * 
	 * <ul> <li>{@link #toString()} <li>{@link #values()} </ul>
	 */
	public static void main(String[] args) {
		for (Day d : Day.values()) {
			System.out.println(d + ", " + d.getAbbreviation());
		}
	}
}
