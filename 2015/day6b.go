package main

import (
	"fmt"
	"regexp"
	"os"
	"log"
	"bufio"
	"strconv"
	// "strings"
)

type coord struct {
	x, y int
}

func printusage() {
	fmt.Printf("Usage: %s [instructions file]\n\nFind the total brightness of all lit lights after following instructions in instructions file\nIf no instructions file is given, day6.txt is assumed to contain the input.\n", os.Args[0])
	log.Fatal("FATAL: no filename given")
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func getfname(fname string) string {
	if (len(os.Args) > 2) || ((len(os.Args) == 2) && (os.Args[1] == "-h")) || ((len(os.Args) == 2) && (os.Args[1] == "--help")) {
		printusage()
	}

	if (len(os.Args) == 2) {
		fname = os.Args[1]
	}

	return fname
}

func operate(operation string, corner1 coord, corner2 coord, lightarray [][]int) {
	for y := corner1.y; y <= corner2.y; y++ {
		for x := corner1.x; x <= corner2.x; x++ {
			switch operation {
				case "turn on":
					lightarray[y][x] += 1
				case "turn off":
					tmpval := lightarray[y][x] - 1
					if tmpval < 0 {
						tmpval = 0
					}
					lightarray[y][x] = tmpval
				case "toggle":
					lightarray[y][x] += 2
			}
		}
	}
}

func observebrightness(lightarray [][]int) (int, int) {
	sum := 0
	maxbrightness := 0
	for y := 0; y < len(lightarray); y++ {
		for x :=0; x < len(lightarray[0]); x++ {
			tmpval := lightarray[y][x]
			sum += tmpval
			if tmpval > maxbrightness {
				maxbrightness = tmpval
			}
		}
	}
	return sum, maxbrightness
}

func writepgm(fname string, lightarray [][]int, maxbrightness int) {
	f, err := os.Create(fname)
	check(err)

	defer f.Close()

	w := bufio.NewWriter(f)

	defer w.Flush()
	
	fmt.Fprintf(w, "P2\n1000 1000\n%d\n", maxbrightness)
	for y := 0; y < len(lightarray); y++ {
		var newval string = strconv.Itoa(lightarray[y][0])
		curlinelen := len(newval)
		w.WriteString(newval)
		for x := 1; x < len(lightarray[y]); x++ {
			newval = strconv.Itoa(lightarray[y][x])
			if curlinelen + len(newval) > 70 + 1 {  // + 1 for the length of the space
				w.WriteByte('\n')
				w.WriteString(newval)
				curlinelen = len(newval) + 1
			} else {
				w.WriteByte(' ')
				w.WriteString(newval)
				curlinelen += len(newval) +1
			}
		}
		w.WriteByte('\n')
	}
}

func main() {
	r := regexp.MustCompile(`(.*) (\d+,\d+) through (\d+,\d+)`)

	f, err := os.Open(getfname("day6.txt"))
	check(err)

	s := bufio.NewScanner(f)

	defer f.Close()

	lightarray := make([][]int, 1000)
	for i := 0; i < 1000; i++ {
		lightarray[i] = make([]int, 1000)
	}

	for s.Scan() {
		matchgroups := r.FindStringSubmatch(s.Text())[1:]

		operation := matchgroups[0]
		corner1, corner2 := coord{}, coord{}

		fmt.Sscanf(matchgroups[1], "%d,%d", &corner1.x, &corner1.y)
		fmt.Sscanf(matchgroups[2], "%d,%d", &corner2.x, &corner2.y)

		// fmt.Printf("%s\n  corner1: %v\n  corner2: %v\n", operation, corner1, corner2)

		operate(operation, corner1, corner2, lightarray)
	}

	// fmt.Println(lightarray)
	totalbrightness, maxbrightness := observebrightness(lightarray)
	fmt.Printf("The total brightness of all lights is %d\n\nThe brightest light lit has a brightness of %d\n", totalbrightness, maxbrightness)

	writepgm("day6b.pgm", lightarray, maxbrightness)
}
