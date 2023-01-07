const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
})
const fs = require('fs')
// const crypto = require('crypto')
// const id = crypto.randomBytes(16).toString("hex")
const time = Math.floor(new Date().getTime() / 100)
var globalPath = "."
var fileName = "untitled"
var fileExtension = "log"
var bin = "bin"
var ignorePath = ["bin"]
var appendMode = false

async function input() {
    return new Promise((resolve, rejects) => {
        readline.question("cin >> ", answer => {
            if (answer) {
                resolve(answer)
            } 
            else {
                resolve(globalPath)
            }
            readline.close()
        })
    })
}


async function Awake() {
    console.log("input_path : ")
    globalPath = await input()
    enumerate_files()
}

async function enumerate_files(newPath) {
    let localPath = globalPath
    if(newPath) localPath = newPath
    if(!fs.existsSync(bin)) fs.mkdirSync(bin)

    let currentScope = fs.readdirSync(localPath, "utf-8")
    for(c of currentScope){
        if(fs.statSync(`${localPath}/${c}`).isFile() && !appendMode){
            appendMode = true
            console.log(`success: ${localPath}/${c}`)
            fs.writeFileSync(`${bin}/${fileName}_${time}.${fileExtension}`, `${localPath}/${c}\n`)
        }
        else if(fs.statSync(`${localPath}/${c}`).isFile()){
            console.log(`success: ${localPath}/${c}`)
            fs.appendFileSync(`${bin}/${fileName}_${time}.${fileExtension}`, `${localPath}/${c}\n`)
        }
        else if(fs.statSync(`${localPath}/${c}`).isDirectory() && !ignorePath.includes(c)){
            enumerate_files(`${localPath}/${c}`)
        }
        else if(ignorePath.includes(c)) {
            console.log(`ignored: ${localPath}/${c}`)
        }
        else {
            console.log(`failed: ${localPath}/${c}`)
        }
    }
}

Awake()


