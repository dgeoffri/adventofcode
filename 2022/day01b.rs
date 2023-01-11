use std::io::{BufReader, BufRead};
use std::fs::File;
// use std::str::FromStr;

fn main() { 
    let mut calories_per_elf: Vec<u32> = Vec::new();
    let f = File::open("day01.txt").unwrap();
    let reader = BufReader::new(f);
    let mut total = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        match line.trim().parse::<u32>() {
            Ok(n) => total += n,
            Err(_) => { calories_per_elf.push(total); total = 0 }
        };
    }
    calories_per_elf.sort();
    let top_3_elves:u32 = calories_per_elf.iter().rev().take(3).sum();
    println!("The sum of the calories carried by the top 3 elves is {} calories.", top_3_elves);
}
