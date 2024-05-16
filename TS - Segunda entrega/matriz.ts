function matriz(conjA: string[], conjB: string[]): string {
    var produto: string = '__|_' + conjB[0];
    for (var j = 1; j < conjB.length; j++) {
        produto += '_|_' + conjB[j];
    }
    
    produto += "_|";

    for (var i = 0; i < conjA.length; i++) {
        produto += "\n" + conjA[i] + " | ";
        for (var j = 0; j < conjB.length; j++) {
            if (conjA[i] == conjB[j]){
                produto += "1 | ";
            } else {
                produto += "0 | ";
            }
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

console.log("A matriz de AxB é:")
console.log(matriz(vetor1.filter((este, i) => vetor1.indexOf(este) === i), vetor2.filter((este, i) => vetor2.indexOf(este) === i)));