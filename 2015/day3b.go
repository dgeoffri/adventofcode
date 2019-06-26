package main

import (
	"fmt"
	"os"
	"log"
	"io/ioutil"
)

func printusage() {
	fmt.Printf("Usage: %s <directions file>\n\nFind how many unique addresses Santa visits based on directions given in <directions file>\n", os.Args[0])
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

	if len(os.Args) > 2 {
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
	current_address_array := [2]Address{{0,0}, {0,0}}
	current_santa := 0
	unique_addresses[current_address_array[0]] = true

	for i := 0; i < len(dat); i++ {
		addresses[i] = current_address_array[current_santa]
		switch(dat[i]) {
			case '^':
				current_address_array[current_santa].y++
			case 'v':
				current_address_array[current_santa].y--
			case '<':
				current_address_array[current_santa].x--
			case '>':
				current_address_array[current_santa].x++
		}
		unique_addresses[current_address_array[current_santa]] = true
		current_santa ^= 1
	}
	addresses[len(dat)] = current_address_array[current_santa]

	// for i := 0; i < len(addresses); i++ {
	// 	fmt.Println(addresses[i])
	// }

	fmt.Printf ("%v houses are visted at least once\n", len(unique_addresses))
}
