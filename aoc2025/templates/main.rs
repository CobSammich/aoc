// Determine the number of times number increases from the previous number.
use std::env; // Read command line args
use std::fs::File; // File I/O
use std::io::{prelude::*, BufReader};

// Read input file and parse the each line into an int32 forming an vector
fn read_input(filename: String) -> Vec<String> {
    println!("Reading input from {}", filename);
    // open file
    let file = File::open(filename).expect("file not found");
    let buf = BufReader::new(file);

    // Parse files into vector of ints
    let vals: Vec<String> = buf.lines().map(|line| line.unwrap()).collect();

    return vals;
}

fn part1(data: &Vec<String>) -> i32 {
    return 0;
}

fn part2(data: &Vec<String>) -> i32 {
    return 0;
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Please provide an input file... \nNone provided - exiting");
        std::process::exit(-1);
    }
    let filename = &args[1];

    // don't use & so that filename is cleaned up
    let data: Vec<String> = read_input(String::from(filename));

    let p1_answer = part1(&data);
    println!("Part 1 Answer: {}", p1_answer);

    let p2_answer = part2(&data);
    println!("Part 2 Answer: {}", p2_answer);
}
