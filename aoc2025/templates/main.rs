// Determine the number of times number increases from the previous number.
use std::env; // Read command line args
use std::fs::File; // File I/O
use std::io::{prelude::*, BufReader};

// Read input file and parse the each line into an int32 forming an vector
fn read_input(filename: String) -> Vec<i32> {
    println!("Reading input from {}", filename);
    // open file
    let file = File::open(filename).expect("file not found");
    let buf = BufReader::new(file);

    // Parse files into vector of ints
    let vals: Vec<i32> = buf
        .lines()
        .map(|line| line.unwrap().parse::<i32>().unwrap())
        .collect();

    return vals;
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Please provide an input file... \nNone provided - exiting");
        std::process::exit(-1);
    }
    let filename = &args[1];

    // don't use & so that filename is cleaned up
    let elves: Vec<i32> = read_input(String::from(filename));
}
