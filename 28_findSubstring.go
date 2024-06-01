package main

import "fmt"

func checkStrs(haystack *string, needle *string, index *int) bool {
	j := 0
	for j < len(*needle) {
		if len(*haystack)-1 < *index+j {
			return false
		}

		if (*haystack)[*index+j] != (*needle)[j] {
			return false
		}
		j++
	}
	return true
}

func strStr(haystack string, needle string) int {
	i := 0

	for i < len(haystack) {
		if haystack[i] == needle[0] && checkStrs(&haystack, &needle, &i) {
			return i
		}
		i++
	}
	return -1
}

func main() {
	haystack := "aaa"
	needle := "aaaa"

	fmt.Println(strStr(haystack, needle))
}
