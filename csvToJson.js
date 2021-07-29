const fs = require("fs");

const csvJSON = (string) => {

    const csv = fs.readFileSync(string).toString();
    const lines = csv.split('\n')
    const result = []
    const headers = lines[0].split(',')

    for(i = 1; i < lines.length; i++)
    {
        if(!lines[i])
            continue
        const obj = {}
        const currentline = lines[i].split(',')
        console.log(currentline);
        headers.forEach((e, index) => {
            obj[e] = parseInt(currentline[index])
        })
        result.push(obj)
    }
    fs.writeFileSync('./datasets/data.json', JSON.stringify(result)); //JSON
    return JSON.stringify(result);
}

exports.csvJSON = csvJSON;