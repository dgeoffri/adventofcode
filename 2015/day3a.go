package main

import (
	"fmt"
	"os"
	"log"
	"io/ioutil"
)

func printusage() {
	fmt.Printf("Usage: %s [directions file]\n\nFind how many unique addresses Santa visits based on directions given in directions file\nIf no directions file is given, day3.txt is assumed to contain the input.\n", os.Args[0])
	log.Fatal("FATAL: no filename given")
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

type Address struct {
	x, y int
}

func main() {
	var fname string

	if (len(os.Args) > 2) || ((len(os.Args) == 2) && (os.Args[1] == "-h")) || ((len(os.Args) == 2) && (os.Args[1] == "--help")) {
		printusage()
	}

	if len(os.Args) == 2 {
		fname = os.Args[1]
	} else {
		fname = "day3.txt"
	}

	dat, err := ioutil.ReadFile(fname)
	check(err)

	unique_addresses := make(map[Address]bool)
	addresses := make([]Address, len(dat)+1)
	current_address := Address{0,0}
	unique_addresses[current_address] = true

	for i := 0; i < len(dat); i++ {
		addresses[i] = current_address
		switch(dat[i]) {
			case '^':
				current_address.y++
			case 'v':
				current_address.y--
			case '<':
				current_address.x--
			case '>':
				current_address.x++
		}
		unique_addresses[current_address] = true
	}
	addresses[len(dat)] = current_address

	// for i := 0; i < len(addresses); i++ {
	// 	fmt.Println(addresses[i])
	// }

	fmt.Printf ("%v houses are visted at least once\n", len(unique_addresses))
}
