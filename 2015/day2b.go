package main

import (
	"fmt"
	"os"
	"log"
	"bufio"
	"strings"
	"strconv"
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

func min(is ...int) int {
	min := is[0]
	for _, i := range is[1:] {
		if i < min {
			min = i
		}
	}
	return min
}

func main() {
	total_length := 0

	if len(os.Args) != 2 {
		printusage()
	}

	f, err := os.Open(os.Args[1])
	check(err)

	s := bufio.NewScanner(f)

	for s.Scan() {
		splitline := strings.Split(s.Text(), "x")
		l, err := strconv.Atoi(splitline[0])
		check(err)
		w, err := strconv.Atoi(splitline[1])
		check(err)
		h, err := strconv.Atoi(splitline[2])
		check(err)
		total_length += 2*min(l+w,w+h,h+l)+l*w*h
	}

	fmt.Printf("%v feet of wrapping paper is needed to wrap all the presents\n", total_length)
}
