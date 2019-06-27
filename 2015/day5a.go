package main

import (
	"fmt"
	"os"
	"log"
	"bufio"
	"strings"
)

func printusage() {
	fmt.Printf("Usage: %s [words file]\n\nCount the number of \"nice\" words in the words file\nIf no words file is given, day5.txt is assumed to contain the input.\n", os.Args[0])
	log.Fatal("FATAL: no filename given")
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	var fname string

	if (len(os.Args) > 2) || ((len(os.Args) == 2) && (os.Args[1] == "-h")) || ((len(os.Args) == 2) && (os.Args[1] == "--help")) {
		printusage()
	}

	if (len(os.Args) == 2) {
		fname = os.Args[1]
	} else {
		fname = "day5.txt"
	}

	f, err := os.Open(fname)
	check(err)

	s := bufio.NewScanner(f)

	var nicestrings []string

	for s.Scan() {
		word := s.Text()
		vowelcount := 0
		for _, vowel := range []string{"a","e","i","o","u"} {
			vowelcount += strings.Count(word, vowel)
		}
		if vowelcount >= 3 {
			var lastcharacter rune
			for _, character := range word {
				if character == lastcharacter {
					badcombo_found := false
					for _, badcombo := range []string{"ab", "cd", "pq", "xy"} {
						if strings.Contains(word, badcombo) {
							badcombo_found = true
							break
						}
					}
					if !badcombo_found {
						nicestrings = append(nicestrings, word)
						break
					}
				}
				lastcharacter = character
			}
		}
	}
	// fmt.Println(nicestrings)
	fmt.Println(len(nicestrings))
}
