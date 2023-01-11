use std::io::{BufReader, BufRead};
use std::fs::File;

fn fight(a:char, b:char) -> u32 {
    let other_hand = (a as u32) - 64;
    let my_hand = (b as u32) - 87;
    if my_hand == other_hand {
        return my_hand + 3;
    }
    else if (my_hand == other_hand + 1) || (my_hand == 1 && other_hand == 3) {
        return my_hand + 6;
    }
    else {
        return my_hand;
    }
}

fn main() {
    let reader = BufReader::new(File::open("day02.txt").unwrap());
    let mut my_score = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        let mut iter = line.split_whitespace();
        let a = match iter.next() {
            Some(s) => s.chars().next().unwrap(),
            None => panic!("Malformed line?")
        };
        let b = match iter.next() {
            Some(s) => s.chars().next().unwrap(),
            None => panic!("Malformed line?")
        };
        my_score += fight(a, b);
    }
    println!("You've ended up with {} points", my_score);
}
