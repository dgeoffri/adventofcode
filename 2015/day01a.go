package main

import (
	"fmt"
	"os"
	"log"
	"io/ioutil"
)

func printusage() {
	fmt.Printf("Usage: %s <directions file>\n\nFind Santa's location based on up and down directions given in <directions file>\n", os.Args[0])
	log.Fatal("FATAL: no filename given")
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	if len(os.Args) != 2 {
		printusage()
	}

	dat, err := ioutil.ReadFile(os.Args[1])
	check(err)

	floor := 0
	for i := 0; i < len(dat); i++ {
		switch(dat[i]) {
			case '(':
				floor++
			case ')':
				floor--
		}
	}
	fmt.Printf("Santa should arrive on floor %v\n", floor)
}
