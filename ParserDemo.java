/***********************************************************************
 * CS361 - Programming Implementations
 * Professor & Author: Christelle Scharff
 * Fall 2017
 * 
 * Code completed by: Tomer Alon & Angie Ramirez
 ***************************************************************************/

public class ParserDemo {
	private static String file1 = "prog2.jay";
	public static void main(String[] args) {
		TokenStream tStream = new TokenStream(file1);
		System.out.println("test1");
		ConcreteSyntax cSyntax = new ConcreteSyntax(tStream);
		System.out.println("test2");
		Program p = cSyntax.program();
		System.out.println(p.display());
		System.out.println("test");
	}

}
