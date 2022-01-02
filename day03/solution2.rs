// Advent of Code 2021 Day 2 part 1
// Written by Jacob Morris (jacobm3@vt.edu)

use std::fs::File; // File I/O
use std::env; // Read command line args
use std::io::{prelude::*, BufReader};
//use bitvec::prelude::BitVec;

// Read input file and parse the each line into a Command
fn read_input(filename: String) -> Vec<Vec<bool>> {
    println!("Reading input from {}", filename);
    // open file
    let file = File::open(filename).expect("file not found");
    let buf = BufReader::new(file);

    // 2D bit matrix
    let mut diagnostic_report: Vec<Vec<bool>> = Vec::new();

    // Parse file into vector of commands
    for line in buf.lines() {
        // Ok() -> String
        let line = line.expect("Unable to read line");

        // current line of bits
        let mut curr_bits: Vec<bool> = Vec::new();

        for c in line.chars() {
            curr_bits.push(string_to_bit(c));
        }
        println!("{:?}", curr_bits);
        diagnostic_report.push(curr_bits);
    }
    return diagnostic_report;
}

// Because we can assume the input is only ever made of 1's and 0's
fn string_to_bit(c: char) -> bool {
    return c == '1';
}

fn binary_to_decimal(binary_array: &Vec<bool>) -> u32 {
    // example:
    // 16 8 4 2 1
    //  1 0 1 1 0
    // = 22
    // store decimal representation of binary array
    let mut decimal_val = 0;
    // get the first value we want to multiply by
    let mut base: u32 = 2;
    let power: usize = binary_array.len() - 1;

    base = u32::pow(base, power as u32);

    for bit in binary_array {
        if *bit {
            decimal_val += base
        }
        base /= 2;
    }
    return decimal_val;
}

// flip the bits in a binary vector
fn flip_bits(bits: Vec<bool>) -> Vec<bool> {
    let mut flipped: Vec<bool> = Vec::new();
    for bit in bits {
        flipped.push(!bit)
    }
    println!("{:?}", flipped);
    return flipped;
}

fn xor(x: bool, y: bool) -> bool {
    //returns the result of an xor between two boolean values
    return x ^ y;
}

fn rating(diagnostic_report: &Vec<Vec<bool>>, depth: usize, bias: bool) -> Vec<bool> {
    // diagnostic_report: Vec<>Vec<bool> - 2D bit array
    // depth: u32 - the vector index to get
    // bias: bool - bias towards 0 or 1 values bits
    // there is only one bit vector left -- this is the answer
    if diagnostic_report.len() == 1 {
        return diagnostic_report.get(0)
            .expect("Could not get final bit vector").to_vec();
    }

    // store the bit arrays that begin with 0 and 1
    let mut zeros: Vec<Vec<bool>> = Vec::new();
    let mut ones: Vec<Vec<bool>> = Vec::new();

    // split the diagnostic_report into two vectors containing lines that start with 0 and lines
    // that start with 1
    for bits in diagnostic_report {
        // get the bit to focus
        let curr_bit = bits.get(depth)
            .expect("Could not read Value from vector (Likely index is not accessible)");
        // add to zeros or ones
        if *curr_bit {
            ones.push(bits.clone());
        }
        else {
            zeros.push(bits.clone());
        }
    }
    // get lengths of vectors
    let n_ones = ones.len();
    let n_zeros = zeros.len();
    let biased: Vec<Vec<bool>>;
    if bias {
        biased = ones.clone();
    }
    else {
        biased = zeros.clone();
    }

    // now pass the desired array back trhough the function recursively
    if n_ones == n_zeros {
        return rating(&biased, depth + 1, bias);
    }
    else if xor(n_ones > n_zeros, !bias) {
        return rating(&ones, depth + 1, bias);
    }
    else if xor(n_ones < n_zeros, !bias) {
        return rating(&zeros, depth + 1, bias);
    }
    // this is bad practive, but it should never reach this line
    return Vec::new();
}

// count the horizontal and vertical positions and get their product
fn solve(diagnostic_report: Vec<Vec<bool>>) -> u32 {
    println!("==Computing Oxygen and CO2 report==");
    let oxygen: Vec<bool> = rating(&diagnostic_report, 0, false);
    let co2: Vec<bool>  = rating(&diagnostic_report, 0, true);
    println!("Oxygen Rating: {:?}", oxygen);
    println!("CO2 Rating: {:?}", co2);
    // convert binary arrays to decimal value
    let oxygen_rating = binary_to_decimal(&oxygen);
    let co2_rating = binary_to_decimal(&co2);
    println!("Oxygen Value: {:?}", oxygen_rating);
    println!("CO2 Value: {:?}", co2_rating);
    // answer is the product of both rates
    return oxygen_rating * co2_rating;
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
    let diagnostic_report: Vec<Vec<bool>> = read_input(String::from(filename));
    // count the number of times the measurements has increased
    let answer: u32 = solve(diagnostic_report);

    // print answer
    println!("The answer is {}", answer)
}
