

use std::io::BufReader;
use std::io::BufRead;
use std::fs::File;

pub struct Grid<T> {
    width: usize,
    height: usize,
    src: Vec<Vec<char>>,
    data: Vec<Vec<T>>,
}

impl<T> Grid<T> {
    pub fn from_file<F>(filename:String, data_from_char:F) -> Result<Grid<T>, String> where F:Fn(char) -> T {
        let m_file = File::open(filename);
        if !m_file.is_ok() {
            return Err(m_file.err().unwrap().to_string());
        }
        let reader = BufReader::new(m_file.unwrap());
        let mut width:usize = 0;
        let mut height:usize = 0;
        let mut src:Vec<Vec<char>> = Vec::with_capacity(0);
        let mut data:Vec<Vec<T>> = Vec::with_capacity(0);
        for m_line in reader.lines() {
            if !m_line.is_ok() {
                return Err(m_line.err().unwrap().to_string());
            }
            let srcline:Vec<char> = m_line.unwrap().chars().collect();
            let mut dataline:Vec<T> = Vec::with_capacity(srcline.capacity());
            let mut calcwidth:usize = 0;
            for char in srcline.iter() {
                dataline.push(data_from_char(char.clone()));
                calcwidth += 1;
            }
            if height != 0 && width != calcwidth {
                return Err("nonrectangular grid".to_string());
            }
            width = calcwidth;
            height += 1;
            src.push(srcline);
            data.push(dataline);
        }

        return Ok(Grid {
            width: width,
            height: height,
            src: src,
            data: data,
        });
    }
    pub fn width(&self) -> usize {
        return self.width;
    }
    pub fn height(&self) -> usize {
        return self.height;
    }
}