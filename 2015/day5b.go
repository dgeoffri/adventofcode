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
		added := false
		for i := 0; i < len(word)-1 && !added; i++ {
			pair := word[i:i+2]
			if strings.Count(word, pair) >=2 {
				for j :=0; j < len(word)-2 && !added; j++ {
					if word[j] == word[j+2] {
						nicestrings = append(nicestrings, word)
						added = true
					}
				}
			}
		}
	}
	// fmt.Println(nicestrings)
	fmt.Println(len(nicestrings))
}
