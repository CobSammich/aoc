// Advent of Code 2021 Day 2 part 1
// Written by Jacob Morris (jacobm3@vt.edu)

use std::fs::File; // File I/O
use std::env; // Read command line args
use std::io::{prelude::*, BufReader};

// Command has a direction component and a length component that defines how far the submarine
// would move in that direction
#[derive(Debug)]
struct Command {
    direction: String, // forward, down, or up
    length: u32,
}

// Read input file and parse the each line into a Command
fn read_input(filename: String) -> Vec<Command> {
    println!("Reading input from {}", filename);
    // open file
    let file = File::open(filename).expect("file not found");
    let buf = BufReader::new(file);

    // output is a vector of "commands"
    let mut commands: Vec<Command> = Vec::new();

    // Parse file into vector of commands
    for line in buf.lines() {
        // Ok() -> String
        let line = line.expect("Unable to read line");
        // Split command into its direction and length
        let mut line_iter = line.split_whitespace();

        // read direction
        let curr_direction = String::from(line_iter.next()
                                          .expect("Could not read direction"));
        // read length
        let curr_length: u32 = line_iter.next()
            .expect("Could not read length")
            .parse::<u32>() // parse string into int
            .unwrap();

        // make current command and push into all the commands
        let curr_command = Command {
            direction: curr_direction,
            length: curr_length
        };
        //println!("{:#?}", curr_command);
        commands.push(curr_command);
    }
    return commands;
}

// count the horizontal and vertical positions and get their product
fn solve(commands: Vec<Command>) -> u32 {
    let mut xpos = 0;
    let mut ypos = 0;

    // iterate over all commands
    for command in commands {
        //println!("{}", command.direction);
        // handle positions based on direction
        if command.direction == "forward" {
            xpos += command.length;
        }
        else if command.direction == "down" {
            ypos += command.length;
        }
        else if command.direction == "up" {
            ypos -= command.length;
        }
        else {
            println!("Invalid movement: {}", command.direction)
        }
    }

    // return the product of the horizontal and vertical displacements
    return xpos * ypos;
}

fn main() {
    // Read in command line arguments boilerplate
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Please provide an input file... \nNone provided - exiting");
        std::process::exit(-1);
    }
    let filename = &args[1];
    // end boilerplate

    // don't use & so that filename is cleaned up
    let commands: Vec<Command> = read_input(String::from(filename));
    // count the number of times the measurements has increased
    let answer: u32 = solve(commands);

    // print answer
    println!("The answer is {}", answer)
}
