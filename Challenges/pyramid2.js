function pyramids(height) {
    // Write your code below this line
     for (let i = 0; i < height; i++) {
        let pyramidRow = '';

        for (let j = i + 1; j < height; j++) {
            pyramidRow += ' ';
        }

        for (let k = 0; k <= i; k++) {
            pyramidRow +='#';
        }

        pyramidRow += '  ';

        for (let l = 0; l <= i; l++) {
            pyramidRow += '#';
        }

        console.log(pyramidRow);
    }
}