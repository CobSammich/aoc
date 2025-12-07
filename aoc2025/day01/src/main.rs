// Determine the number of times number increases from the previous number.
use std::env; // Read command line args
use std::fs::File;
// File I/O
use std::io::{prelude::*, BufReader};

#[derive(Debug)]
struct Line {
    direction: char,
    magnitude: i32,
}

// Read input file and parse each line into a Line struct
fn read_input(filename: String) -> Vec<Line> {
    println!("Reading input from {}", filename);
    let file = File::open(filename).expect("file not found");
    let buf = BufReader::new(file);

    let data: Vec<Line> = buf
        .lines()
        .filter_map(|line| {
            let pline = line.unwrap();
            Some(Line {
                direction: pline.chars().next().unwrap(),
                magnitude: pline[1..].trim().parse().unwrap(),
            })
        })
        .collect();
    return data;
}

fn part1(data: &Vec<Line>) -> i32 {
    let mut dial = 50;
    let mut num_point_at_zero = 0;
    for line in data {
        let mut curr_magnitude = line.magnitude;
        if line.direction == 'L' {
            curr_magnitude *= -1;
        }

        dial += curr_magnitude;
        dial %= 100;
        if dial == 0 {
            num_point_at_zero += 1;
        }
    }
    return num_point_at_zero;
}

fn part2(data: &Vec<Line>) -> i32 {
    let mut dial = 50;
    let mut num_pass_zero = 0;
    for line in data {
        let curr_rotation_pass_zero = line.magnitude / 100;
        let mut curr_magnitude = line.magnitude % 100;

        if line.direction == 'L' {
            curr_magnitude *= -1;
        }

        let mut new_dial = (dial + curr_magnitude) % 100;
        if new_dial < 0 {
            // -18 % 100 in rust doesn't = 82, so do this
            new_dial += 100;
        }

        // edge cases
        if new_dial == 0 {
            num_pass_zero += 1
        } else if line.direction == 'L' && dial != 0 && new_dial > dial {
            num_pass_zero += 1
        } else if line.direction == 'R' && dial != 0 && new_dial < dial {
            num_pass_zero += 1
        }
        num_pass_zero += curr_rotation_pass_zero;
        dial = new_dial
    }
    return num_pass_zero;
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Please provide an input file... \nNone provided - exiting");
        std::process::exit(-1);
    }
    let filename = &args[1];

    // don't use & so that filename is cleaned up
    let data: Vec<Line> = read_input(String::from(filename));

    let p1_answer = part1(&data);
    println!("Part 1 Answer: {}", p1_answer);

    let p2_answer = part2(&data);
    println!("Part 2 Answer: {}", p2_answer);
}
