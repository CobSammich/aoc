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

    let mut curr_buffer: i32 = 0;
    let mut elves: Vec<i32> = Vec::new();

    // Definitely a more elegant way to do this with map
    for line in buf.lines() {
        if let Ok(line) = line {
            if line.len() == 0 {
                elves.push(curr_buffer);
                curr_buffer = 0;
                continue;
            }
            curr_buffer += line.parse::<i32>().unwrap();
        }
    }
    return elves;
}

fn part1(data: &Vec<i32>) -> i32 {
    let mut max = -10;
    for val in data {
        if *val >= max {
            max = *val;
        }
    }
    return max;
}

fn part2(data: &mut Vec<i32>, k: i32) -> i32 {
    data.sort_by(|a, b| b.cmp(a));

    let mut sum: i32 = 0;
    for i in 0..k {
        sum += &data[i as usize];
    }
    return sum;
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Please provide an input file... \nNone provided - exiting");
        std::process::exit(-1);
    }
    let filename = &args[1];

    // don't use & so that filename is cleaned up
    let mut elves: Vec<i32> = read_input(String::from(filename));
    println!("{:?}", elves);

    let p1: i32 = part1(&elves);
    println!("Part 1: {}", p1);

    let p2: i32 = part2(&mut elves, 3);
    println!("Part 2: {}", p2);

}
