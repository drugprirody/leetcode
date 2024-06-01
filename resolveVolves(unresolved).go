package main

import "fmt"

func reverseVowels(s string) string {
	chars, l, last_vowel := []rune(s), 0, -1

	for l < len(s) {
		switch chars[l] {
		case 'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U':
			if last_vowel != -1 {
				chars[l], chars[last_vowel] = chars[last_vowel], chars[l]
			}
			last_vowel = l
		}

		l++
	}
	return string(chars)
}

func main() {
	s := "hello"
	fmt.Println(reverseVowels(s))
}
