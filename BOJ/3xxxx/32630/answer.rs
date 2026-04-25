use std::io::{Write, BufWriter, stdout, stdin};

fn main() {
    let mut n = String::new();
    stdin().read_line(&mut n).unwrap();
    let n: usize = n.trim().parse().unwrap();

    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();
    let arr: Vec<i64> = input.trim().split_whitespace().map(|s| s.parse::<i64>().unwrap()).collect();

    let mut min1 = i64::MAX;
    let mut min2 = i64::MAX;
    let mut max1 = i64::MIN;
    let mut max2 = i64::MIN;
    let mut sum = 0;

    for &x in &arr {
        sum += x;

        if x < min1 {
            min2 = min1;
            min1 = x;
        } else if x < min2 {
            min2 = x;
        }

        if x > max1 {
            max2 = max1;
            max1 = x;
        } else if x > max2 {
            max2 = x;
        }
    }
    let ans1 = sum;
    let ans2 = sum - min1 - min2 + (min1 * min2)*2;
    let ans3 = sum - max1 - max2 + (max1 * max2)*2;

    let result = ans1.max(ans2).max(ans3);

    writeln!(BufWriter::new(stdout().lock()), "{}", result).unwrap();
}
