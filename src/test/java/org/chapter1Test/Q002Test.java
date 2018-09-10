package org.chapter1Test;

import org.junit.*;
import static org.junit.Assert.*;
import org.chapter1.Q002;

public class Q002Test {
	Q002 q2;

	@Before
	public void setUp() throws Exception {
		q2 = new Q002();
	}

	@After
	public void tearDown() throws Exception {
	}

	@Test
	public void testPass() {
		String s1 = "hello";
		String s2 = "lehlo";
		boolean isPermutation = q2.isPermutation(s1, s2);
		assertTrue(isPermutation == true);
	}
	
	@Test
	public void testFail() {
		String s1 = "hello";
		String s2 = "goodbye";
		boolean isPermutation = q2.isPermutation(s1, s2);
		assertTrue(isPermutation == false);
	}
	
	@Test
	public void testDifferentLength() {
		String s1 = "shortstring";
		String s2 = "differentlengthstring";
		boolean isPermutation = q2.isPermutation(s1, s2);
		assertTrue(isPermutation == false);
	}
	
	@Test
	public void testWithSpaces() {
		String s1 = "The quick brown fox";
		String s2 = "brown fox The quick";
		boolean isPermutation = q2.isPermutation(s1, s2);
		assertTrue(isPermutation == true);
	}
	
	@Test
	public void testCase() {
		String s1 = "The quick Brown fox";
		String s2 = "the Quick brown Fox";
		boolean isPermutation = q2.isPermutation(s1, s2);
		assertTrue(isPermutation == false);
	}

}
