// converter para python

function matriz(arr1: string[], arr2: string[]): string {
    var produto: string = '__|___' + arr2[0];
    for (var j = 1; j < arr2.length; j++) {
        produto += '___|___' + arr2[j];
    }
    
    produto += "___|";

    for (var i = 0; i < arr1.length; i++) {
        produto += "\n" + arr1[i] + " | ";
        for (var j = 0; j < arr2.length; j++) {
            produto += "<" + arr1[i] + ";" + arr2[j] + "> | ";
        }
    }
    return produto;
}

var input = require("prompt-sync")();

var vetor1: string[] = [];
var vetor2: string[] = [];
var valor: string = '';

console.clear();

console.log("Digite os valores do conjunto A(digite '/' para parar): ");
while (true) {
    valor = '';
    valor = input('> ');
    if (valor === '/') {
        break;
    }
    vetor1.push(valor);
}

console.clear();

console.log("Digite os valores do conjunto B(digite '/' para parar): ");
while (true) {
    valor = '';
    valor = input('> ');
    if (valor === '/') {
        break;
    }
    vetor2.push(valor);
}

console.clear();

console.log("O produto cartesiano de A com B é: ")
console.log(matriz(vetor1.filter((este, i) => vetor1.indexOf(este) === i), vetor2.filter((este, i) => vetor2.indexOf(este) === i)));
