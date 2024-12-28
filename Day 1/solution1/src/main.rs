use std::fs;
use std::collections::HashMap;
// use std::process;

fn main() {
    let input = fs::read_to_string("../input.txt").expect("Failed to read input");
    
    // part 1
    let (mut left, mut right): (Vec<i32>, Vec<i32>) = input
    .lines()
    .map(|line| {
        let mut nums = line.split_whitespace();
        (
            nums.next().unwrap().parse::<i32>().unwrap(),
            nums.next().unwrap().parse::<i32>().unwrap(),
        )
    })
    .unzip();

    left.sort_unstable();
    right.sort_unstable();

    let c: i32 = left
    .iter()
    .zip(&right)
    .map(|(l, r)| (l-r).abs())
    .sum();

    println!("{:?}", c);

    // part 2
    let (left_location_ids, right_location_ids_counts): (Vec<i32>, HashMap<i32, i32>) = input
    .lines()
    .map(|line| {
        let nums: Vec<&str> = line.split_whitespace().collect();
        (
            nums[0].parse::<i32>().unwrap(),
            nums[1].parse::<i32>().unwrap(),
        )
    })
    .fold((Vec::new(), HashMap::new()), |(mut ids, mut counts), (left, right)| {
        ids.push(left);
        *counts.entry(right).or_insert(0) += 1;
        (ids, counts)
    });

    let c: i32 = left_location_ids
    .iter()
    .map(|location_id| location_id * right_location_ids_counts.get(location_id).unwrap_or(&0))
    .sum();

    println!("{}", c);
}
