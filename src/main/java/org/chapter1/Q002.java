package org.chapter1;

import java.util.HashSet;
import java.util.Set;

/**
 * Given two strings, write a method to decide if one is a permutation of the other.
 * 
 * @author anshuman
 *
 */
public class Q002 {
	
	public boolean isPermutation(String s1, String s2) {
		if(s1.length() != s2.length())
			return false;
		
		Set<Character> chars = new HashSet<Character> ();
		for(int i = 0; i < s1.length(); i++) {
			chars.add(s1.charAt(i));
		}
		
		for(int i = 0; i < s2.length(); i++) {
			if(chars.contains(s2.charAt(i)) == false) 
				return false;
		}
		return true;
		
	}
}
