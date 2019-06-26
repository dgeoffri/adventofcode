package main

import (
	"crypto/md5"
	"strings"
	"fmt"
	"log"
	"os"
)

func printusage() {
	fmt.Printf("Usage: %s <puzzle input>\n", os.Args[0])
	log.Fatal("Invalid or no input provided")
}

func main() {
	if len(os.Args) != 2 {
		printusage()
	}

	var num int
	var md5hex string
	var data []byte

	for num = 0; ! strings.HasPrefix(md5hex, "00000"); num++ {
		data = []byte(fmt.Sprintf("%s%d", os.Args[1], num))
		md5hex = fmt.Sprintf("%x", md5.Sum(data))
	}

	fmt.Println("The answer is:", num-1)
}
