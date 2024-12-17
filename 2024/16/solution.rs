
use grid;

fn main() {
    let grid = grid::Grid::from_file("nano.txt".to_string(), |c| c).expect("unparsable");

    println!("{:?}x{:?}", grid.width(), grid.height());
}