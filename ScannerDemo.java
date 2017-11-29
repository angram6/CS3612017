/***********************************************************************
 * CS361 - Programming Implementations
 * Professor & Author: Christelle Scharff
 * Fall 2017
 * 
 * Code completed by: Tomer Alon & Angie Ramirez
 ***************************************************************************/

public class ScannerDemo {

	private static String file1 = ("prog2.jay");
	private static int counter = 1;

	public static void main(String args[]) {

		TokenStream ts = new TokenStream(file1);

		System.out.println("File: " + file1);

		Token t;

		while (!ts.isEndofFile()) {
			System.out.println("Counter= " + counter);
			t = ts.nextToken();
			System.out.println("token " + counter + ": '" + t.getValue() + "'" + " type: " + t.getType());
			counter++;

		}
	}
}
