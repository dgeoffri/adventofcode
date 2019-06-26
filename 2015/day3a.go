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
	if len(os.Args) != 2 {
		printusage()
	}

	dat, err := ioutil.ReadFile(os.Args[1])
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

	for i := 0; i < len(addresses); i++ {
		fmt.Println(addresses[i])
	}

	fmt.Printf ("%v houses are visted at least once\n", len(unique_addresses))
}
