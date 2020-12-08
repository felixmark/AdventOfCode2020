/*
    Day 8
    Solved with huge help from Flo -> https://github.com/cheatercodes.
    Thanks a lot!
*/

use std::{fs::File, io::{BufRead, BufReader}, num::ParseIntError, str::{FromStr}};


// ============================ Parse Instruction Error ============================
#[derive(Debug)]
struct ParseInstructionError;

impl From<ParseIntError> for ParseInstructionError {
    fn from(_: ParseIntError) -> Self {
        ParseInstructionError
    }
}


// ============================ Instruction Type ============================
#[derive(Debug)]
enum InstructionType {
    ACC, JMP, NOP
}

impl FromStr for InstructionType {
    type Err = ParseInstructionError;

    fn from_str(string: &str) -> Result<Self, Self::Err> {
        match string {
            "acc" => Ok(InstructionType::ACC),
            "jmp" => Ok(InstructionType::JMP),
            "nop" => Ok(InstructionType::NOP),
            _ => Err(ParseInstructionError)
        }
    }
}


// ============================ Instruction ============================
#[derive(Debug)]
struct Instruction {
    instruction_type: InstructionType,
    value: i32,
    executed: bool
}


impl FromStr for Instruction {
    type Err = ParseInstructionError;

    fn from_str(string: &str) -> Result<Self, Self::Err> {
        let instruction_part = &string[..3];
        let value_part = &string[4..];

        let instruction_type = instruction_part.parse()?;
        let value = value_part.parse()?;

        Ok(Instruction {
            instruction_type: instruction_type,
            value: value,
            executed: false
        })
    }
}




// ============================ Main ============================
fn main() {
    // Parsing the lines of instructions
    println!("Parsing lines...");
    let file = File::open("resources/input.txt").unwrap();
    let buf_read = BufReader::new(file);
    let lines = buf_read.lines();

    
    let mut instruction_vec = Vec::<Instruction>::new();
    //let instruction_vec: Vec<Instruction> = lines.map(|line| line.unwrap().parse().unwrap()).collect();   // Same functionality with "lambda".

    for line in lines {
        if let Ok(line) = line {
            instruction_vec.push(line.parse().unwrap());
        } else {
            panic!("The line wasn't very parseable...");
        }
    }
    println!("Instructions:\n{:#?}", instruction_vec);

    let mut current_instruction = 0;
    let mut accumulator = 0;
    while !instruction_vec[current_instruction].executed {
        instruction_vec[current_instruction].executed = true;
        match instruction_vec[current_instruction].instruction_type {
            InstructionType::ACC => {
                accumulator += instruction_vec[current_instruction].value;
                current_instruction += 1;
            }
            InstructionType::JMP => {
                current_instruction = (current_instruction as i32 + instruction_vec[current_instruction].value) as usize;
            }
            InstructionType::NOP => {
                current_instruction += 1;
            }
        }
    }
    println!("Result for Task 1: {}", accumulator);
}
