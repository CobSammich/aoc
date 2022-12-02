// Advent of Code 2021 Day 2 part 1
// Written by Jacob Morris (jacobm3@vt.edu)

// In hindsight, I think it would have made more sense to make each bit array (one line from the
// input) a struct that implements the `flip_bits` and `binary_to_decimal` functions instead of
// them being standalone

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

// Transpose vector of vectors:
// https://stackoverflow.com/questions/64498617/how-to-transpose-a-vector-of-vectors-in-rust
fn transpose<T>(v: Vec<Vec<T>>) -> Vec<Vec<T>>
where
    T: Clone,
{
    assert!(!v.is_empty());
    (0..v[0].len())
        .map(|i| v.iter().map(|inner| inner[i].clone()).collect::<Vec<T>>())
        .collect()
}

fn find_most_common_bit(bits: Vec<bool>) -> bool {
    // keep track of bit frequencies
    let mut count0 = 0;
    let mut count1 = 0;

    for bit in bits {
        if bit { count1 += 1 }
        else { count0 += 1 }
    }
    //println!("0's: {}, 1's: {}", count0, count1);
    // return the most frequent bit
    // TODO how to handle equal?
    return count1 > count0;
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

// find the binary array representing the gamma rate
fn find_gamma_rate(diagnostic_report: Vec<Vec<bool>>) -> Vec<bool> {
    println!("== Computing Gamma Rate ==");
    // gamma rate represented as a vector of bits
    let mut gamma_rate: Vec<bool> = Vec::new();
    // transpose the diagnostic report so we can deal with one relevant vector at a time
    let transposed_dr = transpose(diagnostic_report);
    for bits in transposed_dr {
        let dominant_bit = find_most_common_bit(bits);
        gamma_rate.push(dominant_bit);
    }
    println!("{:?}", gamma_rate);
    return gamma_rate;
}

// count the horizontal and vertical positions and get their product
fn solve(diagnostic_report: Vec<Vec<bool>>) -> u32 {
    // gamma rate is found by the most common bit in each position
    let gamma_rate = find_gamma_rate(diagnostic_report);
    // binary to decimal: (pass in reference so ownership stays in this scope)
    let gamma_value = binary_to_decimal(&gamma_rate);
    // in this case, epsilon rate is just the opposite of the gamma rate
    let epsilon_rate = flip_bits(gamma_rate);
    let epsilon_value = binary_to_decimal(&epsilon_rate);
    println!("Gamma Rate: {}", gamma_value);
    println!("Epsilon Rate: {}", epsilon_value);
    // answer is the product of both rates
    return gamma_value * epsilon_value;
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
