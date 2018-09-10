package org.chapter1Test;

import org.chapter1.Q001;
import org.junit.*;

import junit.framework.TestCase;

public class Q001Test extends TestCase {
	Q001 q1;
	
	@Before
	protected void setUp() throws Exception {
		q1 = new Q001();
	}
	
	@After
	protected void tearDown() throws Exception {
	}
	
	@Test
	public void testTrue() {
		String unique = "abcdefg";
		boolean isUnique = q1.isUnique(unique);
		assertTrue(isUnique == true);
		isUnique = q1.isUniqueWithNoDataStructures(unique);
		assertTrue(isUnique == true);
	}
	
	@Test
	public void testFalse() {
		String notUnique = "aabcdef";
		boolean isUnique = q1.isUnique(notUnique);
		assertTrue(isUnique == false);
		isUnique = q1.isUniqueWithNoDataStructures(notUnique);
		assertTrue(isUnique == false);
	}
	
	@Test
	public void testEmptyString() {
		String empty = "";
		boolean emptyVal = q1.isUnique(empty);
		assertTrue(emptyVal == true);
		emptyVal = q1.isUniqueWithNoDataStructures(empty);
		assertTrue(emptyVal == true);
	}
	
	@Test
	public void testLastCharacter() {
		String str = "lasttt";
		boolean isUnique = q1.isUnique(str);
		assertTrue(isUnique == false);
		isUnique = q1.isUniqueWithNoDataStructures(str);
		assertTrue(isUnique == false);
	}
	
	@Test
	public void testNonConsecutiveCharacters() {
		String str = "abcdabc";
		boolean isUnique = q1.isUnique(str);
		assertTrue(isUnique == false);
		isUnique = q1.isUniqueWithNoDataStructures(str);
		assertTrue(isUnique == false);
	}

}
