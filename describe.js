const fs = require('fs');

class Describe {

    constructor(){
        this.csv = fs.readFileSync("./datasets/dataset_train.csv").toString();
        this.lines = this.csv.split('\n')
        this.headers = this.lines[0].split(',')
    }

    meanCalc(){
        let mean = new Array(this.headers.length - 1);
        mean.fill(0);
        let min = [...mean];
        let max = [...mean];
        let lowP = [...mean];
        let middleP = [...mean];
        let highP = [...mean];
        for(var i = 1; i < this.lines.length; i++)
        {
            if(!this.lines[i])
                continue
            const features = this.lines[i].split(',');
            for (var j = 1; j < features.length; j++)
            {
                let num = parseFloat(features[j]);
                if(num == num){

                    mean[j - 1] += num / (this.headers.length - 1);
                    if (num < min[j - 1] || i == 1)
                        min[j - 1] = num;
                    if(num > max[j - 1] || i == 1)
                        max[j - 1] = num;
                }

            }
        }
        console.log(mean);
        console.log(min);
        console.log(max);
    }

}

let describe = new Describe;
describe.meanCalc();