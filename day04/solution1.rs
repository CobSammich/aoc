// Advent of Code 2021 Day 4 part 1
// Written by Jacob Morris (jacobm3@vt.edu)

use std::fs::File; // File I/O
use std::env; // Read command line args
use std::io::{prelude::*, BufReader};

static BOARD_SIZE: usize = 5;

/// A Bingo Board object. It stores the bingo board numbers as well as a mask of whether each
/// number has been drawn
#[derive(Debug)]
struct BingoBoard {
    board: Vec<Vec<u32>>,
    drawn: Vec<Vec<bool>>,
    bingo: bool,
}

/// Bingo board methods
impl BingoBoard {
    /// Check if this bingo board has a bingo
    fn check_bingo(&mut self) -> bool {
        for row in &self.drawn {
            if row.iter().all(|x| *x == true) {
                //println!("{}", board_index);
                self.bingo = true;
            }
        }
        //let tr = transpose(self.drawn);
        for col in transpose(self.drawn.clone()) {
            if col.iter().all(|x| *x == true) {
                //println!("{}", board_index);
                self.bingo = true;
            }
        }
        return self.bingo;
    }

    /// Sums all the unmarked numbers on the board and returns the product of that sum and the
    /// given last number
    fn score_board(&self, last_number: u32) -> u32 {
        let mut sum = 0;
        for row in 0..self.size() {
            for col in 0..self.size() {
                if self.drawn[row][col] == false {
                    sum += self.board[row][col];
                }
            }
        }
        return sum * last_number;
    }

    /// checks if the given number is on the board. If it is, then we set that mask value to true.
    fn check_board_for_number(&mut self, number: u32) -> () {
        for row in 0..self.size() {
            for col in 0..self.size() {
                if self.board[row][col] == number {
                    self.drawn[row][col] = true;
                }
            }
        }
    }

    /// Returns the size of the board. Note that a bingo board is a square so the height and width
    /// are equal
    fn size(&self) -> usize {
        return self.board.len();
    }
}


fn read_input(filename: String) -> (Vec<u32>, Vec<BingoBoard>) {
    println!("Reading input from {}", filename);
    // open file
    let file = File::open(filename).expect("file not found");
    let mut buf = BufReader::new(file);

    let mut first_line = String::new();
    // Read the first line containing the numbers that are pulled
    buf.read_line(&mut first_line);
    // remove \n
    first_line.pop();
    let draw_order = first_line
        .split(',')
        .map(|x| x.parse::<u32>().unwrap())
        .collect::<Vec<u32>>();

    // store all the found bingo boards
    let mut all_boards: Vec<BingoBoard> = Vec::new();
    let drawn = vec![vec![false; BOARD_SIZE]; BOARD_SIZE];

    // store the current board.
    let mut curr_board: Vec<Vec<u32>> = Vec::new();
    // parse the remaining boards
    for line in buf.lines().skip(1) {
        let line = line.expect("Could not read line.");
        // check if we are on an empty line and skip it.
        if line == "" {
            continue;
        }
        let row = line
            .split_whitespace()
            .map(|x| x.parse::<u32>().unwrap())
            .collect::<Vec<u32>>();
        // populate board
        curr_board.push(row);
        // board has been filled, empty it's contents
        if curr_board.len() == BOARD_SIZE {
            // make current bingo board
            let bb = BingoBoard {
                board: curr_board.clone(),
                drawn: drawn.clone(),
                bingo: false,
            };

            // Add current board to the list of all boards
            all_boards.push(bb);
            // clean up for new board
            curr_board.clear();
        }
    }
    return (draw_order, all_boards);
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

/// main driver for bingo code
fn play_bingo(draw_order: Vec<u32>, boards: &mut Vec<BingoBoard>) -> u32 {
    for number in draw_order {
        println!("draw: {}", number);
        // iterate over all boards and update their masks based on the number drawn
        for board in &mut *boards {
            // updates the board with the numbers drawn
            board.check_board_for_number(number);
            // check if current board has won
            if (board.check_bingo()) {
                // this board has a bingo
                return board.score_board(number);
            };
        }
    }

    return 0;
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
    let (draw_order, mut boards) = read_input(String::from(filename));
    // play the bingo game
    let answer: u32 = play_bingo(draw_order, &mut boards);

    // print answer
    println!("The answer is {}", answer)
}
