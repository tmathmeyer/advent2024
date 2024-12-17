
use std::collections::HashMap;

fn cached_lookup(stone:usize, depth:usize, results:&mut HashMap<(usize, usize), usize>) -> usize {
    if depth == 0 {
        return 1;
    }
    let key = (depth, stone);
    let lookup =results.get(&key);
    if !lookup.is_none() {
        return *lookup.unwrap();
    }
    let digits: usize = f64::log10(stone as f64) as usize + 1;
    let splittor: usize = usize::pow(10, (digits/2) as u32);
    let value: usize = match (stone, digits%2) {
        (0, _) => cached_lookup(stone+1, depth-1, results),
        (_, 1) => cached_lookup(stone*2024, depth-1, results),
        (_, 0) => cached_lookup(stone%splittor, depth-1, results) +
                  cached_lookup((stone/splittor) as usize, depth-1, results),
        _ => 0
    };

    results.insert(key, value);
    return value;
}


fn main() {
    let mut cache = HashMap::new();
    let nums: [usize; 8] = [77, 515, 6779622, 6, 91370, 959685, 0, 9861];
    let mut sum: usize = 0;
    for num in nums {
        sum += cached_lookup(num, 75, &mut cache);
    }
    println!("{:?}", sum);
}