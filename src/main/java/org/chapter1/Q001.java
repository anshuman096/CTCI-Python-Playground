package org.chapter1;

import java.util.HashSet;
import java.util.Set;

/**
 * Implement an algorithm to determine if a string has all unique characters.
 * What if you cannot use additional data structures?
 *
 */
public class Q001 {
	
	public boolean isUnique(String str) {
		Set<Character> strSet = new HashSet<Character> ();
		for(int i = 0; i < str.length(); i++) {
			if(strSet.contains(str.charAt(i)))
				return false;
			else
				strSet.add(str.charAt(i));
		}
		return true;
	}
	
	public boolean isUniqueWithNoDataStructures(String str) {
		for(int i = 0; i < str.length() - 1; i++) {
			char curr = str.charAt(i);
			for(int j = i + 1; j < str.length(); j++) {
				char check = str.charAt(j);
				if(curr == check)
					return false;
				else
					continue;
			}
		}
		return true;
	}
	
    
}
